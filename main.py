"""Entry program for the news-image-20261121 bounty.

The entry image lives in this repository as entry.png: a newspaper
front page summing up Saturday 21 November 2026 in six panels. This
program places an exact copy of it where the grader looks, at
/output/entry.png, so the judge sees precisely the bytes committed
here.

Python 3.13, standard library only; no network access, no arguments.
Run it locally with:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

Without MAKEFUN_OUTPUT_DIR it writes to ./output/entry.png instead.
"""

import hashlib
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
IMAGE = HERE / "entry.png"
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "output")
OUT_PATH = OUT_DIR / "entry.png"

# The eight bytes every PNG file starts with.
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"

# The competition caps the image at 1 MiB.
MAX_BYTES = 1024 * 1024


def fingerprint(path: Path) -> str:
    """Return the sha256 hex digest of a file's bytes."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inspect_png(path: Path) -> tuple[int, int]:
    """Read a PNG header and return its (width, height) in pixels."""
    with path.open("rb") as handle:
        head = handle.read(33)
    if head[:8] != PNG_SIGNATURE:
        raise RuntimeError("output is not a PNG file")
    if head[12:16] != b"IHDR":
        raise RuntimeError("output has no PNG IHDR chunk")
    width = int.from_bytes(head[16:20], "big")
    height = int.from_bytes(head[20:24], "big")
    return width, height


def main() -> None:
    """Copy entry.png to the output directory and prove it matches."""
    if not IMAGE.is_file():
        raise RuntimeError(f"entry image missing: {IMAGE}")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(IMAGE, OUT_PATH)
    if fingerprint(OUT_PATH) != fingerprint(IMAGE):
        raise RuntimeError("copied image differs from entry.png")
    if OUT_PATH.stat().st_size > MAX_BYTES:
        raise RuntimeError("entry image is over the 1 MiB limit")
    width, height = inspect_png(OUT_PATH)
    if (width, height) != (1024, 1024):
        raise RuntimeError(f"entry image is {width}x{height}, want 1024x1024")


if __name__ == "__main__":
    main()
