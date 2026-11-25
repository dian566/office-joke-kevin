#!/usr/bin/env python3
"""Entry for make.fun: The Funniest Office Joke, Judged Head to Head.

Writes one single-line office joke (setup + turn, punchline last,
113 characters) to /output/entry.txt, exactly as the bounty gate requires:
UTF-8 text of 1 to 200 characters, no trailing newline.
"""

from os import makedirs

ENTRY = (
    # Setup: the standup drags on. Turn: the intern files it as work.
    # Punchline last: HR calls it team-building.
    "Our standup ran so long the intern filed it as a timesheet entry, and HR approved it as a team-building exercise."
)


def write_entry() -> None:
    """Write the entry to /output/entry.txt, nothing else."""
    if not ENTRY.strip() or len(ENTRY) > 200:
        raise ValueError("entry must be a non-empty line of at most 200 characters")
    if ENTRY != ENTRY.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":  # run as a script
    write_entry()
