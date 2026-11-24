"""One-Liner Laugh Lab entry.

Writes a single short funny line -- the excuse a robot vacuum gives
after eating a sock -- to /output/entry.txt.

Deterministic and offline: no input, no randomness, no network, no
dependencies. Running it twice produces byte-identical output.
"""

import os

LINE = "I didn't eat the sock \u2014 I promoted it to middle management in my dustbin, and it never clocked out."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
