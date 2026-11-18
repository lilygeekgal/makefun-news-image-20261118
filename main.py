#!/usr/bin/env python3
"""Write the entry image to the grader's output directory.

The image (a front page summing up the world's news of Wednesday
18 November 2026) is stored in this repository as entry.png. This
program copies it byte for byte to $MAKEFUN_OUTPUT_DIR/entry.png
(default /output). It uses only the standard library, makes no
network access, and writes identical bytes on every run.
"""
import os
import shutil
import sys

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.png")
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main() -> int:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT_PATH)
    # Confirm the copy is whole: a PNG header and the source's byte count.
    with open(OUTPUT_PATH, "rb") as fh:
        data = fh.read()
    if not data.startswith(PNG_MAGIC):
        print("entry.png is not a PNG file", file=sys.stderr)
        return 1
    if len(data) != os.path.getsize(SOURCE):
        print("copied file size differs from source", file=sys.stderr)
        return 1
    print(f"wrote {OUTPUT_PATH} ({len(data)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
