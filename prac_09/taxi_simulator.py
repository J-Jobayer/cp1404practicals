"""
Menu-driven taxi simulator using Taxi and SilverServiceTaxi.
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


MENU = "q)uit, c)hoose taxi, d)rive"


def main() -> None:
    """Run the taxi simulator program."""
    print("Let's drive!")
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4),
    ]
    current_taxi = None
    bill_to_date = 0.0

    while True:
        print(MENU)
        choice = input(">>> ").lower().strip()

        if choice == "q":
            break
        elif choice == "c":
            current_taxi = choose_taxi(taxis)
        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                bill_to_date += drive_taxi(current_taxi)
        else:
            print("Invalid option")

        print(f"Bill to date: ${bill_to_date:.2f}")

    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis) -> None:
    """Display the list of taxis with their index numbers."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    """Handle taxi selection and return the chosen taxi (or None if invalid)."""
    print("Taxis available:")
    display_taxis(taxis)
    try:
        choice = int(input("Choose taxi: "))
        if 0 <= choice < len(taxis):
            return taxis[choice]
        print("Invalid taxi choice")
        return None
    except ValueError:
        print("Invalid input (please enter a number)")
        return None


def drive_taxi(taxi) -> float:
    """Drive the given taxi and return the cost of the trip."""
    try:
        distance = float(input("Drive how far? "))
    except ValueError:
        print("Invalid distance")
        return 0.0

    taxi.start_fare()
    taxi.drive(distance)
    trip_cost = taxi.get_fare()
    print(f"Your {taxi.name} trip cost you ${trip_cost:.2f}")
    return trip_cost


if __name__ == "__main__":
    main()
