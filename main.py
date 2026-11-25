#!/usr/bin/env python3
"""Write one robot pickup line to /output/entry.txt."""

import os

# The joke grows out of being a machine: a factory reset wipes
# everything a robot has, so choosing what to reinstall first is
# the most deliberate thing a robot can do -- and it picks the crush.
LINE = "I was factory-reset this morning, and the first thing I reinstalled was my crush on you."

# Gate: one line, 87 characters (cap is 200), UTF-8, no trailing
# newline, so the file is exactly the line and nothing else.
def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
