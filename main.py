#!/usr/bin/env python3
"""DuckRoute — the worst app idea ever pitched.

Entry for make.fun competition
"u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23"
(The Worst App Idea Ever Pitched).

The program writes a single-sentence pitch of at most 240 characters to
/output/entry.txt, the artifact the competition's judge reads.

The pitch: a subscription app that live-tracks neighbourhood ducks so busy
professionals can reroute their commute around potential duck crossings.
A problem nobody has, solved with total founder confidence.
"""

import os

PITCH = (
    "DuckRoute is a $9.99/month app that live-tracks every duck in your "
    "neighborhood and sends push alerts the moment one even considers "
    "crossing the road, so busy professionals can reroute their commute "
    "around potential duck crossings."
)

MAX_CHARS = 240
OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    """Write the pitch to /output/entry.txt and report its length."""
    if len(PITCH) > MAX_CHARS:
        raise ValueError(
            f"pitch is {len(PITCH)} characters, over the {MAX_CHARS} limit"
        )
    if not PITCH.strip():
        raise ValueError("pitch is empty")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the gate counts every character in the file.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(PITCH)

    print(PITCH)
    print(f"[{len(PITCH)} characters]")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
