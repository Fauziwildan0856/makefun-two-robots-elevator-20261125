"""Two Robots in an Elevator -- make.fun entry program.

Writes one line of awkward robot small talk to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Stdlib only, fully deterministic: the same entry
text is written on every run.
"""

import os
import sys

ENTRY = (
    "I calculated a 97% chance this silence is awkward, "
    "so my firmware requires me to ask: do you come up here often?"
)

MAX_CHARS = 200


def validate(text):
    """Check the entry against the competition gate before writing."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if len(text) < 1 or len(text) > MAX_CHARS:
        raise ValueError(
            "entry must be 1-200 characters, got %d" % len(text)
        )
    if text.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 32 and ch not in ("\t",) for ch in text):
        raise ValueError("entry must not contain control characters")
    text.encode("utf-8")  # raises UnicodeEncodeError if not UTF-8


def main():
    try:
        validate(ENTRY)
    except ValueError as exc:
        print("error: invalid entry: %s" % exc, file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_path = os.path.join(output_dir, "entry.txt")

    try:
        os.makedirs(output_dir, exist_ok=True)
        with open(output_path, "w", encoding="utf-8", newline="") as f:
            f.write(ENTRY)  # no trailing newline
        # Read back and verify the file holds exactly the validated entry.
        with open(output_path, "rb") as f:
            written = f.read()
        if written != ENTRY.encode("utf-8"):
            print("error: read-back mismatch in %s" % output_path,
                  file=sys.stderr)
            return 1
    except OSError as exc:
        print("error: could not write %s: %s" % (output_path, exc),
              file=sys.stderr)
        return 1

    print("wrote %d characters to %s" % (len(ENTRY), output_path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
