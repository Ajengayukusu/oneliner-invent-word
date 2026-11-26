# Invent a Word We Need — one coinage for make.fun's
# "Invent a Word We Need" bounty.
#
# Judge brief: coin a new English word and define it in one clear line
# of at most 140 characters; the word must fill a real gap — something
# English has no word for that a reader recognises at once; the
# definition exact and self-contained, landing in one reading; the word
# sayable, spellable and memorable, as if English could have grown it.
#
# The coinage: "threshnesia" — threshold + amnesia. Everyone knows the
# moment: you walk through a doorway and the reason you came evaporates.
# Science calls it the doorway effect; nobody has a word for the blank
# half-second itself. This one sounds like a diagnosis and a shrug at
# the same time, which is exactly how it feels.
#
# SPDX-License-Identifier: MIT
import os
import sys
from pathlib import Path

LINE = (
    "threshnesia (n.): the blank half-second after you walk through a "
    "doorway and forget why you came."
)

MAX_CHARS = 140


def entry_line() -> str:
    line = LINE.strip()
    if not line:
        raise ValueError("entry line must not be empty")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry line is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if "  " in line:
        raise ValueError("entry must not contain double spaces")
    if any(ord(c) < 32 or ord(c) == 127 for c in line):
        raise ValueError("entry must not contain control characters")
    # Dictionary form: the coined word first, then its part of speech,
    # then the definition — the word must be the line's first token.
    if not line.startswith("threshnesia (n.):"):
        raise ValueError("entry must open with the coined word and its marker")
    return line


def output_path() -> Path:
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(base) / "entry.txt"


def run() -> int:
    line = entry_line()
    dest = output_path()
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(line, encoding="utf-8")
    print(f"wrote {len(line)} characters to {dest}")
    return 0


if __name__ == "__main__":
    sys.exit(run())
