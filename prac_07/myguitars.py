# myguitars.py
# Main program for the "More Guitars" exercise.
# Files expected in same folder:
#   - guitar.py (defines class Guitar with name, year, cost; __str__ recommended)
#   - guitars.csv (no header; rows: Name,Year,Cost)

from pathlib import Path
from guitar import Guitar

FILENAME = "guitars.csv"
SEED_ROWS = [
    "Fender Stratocaster,2014,765.4",
    "Gibson L-5 CES,1922,16035.4",
    "Line 6 JTV-59,2010,1512.9",
]


def main():
    guitars = load_guitars(FILENAME)
    if guitars:
        print(f"Loaded {len(guitars)} guitars from {FILENAME}.\n")
        print("Guitars (original order):")
        display_guitars(guitars)
    else:
        print(f"No guitars found in {FILENAME}. Seeding example data...")
        save_raw_lines(FILENAME, SEED_ROWS)
        guitars = load_guitars(FILENAME)
        print("Seeded and reloaded.\n")

    # Sort by year safely (does NOT require __lt__ on Guitar)
    guitars.sort(key=lambda g: g.year)
    print("\nGuitars (sorted by year, oldest → newest):")
    display_guitars(guitars)

    # Add new guitars
    new_guitars = prompt_new_guitars()
    if new_guitars:
        guitars.extend(new_guitars)
        guitars.sort(key=lambda g: g.year)
        save_guitars(FILENAME, guitars)
        print(f"\nSaved {len(guitars)} total guitars to {FILENAME}.")
    else:
        print("\nNo new guitars added. File unchanged.")


def load_guitars(filename):
    """Read guitars from CSV: name,year,cost (no header). Return list of Guitar."""
    path = Path(filename)
    if not path.exists():
        return []

    guitars = []
    with path.open("r", encoding="utf-8") as in_file:
        for raw in in_file:
            line = raw.strip()
            if not line:
                continue
            try:
                name, year, cost = [p.strip() for p in line.split(",", maxsplit=2)]
                guitars.append(Guitar(name, int(year), float(cost)))
            except Exception:
                # Skip malformed lines gracefully
                print(f"(Skipping malformed line: {line!r})")
    return guitars


def display_guitars(guitars):
    if not guitars:
        print("(none)")
        return
    for i, g in enumerate(guitars, start=1):
        print(f"Guitar {i}: {g}")


def prompt_new_guitars():
    print("\nAdd new guitars (leave Name blank to finish):")
    added = []
    while True:
        name = input("Name: ").strip()
        if name == "":
            break
        year = prompt_int("Year: ")
        cost = prompt_float("Cost: $")
        added.append(Guitar(name, year, cost))
    if added:
        print(f"Added {len(added)} new guitar(s).")
    return added


def prompt_int(prompt_text):
    while True:
        try:
            return int(input(prompt_text))
        except ValueError:
            print("Invalid integer. Please try again.")


def prompt_float(prompt_text):
    while True:
        try:
            return float(input(prompt_text))
        except ValueError:
            print("Invalid number. Please try again.")


def save_guitars(filename, guitars):
    with open(filename, "w", encoding="utf-8") as out_file:
        for g in guitars:
            print(f"{g.name},{g.year},{g.cost}", file=out_file)


def save_raw_lines(filename, lines):
    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
