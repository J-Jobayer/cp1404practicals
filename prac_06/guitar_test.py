"""
guitar_test.py - CP1404 prac_06
Manual tests for Guitar.get_age() and Guitar.is_vintage().
Estimate: 5 minutes
Actual: <record after you finish>
"""
from prac_06.guitar import Guitar  # or: from guitar import Guitar

def main():
    # Use a fixed year so expected values match the prac text examples.
    test_year = 2022

    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another = Guitar("Another Guitar", 2013, 0)

    print(f"{gibson.name} get_age() - Expected 100. Got {gibson.get_age(test_year)}")
    print(f"{another.name} get_age() - Expected 9. Got {another.get_age(test_year)}")
    print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage(test_year)}")
    print(f"{another.name} is_vintage() - Expected False. Got {another.is_vintage(test_year)}")


if __name__ == "__main__":
    main()
