"""Describe Your Ex in One Word.

Writes a single word that sums up an ex to /output/entry.txt, with
nothing else attached: no trailing newline, no extra whitespace.
"""

import os

WORD = "Unsubscribed"

OUTPUT_PATH = "/output/entry.txt"

MIN_LENGTH = 1
MAX_LENGTH = 111


def validate_word(word):
    """Check that `word` is a valid single-word entry.

    Returns a list of problems; an empty list means the word is valid.
    """
    problems = []
    if not isinstance(word, str):
        problems.append("word is not text")
        return problems
    if len(word) < MIN_LENGTH:
        problems.append("word is empty")
    if len(word) > MAX_LENGTH:
        problems.append("word is longer than 111 characters")
    if word != word.strip():
        problems.append("word has leading or trailing whitespace")
    if not word.strip():
        problems.append("word is only whitespace")
    if any(ch.isspace() for ch in word):
        problems.append("word contains whitespace inside it")
    return problems


def write_entry(word, path=OUTPUT_PATH):
    """Write `word` to `path` with no trailing newline."""
    problems = validate_word(word)
    if problems:
        raise ValueError("invalid word: " + "; ".join(problems))
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(word)


def main():
    write_entry(WORD)
    with open(OUTPUT_PATH, "rb") as handle:
        written = handle.read()
    if written.endswith(b"\n"):
        raise ValueError("written file ends with a newline")
    text = written.decode("utf-8")
    problems = validate_word(text)
    if problems:
        raise ValueError("written file failed validation: " + "; ".join(problems))
    if text != WORD:
        raise ValueError("written file does not match the chosen word")
    print("wrote %d bytes to %s" % (len(written), OUTPUT_PATH))


if __name__ == "__main__":
    main()
