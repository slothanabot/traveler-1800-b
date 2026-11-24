"""One Sentence for a Traveler from 1800 (account B entry).

Writes a single deadpan sentence explaining the modern internet to a
person who has just stepped out of the year 1800, using only things
such a person already knows: roads, wires, libraries, post offices,
letters, ink, and the evening gossip of idle men. No modern words, no
list of features, just one picture -- a road of wires linking every
library and post office on earth, so a letter reaches the far side
before the ink dries -- and a shrug at what men do with it.
"""

import os
import re

LINE = (
    "A road of wires links every library and post office on earth, "
    "so a letter reaches the far side before the ink dries, and men "
    "still waste their evenings gossiping over it."
)


MAX_CHARS = 200

# Words coined after 1800 that a traveler of that year could not know.
# The sentence must stay free of them so the picture stays in-period.
FORBIDDEN_WORDS = (
    "internet",
    "computer",
    "website",
    "email",
    "online",
    "digital",
    "screen",
    "phone",
)


def validate(line: str) -> None:
    """Enforce the kit gate: one sentence, 1-200 chars, no blank text,
    and no word a person of 1800 could not know."""
    stripped = line.strip()
    if not stripped:
        raise ValueError("line must not be blank")
    if "  " in stripped:
        raise ValueError("line must not contain double spaces")
    if len(line) > MAX_CHARS:
        raise ValueError(f"line is {len(line)} chars, over the {MAX_CHARS} limit")
    if stripped.count(".") != 1 or not stripped.endswith("."):
        raise ValueError("line must be exactly one sentence")
    words = set(re.findall(r"[a-z]+", stripped.lower()))
    bad = sorted(words & set(FORBIDDEN_WORDS))
    if bad:
        raise ValueError(f"line uses modern words: {', '.join(bad)}")


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
