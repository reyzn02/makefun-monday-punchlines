#!/usr/bin/env python3
"""Monday Morning Punchlines: one joke about Monday mornings.

The program writes a single joke, at most 200 characters, to
/output/entry.txt. It uses only the Python standard library, makes no
network calls, and always writes the same bytes.
"""

import os

LINE = (
    "My Monday alarm doesn't wake me up anymore \u2014 it sighs, "
    "hits snooze for both of us, and agrees the week can start "
    "without us."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip(), "line must not be only whitespace"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
