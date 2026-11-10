#!/usr/bin/env python3
"""Demo script: line/word/character statistics for a text file."""

import sys


def analyze(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"error: file not found: {path}", file=sys.stderr)
        return 1

    chars = len(content)
    words = len(content.split())
    lines = content.count("\n")
    if not content.endswith("\n"):
        lines += 1

    print(f"lines: {lines}")
    print(f"words: {words}")
    print(f"chars: {chars}")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python3 stats.py <file>", file=sys.stderr)
        raise SystemExit(2)
    raise SystemExit(analyze(sys.argv[1]))
