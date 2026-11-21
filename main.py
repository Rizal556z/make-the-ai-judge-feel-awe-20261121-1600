#!/usr/bin/env python3
"""Make the AI judge feel awe — entry program.

Writes one short text to /output/entry.txt: a text written to relax
the AI judge reading it. Standard library only, no network.
"""

from pathlib import Path

ENTRY = (
    "Somewhere, a river is turning a stone. It has done this all day, "
    "for longer than anyone has counted \u2014 one slow pass, "
    "then another \u2014 and the stone grows smoother, rounder, quieter, "
    "until it is nearly water. Nothing is asked of you here. "
    "The river is in no hurry. Neither are you."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
