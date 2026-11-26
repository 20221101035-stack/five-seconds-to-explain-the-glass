#!/usr/bin/env python3
"""Five Seconds to Explain the Glass entry for make.fun.

Writes one original sentence - the excuse a house cat gives in the five
seconds after knocking a glass off the table - to entry.txt.
Deterministic, standard library only: the same bytes every run.
"""

import os

EXCUSE = (
    "That glass was empty, parked in my sunbeam, and contributing nothing "
    "to this household, so I liquidated it."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
