#!/usr/bin/env python3
"""
LLM API Monitor - Transparent proxy that logs requests/responses to LLM backends.

Usage:
    python llm_monitor.py [--port 8080] [--target https://api.anthropic.com]

Then point your program at http://localhost:8080 instead of the real API.
Set the base URL in your SDK, e.g.:
    - Anthropic Python: anthropic.Anthropic(base_url="http://localhost:8080")
    - OpenAI Python:    openai.OpenAI(base_url="http://localhost:8080/v1")
"""

import argparse
import json
import sys
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import urllib.parse

# ── Config ────────────────────────────────────────────────────────────────────

DEFAULT_PORT   = 8080
DEFAULT_TARGET = "http://localhost:1234"
STREAM_CHUNK_SIZE = 4096

# ── Formatting helpers ─────────────────────────────────────────────────────────

RESET  = "\033[0m"
BOLD   = "\033[1m"
CYAN   = "\033[36m"
GREEN  = "\033[32m"
YELLOW = "\033[33m"
RED    = "\033[31m"
DIM    = "\033[2m"

def separator(label: str, color: str = CYAN):
    width = 72
    bar = "─" * ((width - len(label) - 2) // 2)
    print(f"\n{color}{BOLD}{bar} {label} {bar}{RESET}", flush=True)

def pretty_json(data) -> str:
    if isinstance(data, (str, bytes)):
        try:
            data = json.loads(data)
        except Exception:
            return str(data)
    return json.dumps(data, indent=2, ensure_ascii=False)

def print_messages(messages):
    """Print the messages array in a readable format."""
    for i, msg in enumerate(messages):
        role = msg.get("role", "?").upper()
        color = GREEN if role == "USER" else YELLOW
        content = msg.get("content", "")
        if isinstance(content, list):
            # Multi-modal content blocks
            for block in content:
                btype = block.get("type", "?")
                if btype == "text":
                    print(f"  {color}{BOLD}[{role}]{RESET} {block['text']}", flush=True)
                else:
                    print(f"  {color}{BOLD}[{role} / {btype}]{RESET} {pretty_json(block)}", flush=True)
        else:
            print(f"  {color}{BOLD}[{role}]{RESET} {content}", flush=True)

# ── Proxy handler ──────────────────────────────────────────────────────────────

class LLMProxyHandler(BaseHTTPRequestHandler):
    target: str = DEFAULT_TARGET

    def log_message(self, fmt, *args):
        pass  # suppress default access log

    def do_POST(self):
        self._proxy("POST")

    def do_GET(self):
        self._proxy("GET")

    def _proxy(self, method):
        # ── Read request body ──────────────────────────────────────────────
        content_length = int(self.headers.get("Content-Length", 0))
        body_bytes = self.rfile.read(content_length) if content_length else b""

        target_url = self.target.rstrip("/") + self.path
        t_start = time.monotonic()

        # ── Log request ───────────────────────────────────────────────────
        separator(f"REQUEST  {method} {self.path}")
        if body_bytes:
            try:
                body = json.loads(body_bytes)
                model   = body.get("model", "?")
                system  = body.get("system")
                msgs    = body.get("messages", [])
                stream  = body.get("stream", False)

                print(f"  {DIM}model   :{RESET} {model}")
                print(f"  {DIM}stream  :{RESET} {stream}")
                if system:
                    print(f"\n  {BOLD}SYSTEM PROMPT:{RESET}")
                    if isinstance(system, list):
                        for blk in system:
                            print(f"    {blk.get('text','')}", flush=True)
                    else:
                        print(f"    {system}", flush=True)
                if msgs:
                    print(f"\n  {BOLD}MESSAGES:{RESET}")
                    print_messages(msgs)
                # Show other top-level params (tools, temperature, etc.)
                extras = {k: v for k, v in body.items()
                          if k not in ("model","stream","system","messages")}
                if extras:
                    print(f"\n  {DIM}other params:{RESET}")
                    for k, v in extras.items():
                        print(f"    {k}: {pretty_json(v)}")
            except Exception:
                print(body_bytes.decode(errors="replace"), flush=True)
        print(flush=True)

        # ── Forward request ────────────────────────────────────────────────
        forward_headers = {
            k: v for k, v in self.headers.items()
            if k.lower() not in ("host", "content-length")
        }
        req = Request(target_url, data=body_bytes or None,
                      headers=forward_headers, method=method)

        try:
            resp = urlopen(req)
            status = resp.status
            resp_headers = dict(resp.headers)
            resp_body = resp.read()
        except HTTPError as e:
            status = e.code
            resp_headers = dict(e.headers)
            resp_body = e.read()

        elapsed = time.monotonic() - t_start

        # ── Log response ───────────────────────────────────────────────────
        status_color = GREEN if 200 <= status < 300 else RED
        separator(f"RESPONSE  {status_color}{status}{RESET}{CYAN}  ({elapsed:.2f}s)")
        try:
            resp_json = json.loads(resp_body)

            # ── Anthropic format: { content: [{type, text}, ...] } ─────────
            if "content" in resp_json:
                content_blocks = resp_json.get("content", [])
                if content_blocks:
                    print(f"  {BOLD}ASSISTANT RESPONSE:{RESET}")
                    for blk in content_blocks:
                        btype = blk.get("type", "?")
                        if btype == "text":
                            print(f"  {YELLOW}{BOLD}[ASSISTANT]{RESET} {blk['text']}", flush=True)
                        else:
                            print(f"  {YELLOW}{BOLD}[ASSISTANT / {btype}]{RESET}")
                            print(f"  {pretty_json(blk)}", flush=True)

            # ── OpenAI format: { choices: [{message: {role, content}}, ...] }
            elif "choices" in resp_json:
                choices = resp_json["choices"]
                print(f"  {BOLD}ASSISTANT RESPONSE:{RESET}")
                for i, choice in enumerate(choices):
                    msg = choice.get("message") or choice.get("delta", {})
                    role    = msg.get("role", "assistant").upper()
                    content = msg.get("content") or ""
                    tool_calls = msg.get("tool_calls")
                    finish  = choice.get("finish_reason", "")

                    if content:
                        print(f"  {YELLOW}{BOLD}[{role}]{RESET} {content}", flush=True)
                    if tool_calls:
                        print(f"  {YELLOW}{BOLD}[{role} / tool_calls]{RESET}")
                        for tc in tool_calls:
                            fn   = tc.get("function", {})
                            name = fn.get("name", "?")
                            try:
                                args = pretty_json(json.loads(fn.get("arguments", "{}")))
                            except Exception:
                                args = fn.get("arguments", "")
                            print(f"    call: {BOLD}{name}{RESET}({args})", flush=True)
                    if finish and finish != "stop":
                        print(f"  {DIM}finish_reason: {finish}{RESET}", flush=True)

            # ── Unknown / error body ───────────────────────────────────────
            else:
                print(pretty_json(resp_json), flush=True)

            # ── Usage stats (both formats use "usage") ─────────────────────
            usage = resp_json.get("usage")
            if usage:
                print(f"\n  {DIM}usage: {usage}{RESET}", flush=True)

            if "error" in resp_json:
                print(f"\n  {RED}ERROR:{RESET} {pretty_json(resp_json['error'])}", flush=True)

        except Exception:
            print(resp_body.decode(errors="replace"), flush=True)
        print(flush=True)

        # ── Forward response to client ─────────────────────────────────────
        self.send_response(status)
        for k, v in resp_headers.items():
            if k.lower() not in ("transfer-encoding",):
                try:
                    self.send_header(k, v)
                except Exception:
                    pass
        self.send_header("Content-Length", str(len(resp_body)))
        self.end_headers()
        self.wfile.write(resp_body)


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="LLM API monitor proxy")
    parser.add_argument("--port",   type=int, default=DEFAULT_PORT,   help="Local port to listen on")
    parser.add_argument("--target", type=str, default=DEFAULT_TARGET, help="Target API base URL")
    args = parser.parse_args()

    LLMProxyHandler.target = args.target.rstrip("/")

    print(f"{BOLD}{CYAN}LLM Monitor{RESET}")
    print(f"  Listening : {BOLD}http://localhost:{args.port}{RESET}")
    print(f"  Forwarding: {BOLD}{args.target}{RESET}")
    print(f"\nPoint your SDK's base_url at http://localhost:{args.port}")
    print(f"Press Ctrl-C to stop.\n")

    server = HTTPServer(("localhost", args.port), LLMProxyHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print(f"\n{DIM}Stopped.{RESET}")
        sys.exit(0)

if __name__ == "__main__":
    main()
