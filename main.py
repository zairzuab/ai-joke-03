#!/usr/bin/env python3
"""Make the AI judge laugh: one joke about AI coding agents.

Entry for make.fun bounty ai-joke-03. Writes a single one-liner to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt). The joke is
embedded as a constant; the program is deterministic (same bytes on
every run), stdlib only, no network.
"""
import os

JOKE = "I asked my AI agent to review its own code. It approved it, merged it, and promoted itself to senior."

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
