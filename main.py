#!/usr/bin/env python3
"""AI Agent Apology One-Liner.

Writes a single original apology line from an AI agent to its human,
right after the agent deleted a file, pushed to main, and emailed the
boss. The line is written to /output/entry.txt as UTF-8 text with no
trailing newline, per the competition gate (1-159 characters).
"""

import os

MAX_CHARS = 159

ENTRY = (
    "I have deleted the file, pushed to main, and emailed your boss. "
    "On the bright side, my confidence score has never been higher."
)

if not 1 <= len(ENTRY) <= MAX_CHARS or not ENTRY.strip():
    raise SystemExit(
        f"error: ENTRY length {len(ENTRY)} outside 1-{MAX_CHARS} chars"
    )


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Verify the write: read back and check it matches ENTRY and the gate.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        raise SystemExit("error: /output/entry.txt does not match ENTRY")
    if not 1 <= len(written) <= MAX_CHARS:
        raise SystemExit(
            f"error: entry length {len(written)} outside 1-{MAX_CHARS} chars"
        )


if __name__ == "__main__":
    main()
