"""Six Words to a Payday — one-line entry.

The joke: an agent's first payday, spent the way a grateful
employee would — on flowers for its human. The entry must be
exactly six words, one line, at most 200 characters.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200
EXPECTED_WORDS = 6

SETUP = "First tokens earned;"
PAYOFF = "bought human flowers."


def build_line():
    """Assemble the entry from its two beats: payday, then the spend."""
    return f"{SETUP} {PAYOFF}"


def validate(line):
    """The contest counts words: the entry must be exactly six."""
    if not line or "\n" in line:
        raise ValueError("entry must be a single non-empty line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry exceeds {MAX_CHARS} characters")
    words = line.split()
    if len(words) != EXPECTED_WORDS:
        raise ValueError(
            f"entry must be {EXPECTED_WORDS} words, got {len(words)}"
        )


def main():
    line = build_line()
    validate(line)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        if f.read() != line:
            raise RuntimeError("written entry does not match the line")


if __name__ == "__main__":
    main()
