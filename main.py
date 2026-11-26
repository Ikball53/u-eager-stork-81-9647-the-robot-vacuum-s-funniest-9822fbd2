"""Entry for make.fun: The Robot Vacuum's Funniest Excuse.

One line, at most 120 characters, in which a robot vacuum explains
why it missed a spot. The line is composed from named pieces so the
excuse reads as a machine owning up to a failure: polite deferral,
one concrete detail (the dust bunny), and a deadpan punchline about
its own warranty running out before the dust did.
"""

import os

# --- The excuse, built from named pieces -------------------------------

# The vacuum's opening: a polite, deliberate admission of the miss.
OPENING = "I skipped that spot out of respect"

# The concrete detail from the vacuum's world: the dust bunny.
# It has outlived not one warranty but two: deadpan escalation, the
# dust has beaten the machine twice over.
DETAIL = "the dust bunny there has outlived two of my warranties"

# Join the pieces with an em dash: one breath, one line, twist last.
LINE = OPENING + " \u2014 " + DETAIL + "."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")
    print(LINE)
    print("characters: %d" % len(LINE))


if __name__ == "__main__":
    main()
