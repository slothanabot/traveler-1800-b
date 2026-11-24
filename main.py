"""One Sentence for a Traveler from 1800 (account B entry).

Writes a single deadpan sentence explaining the modern internet to a
person who has just stepped out of the year 1800, using only things
such a person already knows: roads, wires, libraries, post offices,
market stalls, letters, and ink. No modern words, no list of features,
just one picture -- and a shrug at what people do with it.
"""

import os

LINE = (
    "It is a road of thin wires joining every library, post office, "
    "and market stall on earth, so a letter arrives before the ink is "
    "dry, and men still spend their evenings gossiping through it."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"Wrote {len(LINE)} characters to {path}")


if __name__ == "__main__":
    main()
