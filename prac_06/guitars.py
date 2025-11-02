"""
guitars.py - CP1404 prac_06
Collect Guitar objects from user, then display nicely.
Estimate: 10 minutes
Actual: <record after you finish>
"""
from prac_06.guitar import Guitar  # or: from guitar import Guitar


def main():
    print("My guitars!")
    guitars: list[Guitar] = []

    # --- For quick testing, comment user input and use pre-filled data:
    # guitars.append(Guitar("Fender Stratocaster", 2014, 765.40))
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    # Input loop
    name = input("Name: ").strip()
    while name:
        year = int(input("Year: ").strip())
        cost = float(input("Cost: $").strip())
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")
        name = input("Name: ").strip()

    # Output
    if guitars:
        print("\nThese are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = " (vintage)" if guitar.is_vintage() else ""
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), "
                  f"worth ${guitar.cost:10,.2f}{vintage_string}")
    else:
        print("No guitars (boo!)")


if __name__ == "__main__":
    main()
