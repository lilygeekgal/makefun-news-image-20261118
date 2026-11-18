#!/usr/bin/env python3
"""make.fun news-image-20261118 entry.

The entry is one picture: a newspaper front page that sums up the
world news of Wednesday 18 November 2026. The picture is stored in
this repository as entry.png. This program copies it, byte for byte,
to the grader's output directory, $MAKEFUN_OUTPUT_DIR/entry.png
(default /output).

It only uses the Python standard library, makes no network requests,
and writes the same bytes on every run.
"""

import os
import shutil
import sys
from pathlib import Path


def main() -> int:
    source = Path(__file__).resolve().parent / "entry.png"
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target = output_dir / "entry.png"

    if not source.is_file():
        print(f"error: source image not found: {source}", file=sys.stderr)
        return 1

    png_signature = b"\x89PNG\r\n\x1a\n"
    with source.open("rb") as handle:
        header = handle.read(len(png_signature))
    if header != png_signature:
        print(f"error: source image is not a PNG file: {source}", file=sys.stderr)
        return 1

    output_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)
    print(f"wrote {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
