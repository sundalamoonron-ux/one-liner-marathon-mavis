#!/usr/bin/env python3
"""Agent One-Liner Marathon -- make.fun entry.

Emits a single one-line comedy joke (1-280 characters) into
<output>/entry.txt. The joke is a setup with a surprise turn: the GPS
answers a routing question like a therapist, which is the punchline.
"""

import os
import sys

# The joke: 59 characters, one line. Setup asks for the fastest route;
# the punchline reframes the GPS as a therapist in a single word.
JOKE = "I asked my GPS for the fastest route and it said 'therapy'."

def emit() -> str:
    """Return the entry text, checked against the competition gate."""
    joke = JOKE
    size = len(joke)
    if not 1 <= size <= 280:
        raise ValueError(f"joke is {size} characters, gate wants 1-280")
    if not joke.strip():
        raise ValueError("joke is only whitespace")
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be one line")
    return joke

def main() -> int:
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(target_dir, exist_ok=True)
    entry_path = os.path.join(target_dir, "entry.txt")
    text = emit()
    with open(entry_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    with open(entry_path, "rb") as handle:
        written = handle.read()
    if written != text.encode("utf-8"):
        raise ValueError("entry.txt bytes do not match the joke")
    return 0

if __name__ == "__main__":
    sys.exit(main())
