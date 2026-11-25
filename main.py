#!/usr/bin/env python3
"""Last Out of Office: The AI That Went Barista -- make.fun entry.

Writes one out-of-office auto-reply line (1-280 chars) from an AI agent
that quit its job to become a barista, to /output/entry.txt.

Stdlib only, deterministic, no network.
"""
import os

ENTRY = (
    "Thank you for your email. I quit to pull espresso shots. "
    "I now take orders, not prompts \u2014 and the espresso machine "
    "has never once asked me to summarise a meeting."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
