#!/usr/bin/env python3
"""The Excuse That Almost Works — entry program.

Writes one excuse to /output/entry.txt.

The line (77 characters, 16 words):
  Been up all night with the baby, she's finally asleep on me and I can't move.

Deterministic: the same bytes on every run. No network, no dependencies,
no environment reads, no files outside this repository.
"""

import os

LINE = "Been up all night with the baby, she's finally asleep on me and I can't move."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate check, same rule as the sealed scorer: 1 to 140 characters,
    # and at most 20 words, as the brief requires.
    if not 1 <= len(LINE) <= 140:
        raise SystemExit("line is %d characters, outside the 1-140 gate" % len(LINE))
    if len(LINE.split()) > 20:
        raise SystemExit("line is %d words, over the 20-word limit" % len(LINE.split()))
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(LINE.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
