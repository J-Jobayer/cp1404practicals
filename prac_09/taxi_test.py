"""
Program to test the Taxi class.
"""

from taxi import Taxi


def main() -> None:
    """Test creating and using a Taxi."""
    my_taxi = Taxi("Prius 1", 100)

    # Drive 40 km
    my_taxi.start_fare()
    my_taxi.drive(40)
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")

    # Start a new fare and drive 100 km
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")


if __name__ == "__main__":
    main()
