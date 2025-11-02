"""
car.py - CP1404 prac_06
Estimate: 10 minutes
Actual: <record after you finish>
"""

class Car:
    """Represent a car object."""

    def __init__(self, name: str = "Car", fuel: int | float = 0) -> None:
        """Initialise a Car with a name, fuel amount and odometer starting at 0."""
        self.name = name
        # Store fuel as a non-negative number
        self.fuel = max(0, int(fuel))
        self.odometer = 0

    def add_fuel(self, amount: int | float) -> None:
        """Add fuel to the car; ignore negative amounts."""
        if amount > 0:
            self.fuel += int(amount)

    def drive(self, distance: int | float) -> int:
        """
        Drive the car a given distance.
        Will drive until fuel runs out; returns the actual distance driven.
        Fuel consumption is 1 unit of fuel per 1 km driven (classic CP1404 Car).
        """
        distance = int(max(0, distance))
        # Can only drive up to available fuel
        distance_driven = min(distance, self.fuel)
        self.odometer += distance_driven
        self.fuel -= distance_driven
        return distance_driven

    def __str__(self) -> str:
        """Return a string like: 'Limo, fuel=105, odometer=115'."""
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}"
