"""
Tests for SilverServiceTaxi class.
"""

from silver_service_taxi import SilverServiceTaxi


def main() -> None:
    """Test SilverServiceTaxi calculations."""
    hummer = SilverServiceTaxi("Hummer", 200, fanciness=2)
    hummer.start_fare()
    hummer.drive(18)
    fare = hummer.get_fare()
    print(hummer)
    print(f"Fare for 18km trip: ${fare:.2f}")

    # After rounding to nearest 10c in Taxi.get_fare, expected is $48.80
    expected_fare = 48.80
    # Allow tiny float tolerance
    assert abs(fare - expected_fare) < 0.01, f"Expected {expected_fare}, got {fare}"


if __name__ == "__main__":
    main()
