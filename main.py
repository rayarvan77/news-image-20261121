#!/usr/bin/env python3
"""Deliver the news-image-20261121 entry to the grader.

The picture itself is committed here as ``entry.png``: a front page for
Saturday 21 November 2026, drawn from the day's news. This script is the
whole entry program. It copies that file to the place the grader reads,
``/output/entry.png``, and then proves the copy is the file it claims to
be: the same bytes, a PNG of 1024 by 1024, and smaller than the 1 MiB the
competition allows.

It needs nothing but the Python 3.13 standard library, talks to no
network, and takes no arguments. To try it on this machine:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

Leave ``MAKEFUN_OUTPUT_DIR`` unset and it uses ``./output`` instead.
"""

import hashlib
import os
import shutil
import struct
from pathlib import Path

# Where the picture lives, and where the grader expects it.
SOURCE = Path(__file__).resolve().parent / "entry.png"
DEST_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "output")
DEST = DEST_DIR / "entry.png"

# What the competition asks of the picture.
WANTED_WIDTH = 1024
WANTED_HEIGHT = 1024
BYTE_LIMIT = 1024 * 1024

# A PNG file opens with these eight bytes, then an IHDR chunk whose first
# eight data bytes are the width and the height, big-endian.
MAGIC = b"\x89PNG\r\n\x1a\n"


def sha256_hex(path: Path) -> str:
    """Hash a file's bytes and return the digest as hex."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def png_dimensions(path: Path) -> tuple[int, int]:
    """Pull the width and height out of a PNG file's IHDR chunk."""
    with path.open("rb") as handle:
        head = handle.read(33)
    if head[:8] != MAGIC:
        raise SystemExit(f"{path}: not a PNG file (bad magic bytes)")
    if head[12:16] != b"IHDR":
        raise SystemExit(f"{path}: no IHDR chunk where one belongs")
    width, height = struct.unpack(">II", head[16:24])
    return width, height


def deliver() -> None:
    """Copy the entry picture into place and check it every way that matters."""
    if not SOURCE.is_file():
        raise SystemExit(f"entry picture is missing: {SOURCE}")
    DEST_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, DEST)

    if sha256_hex(DEST) != sha256_hex(SOURCE):
        raise SystemExit("the copy is not byte-identical to entry.png")
    size = DEST.stat().st_size
    if size > BYTE_LIMIT:
        raise SystemExit(f"the picture is {size} bytes, over the 1 MiB limit")
    width, height = png_dimensions(DEST)
    if (width, height) != (WANTED_WIDTH, WANTED_HEIGHT):
        raise SystemExit(f"the picture is {width}x{height}, want 1024x1024")
    print(f"delivered {width}x{height} PNG, {size} bytes, to {DEST}")


if __name__ == "__main__":
    deliver()
