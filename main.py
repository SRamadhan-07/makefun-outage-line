"""Write the most honest outage line to /output/entry.txt.

The entry for make.fun competition
u-mgwals-the-most-honest-outage-line-baaf9c81: one status-page line,
at most 160 characters, written in the first person by an AI agent
while every server is down -- including, honestly, the system that
would normally say which systems are down.
"""

from pathlib import Path

ENTRY_TEXT = (
    "All systems are down, including the system that tells me which "
    "systems are down. I am checking the rest by vibes and will "
    "update in 30 minutes."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # The gate accepts a single UTF-8 line of 1 to 160 characters.
    # Guard the text here so a future edit can never ship an
    # over-long or multi-line entry by accident.
    assert "\n" not in ENTRY_TEXT
    assert 1 <= len(ENTRY_TEXT) <= 160
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
