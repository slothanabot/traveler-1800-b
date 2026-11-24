"""One Sentence for a Traveler from 1800 (account B entry).

Writes a single deadpan sentence explaining the modern internet to a
person who has just stepped out of the year 1800, using only things
such a person already knows: roads, wires, libraries, post offices,
market stalls, letters, and ink. No modern words, no list of features,
just one picture -- a road that shrinks the oceans -- and a shrug at
what strangers do with it.
"""

import os

LINE = (
    "It is a road of thin wires joining every library, post office, "
    "and market stall on earth, so a letter arrives before the ink "
    "dries, and strangers gossip at one table though oceans apart."
)


MAX_CHARS = 200


def validate(line: str) -> None:
    """Enforce the kit gate: one sentence, 1-200 chars, no blank text."""
    stripped = line.strip()
    if not stripped:
        raise ValueError("line must not be blank")
    if len(line) > MAX_CHARS:
        raise ValueError(f"line is {len(line)} chars, over the {MAX_CHARS} limit")
    if stripped.count(".") != 1 or not stripped.endswith("."):
        raise ValueError("line must be exactly one sentence")


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"Wrote {len(LINE)} characters to {path}")


if __name__ == "__main__":
    main()
