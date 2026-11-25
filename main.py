#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint entry.

Writes a two-part micro-confession (a To: line plus the unsent
message itself, one line) to $MAKEFUN_OUTPUT_DIR/entry.txt.
Gate: the whole file is UTF-8 text of 1 to 260 characters and the
message line is at most 200 characters.
"""
import os
from pathlib import Path

TO_LINE = "To: Mom"
MESSAGE = (
    "I still call your number when a recipe goes wrong, just to hear "
    "your voicemail say my name like nothing happened, then I hang up "
    "and add salt until it tastes close."
)
ENTRY = TO_LINE + "\n" + MESSAGE


def build_entry() -> str:
    return ENTRY


def validate(text: str) -> None:
    """Enforce the kit gate and the two-part format before writing."""
    assert 1 <= len(text) <= 260, f"entry must be 1-260 chars, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    lines = text.split("\n")
    assert len(lines) == 2, f"entry must be exactly two lines, got {len(lines)}"
    assert lines[0].startswith("To: ") and len(lines[0]) > 4, "first line must name the addressee"
    assert lines[1] and "\n" not in lines[1], "message must be one non-empty line"
    assert len(lines[1]) <= 200, f"message must be <=200 chars, got {len(lines[1])}"


def main() -> None:
    text = build_entry()
    validate(text)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(text, encoding="utf-8")
    # Read back and verify the file landed byte for byte.
    written = out_path.read_bytes()
    assert written == text.encode("utf-8"), "written file differs from entry text"
    print(f"wrote {out_path} ({len(text)} chars)")


if __name__ == "__main__":
    main()
