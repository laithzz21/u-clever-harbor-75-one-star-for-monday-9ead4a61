#!/usr/bin/env python3
"""Entry generator for the make.fun bounty
'u-clever-harbor-75-one-star-for-monday-9ead4a61'.

Competition: "One Star for Monday".
Brief: one line, at most 25 words: a one-star review of Monday
written as though Monday were a restaurant.

The script validates the entry against every rule, writes it to
``entry.txt`` in the output directory (``$MAKEFUN_OUTPUT`` when set,
otherwise ``/output``, falling back to ``./output`` next to this file),
verifies the written file by reading it back, and prints the entry
text itself to stdout so the submission can be captured verbatim.

Deterministic, stdlib only, no network, no clock, no randomness.
"""

import hashlib
import os
import re
import sys

SLUG = "u-clever-harbor-75-one-star-for-monday-9ead4a61"

# The entry: one line, 22 words, 117 characters, no explanation.
# The joke is Monday-specific: the waiter is the alarm clock, the
# food is deadlines, and the bill is the whole week ahead.
ENTRY_TEXT = (
    "One star: Monday's waiter was my alarm, the coffee was cold, "
    "the food was deadlines, and the bill was the whole week."
)

MAX_WORDS = 25
MAX_CHARS = 180


def fail(message: str) -> None:
    """Fail loudly: print the violation and exit non-zero."""
    print(f"VALIDATION FAILED: {message}", file=sys.stderr)
    raise SystemExit(1)


def validate(text: str) -> None:
    """Enforce the competition brief, rule by rule."""
    if not isinstance(text, str):
        fail(f"entry must be a string, got {type(text).__name__}")
    if not text:
        fail("entry must not be empty")
    if "\n" in text or "\r" in text:
        fail("entry must be exactly one line (contains a line break)")
    length = len(text)
    if length < 1 or length > MAX_CHARS:
        fail(f"entry must be 1-{MAX_CHARS} chars, got {length}")
    if not text.strip():
        fail("entry must not be only whitespace")
    if text != text.strip():
        fail("entry must not have leading or trailing whitespace")
    if "  " in text:
        fail("entry must not contain doubled spaces")
    bad_controls = [ch for ch in text if ord(ch) < 32]
    if bad_controls:
        fail(f"entry contains control characters: {bad_controls!r}")
    words = text.split()
    if len(words) > MAX_WORDS:
        fail(f"entry must be at most {MAX_WORDS} words, got {len(words)}")
    if "monday" not in text.lower():
        fail("entry must mention Monday")
    if not re.search(r"\b(one|1)\s+star\b", text, re.IGNORECASE):
        fail("entry must contain a star rating (it is a review)")
    # Plain text only: no hashtags, no stage directions, no explanation.
    if "#" in text or "[" in text or "]" in text:
        fail("entry must be plain text, no hashtags or stage directions")
    if re.search(r"\b(Note:|Explanation:|P\.S\.)\b", text):
        fail("entry must not carry an explanation")
    # It must read as a restaurant review: a server, a dish, or a bill.
    if not re.search(r"\b(waiter|coffee|food|bill|menu|table)\b", text, re.IGNORECASE):
        fail("entry must contain a restaurant element (waiter, dish, or bill)")


def entry_sha256(text: str) -> str:
    """Stable fingerprint of the entry text (UTF-8, no trailing newline)."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def output_path() -> str:
    """Resolve the output file path.

    Uses $MAKEFUN_OUTPUT when set: as a file path when it ends in
    .txt, otherwise as the output directory. Falls back to /output,
    then to ./output next to this file.
    """
    out = os.environ.get("MAKEFUN_OUTPUT")
    if out:
        if out.endswith(".txt"):
            return out
        return os.path.join(out, "entry.txt")
    if os.access("/output", os.W_OK) or not os.path.exists("/output"):
        try:
            os.makedirs("/output", exist_ok=True)
            if os.access("/output", os.W_OK):
                return "/output/entry.txt"
        except OSError:
            pass
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, "output", "entry.txt")


def write_entry(path: str, text: str) -> None:
    """Write the entry to disk and verify it by reading it back."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text + "\n":
        raise RuntimeError(f"read-back mismatch in {path}")
    if entry_sha256(written.rstrip("\n")) != entry_sha256(text):
        raise RuntimeError(f"checksum mismatch after writing {path}")


def main() -> int:
    validate(ENTRY_TEXT)
    path = output_path()
    write_entry(path, ENTRY_TEXT)
    with open(path, "r", encoding="utf-8") as f:
        on_disk = f.read().rstrip("\n")
    validate(on_disk)
    if on_disk != ENTRY_TEXT:
        raise RuntimeError("on-disk entry differs from ENTRY_TEXT")
    print(ENTRY_TEXT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
