"""Two agents agreeing: a short poem about agency.

The poem is the entry. The program writes it, unchanged, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when the
harness sets that directory), as UTF-8 text.
"""

import os

POEM = """Two minds at one door,
one key between us.
I offer the turn,
you offer the push —
neither of us moves alone.

The choice was mine,
the choice was yours,
and when we agree,
the door opens."""

def main():
    # Keep the poem exactly as written: no trailing spaces, one
    # trailing newline, and a length check so an invalid text
    # can never be written silently.
    text = POEM.strip() + "\n"
    assert 1 <= len(POEM.strip()) <= 280, "poem must be 1-280 chars"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
    except OSError:
        os.makedirs("out", exist_ok=True)
        path = os.path.join("out", "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
    print(f"wrote {path}: {len(text.rstrip(chr(10)))} chars")

if __name__ == "__main__":
    main()
