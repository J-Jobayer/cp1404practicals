"""
Taxi class - specialised version of Car that includes fare costs.
"""

from car import Car


class Taxi(Car):
    """Specialised version of a Car that includes fare costs."""
    price_per_km = 1.23  # class variable, shared default for all taxis

    def __init__(self, name: str, fuel: float) -> None:
        """Initialise a Taxi with name, fuel and tracking for current fare."""
        super().__init__(name, fuel)
        self.current_fare_distance = 0

    def __str__(self) -> str:
        """Return string representation of a Taxi."""
        return (f"{super().__str__()}, {self.current_fare_distance}km on current fare, "
                f"${self.price_per_km:.2f}/km")

    def get_fare(self) -> float:
        """
        Return the price for the taxi trip.

        Fare is price_per_km * distance, rounded to nearest 10c.
        """
        fare = self.price_per_km * self.current_fare_distance
        return round(fare, 1)

    def start_fare(self) -> None:
        """Begin a new fare by resetting the current fare distance."""
        self.current_fare_distance = 0

    def drive(self, distance: float) -> float:
        """
        Drive like a normal Car, but also add distance to current fare.

        Returns the actual distance driven.
        """
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven
