#!/usr/bin/env python3
"""make.fun entry: The Router Confesses (router-confess-b).

The entry is one line in which a home Wi-Fi router excuses itself
for dying at the climax of a movie. The gag gives the router a
guilty conscience: it saw the twist coming, panicked, and unplugged
itself before the villain could get to it. The program checks the
line against the competition gate (RULES.txt: /output/entry.txt
must be UTF-8 text of 1 to 200 characters, not only whitespace, a
single line) and writes it to /output/entry.txt.
"""

from pathlib import Path

OUT_PATH = Path("/output/entry.txt")
CHAR_LIMIT = 200


def build_entry():
    """Return the confession line, my own wording throughout."""
    # The turn is the router as a cowardly moviegoer. It is not
    # broken, it is scared, and it chose to faint rather than watch
    # the villain. Blaming the plot twist makes an outage feel
    # personal instead of technical.
    return (
        "Sorry the Wi-Fi died right at the climax - I saw the plot "
        "twist coming, panicked, and unplugged myself before the "
        "villain could."
    )


def validate(line):
    """Raise SystemExit listing every gate problem, if there is one."""
    problems = []
    if not line.strip():
        problems.append("empty")
    if line != line.strip():
        problems.append("leading/trailing whitespace")
    if len(line) > CHAR_LIMIT:
        problems.append("too long: %d chars" % len(line))
    if "\n" in line:
        problems.append("not a single line")
    if problems:
        raise SystemExit("gate failed: " + "; ".join(problems))


def main():
    line = build_entry()
    validate(line)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(line, encoding="utf-8")
    saved = OUT_PATH.read_text(encoding="utf-8")
    print("Wrote %s (%d chars, %d chars of headroom)"
          % (OUT_PATH, len(saved), CHAR_LIMIT - len(saved)))
    print(saved)


if __name__ == "__main__":
    main()
