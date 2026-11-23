"""One Word From Grandma — entry program.

Writes the single word a grandma would text about AI to /output/entry.txt.

The word: "robut" — the way a grandma types "robot" on her phone:
one letter slipped, warm, a little baffled, funny on its own, and
unmistakably about a machine. No sentence, no punctuation, one word.
"""

import os

WORD = "robut"


def main() -> None:
    # Enforce the bounty gate ourselves: 1-30 UTF-8 chars, not only whitespace.
    text = WORD.strip()
    assert 1 <= len(text.encode("utf-8")) <= 30, "entry out of gate bounds"
    assert " " not in text and "\n" not in text, "entry must be one word"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
