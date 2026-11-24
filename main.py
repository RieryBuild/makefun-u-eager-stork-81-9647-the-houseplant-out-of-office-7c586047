"""Write the houseplant out-of-office entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only (os). Deterministic: the same line every run.
"""

import os

LINE = "Out of office: the plant by the printer. Last watered March. I've started drinking the fluorescent light out of spite."

assert 1 <= len(LINE) <= 120, "line must be 1-120 characters"
assert LINE.strip(), "line must not be whitespace-only"
assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
