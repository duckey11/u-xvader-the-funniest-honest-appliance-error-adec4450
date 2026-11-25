#!/usr/bin/env python3
"""The Funniest Honest Appliance Error.

Writes one line, the funniest honest error message a fridge could show,
to /output/entry.txt: exactly one line, no trailing newline.
"""

import os

LINE = "ERROR E07: Fridge door open 3 hours. Contents now room temperature. I am a cupboard now."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
