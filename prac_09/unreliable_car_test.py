"""
Test the UnreliableCar class.
"""

from unreliable_car import UnreliableCar


def main() -> None:
    """Demonstrate behaviour of UnreliableCar."""
    # Very unreliable car
    dud_car = UnreliableCar("Dud", 100, reliability=20)
    # Very reliable car
    good_car = UnreliableCar("Good", 100, reliability=90)

    print("Testing unreliable car over multiple attempts...")
    total_dud_distance = 0
    total_good_distance = 0

    for _ in range(10):
        total_dud_distance += dud_car.drive(10)
        total_good_distance += good_car.drive(10)

    print(f"{dud_car.name} travelled {total_dud_distance}km out of 100km requested.")
    print(f"{good_car.name} travelled {total_good_distance}km out of 100km requested.")

    # Simple sanity assert: good_car should drive at least as far as dud_car
    assert total_good_distance >= total_dud_distance


if __name__ == "__main__":
    main()
