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
from pprint import pprint
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import urllib.parse

# ── Config ────────────────────────────────────────────────────────────────────

DEFAULT_PORT   = 8080
DEFAULT_TARGET = "http://localhost:1234"
# DEFAULT_TARGET = "https://api.anthropic.com"
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
        pprint(self.headers.items())
        if body_bytes:
            try:
                body = json.loads(body_bytes)
                print(pretty_json(body))
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
        pprint(resp_headers)
        try:
            resp_json = json.loads(resp_body)
            print(pretty_json(resp_json))
        except Exception:
            print(resp_body.decode(errors="replace"), flush=True)
        print(flush=True)

        # ── Forward response to client ─────────────────────────────────────
        self.send_response(status)
        for k, v in resp_headers.items():
            if k.lower() not in ("transfer-encoding", "content-length"):
                try:
                    self.send_header(k, v)
                except Exception:
                    pass
        self.send_header("Content-Length", str(len(resp_body)))
        self.end_headers()
        self.wfile.write(resp_body)

def run_proxy(port, target):
    LLMProxyHandler.target = target

    print(f"{BOLD}{CYAN}LLM Monitor{RESET}")
    print(f"  Listening : {BOLD}http://localhost:{port}{RESET}")
    print(f"  Forwarding: {BOLD}{target}{RESET}")
    print(f"\nPoint your SDK's base_url at http://localhost:{port}")
    print(f"Press Ctrl-C to stop.\n")

    server = HTTPServer(("localhost", port), LLMProxyHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print(f"\n{DIM}Stopped.{RESET}")
        sys.exit(0)

# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="LLM API monitor proxy")
    parser.add_argument("--port",   type=int, default=DEFAULT_PORT,   help="Local port to listen on")
    parser.add_argument("--target", type=str, default=DEFAULT_TARGET, help="Target API base URL")
    args = parser.parse_args()

    run_proxy(args.port, args.target.rstrip("/"))

if __name__ == "__main__":
    main()
