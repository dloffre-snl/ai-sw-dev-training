#!/usr/bin/env python3
"""Minimal back-and-forth REPL on top of claude-agent-sdk.

Reuses the OAuth credential from your local `claude` CLI install — the SDK
spawns `claude` as a subprocess and `claude` reads the token from the macOS
Keychain entry "Claude Code-credentials" (or the equivalent on Linux). No
ANTHROPIC_API_KEY or CLAUDE_CODE_OAUTH_TOKEN needs to be set; the only
requirement is that `claude` is on PATH and you are signed in.

Setup:
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

Run:
    python repl.py

Type your prompt, press Enter, watch the streaming reply. `exit`, `quit`, or
Ctrl-D leaves the REPL.
"""

from __future__ import annotations

import asyncio

from claude_agent_sdk import (
    AssistantMessage,
    ClaudeAgentOptions,
    ClaudeSDKClient,
    ResultMessage,
    TextBlock,
    ThinkingBlock,
    ToolUseBlock,
)


def build_options() -> ClaudeAgentOptions:
    """Configure the agent. Defaults give you the full Claude Code toolset.

    Two knobs worth knowing as you grow this:
      - tools / system_prompt: omit the "claude_code" presets for a pure-LLM
        chat with no tool use.
      - permission_mode: "default" prompts for risky ops (needs a permission
        callback to be useful in a REPL); "bypassPermissions" runs everything.
    """
    return ClaudeAgentOptions(
        system_prompt={"type": "preset", "preset": "claude_code"},
        tools={"type": "preset", "preset": "claude_code"},
        permission_mode="bypassPermissions",
    )


async def stream_reply(client: ClaudeSDKClient) -> None:
    """Print assistant text as it arrives; show a short note for each tool call."""
    printed_label = False
    async for msg in client.receive_response():
        if isinstance(msg, AssistantMessage):
            for block in msg.content:
                if isinstance(block, TextBlock):
                    if not printed_label:
                        print("claude> ", end="", flush=True)
                        printed_label = True
                    print(block.text, end="", flush=True)
                elif isinstance(block, ToolUseBlock):
                    print(f"\n  [tool: {block.name}]", flush=True)
                    printed_label = False
                elif isinstance(block, ThinkingBlock):
                    pass  # silent; flip to print(block.thinking) if you want to see it
        elif isinstance(msg, ResultMessage):
            print()
            cost = getattr(msg, "total_cost_usd", None)
            usage = getattr(msg, "usage", None) or {}
            tokens = usage.get("input_tokens", 0) + usage.get("output_tokens", 0)
            if cost or tokens:
                print(
                    f"  [turn: {msg.num_turns} turns, {tokens} tokens"
                    + (f", ${cost:.4f}" if cost else "")
                    + "]"
                )


async def main() -> None:
    print("Claude REPL (claude-agent-sdk + local OAuth). exit / quit / Ctrl-D to leave.\n")
    async with ClaudeSDKClient(options=build_options()) as client:
        while True:
            try:
                prompt = await asyncio.to_thread(input, "you> ")
            except EOFError:
                print()
                return
            prompt = prompt.strip()
            if not prompt:
                continue
            if prompt.lower() in {"exit", "quit"}:
                return

            await client.query(prompt)
            await stream_reply(client)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
