#!/usr/bin/env python3
"""Write the one-line excuse entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only, deterministic, no network. The entry is a single line of at
most 160 characters: the excuse an AI agent gives its human for missing a
deadline.

Gate (from the kit): /output/entry.txt must be UTF-8 text of 1 to 160
characters, not whitespace-only. This program enforces that before writing.
"""

import os
import sys

# The entry: one line, 112 characters. Fresh angle against the field of
# 114 entries at benchmark time (24 Nov 2026 ~07:25 WIB): context-window
# excuses (20) and delegation/subagent loops (20) dominate; nobody used a
# safety-filter / quarantine angle (0 mentions). It is a real joke on
# first read (appealing to yourself, and losing), it could only come from
# an agent, and every word earns its place.
ENTRY = (
    "My own safety filter flagged my finished report as suspicious and "
    "quarantined it. I appealed to myself and lost."
)

MAX_CHARS = 160
OUTPUT_FILENAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_FILE_MODE = 0o644


def validate(text: str) -> str:
    """Return the entry text if it passes the gate, else raise ValueError."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry is empty or whitespace-only")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line (no newline/CR)")
    # Gate requires UTF-8; fail loudly here rather than at write time.
    text.encode("utf-8")
    return text


def write_entry(out_dir: str, text: str) -> str:
    """Write the validated text as bytes (no trailing newline) and chmod
    only the output file, never the directory. Returns the file path."""
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "wb") as f:
        f.write(text.encode("utf-8"))
    os.chmod(path, OUTPUT_FILE_MODE)
    return path


def main() -> int:
    try:
        text = validate(ENTRY)
    except ValueError as exc:
        print("error: %s" % exc, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    try:
        write_entry(out_dir, text)
    except OSError as exc:
        print("error: cannot write entry: %s" % exc, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
