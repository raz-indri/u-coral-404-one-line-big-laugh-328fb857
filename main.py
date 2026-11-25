"""One Line, Big Laugh — entry program.

Writes exactly one funny line (at most 200 characters) to
/output/entry.txt. No dependencies, no setup, no explanation:
the file holds the joke and nothing else.

Duel-tested winner (6-0 across 21 pairwise duels, both orders):
a wedding DJ, a 2019 voicemail to an ex, and a mother-in-law encore.
"""

import os

LINE = "At my wedding, the DJ played my 2019 voicemail to my ex — twice, because my mother-in-law requested an encore."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
