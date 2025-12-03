"""
UnreliableCar class - Car that may not move when you try to drive it.
"""

from random import uniform
from car import Car


class UnreliableCar(Car):
    """Car that sometimes does not drive when asked, depending on reliability."""

    def __init__(self, name: str, fuel: float, reliability: float) -> None:
        """
        Initialise an UnreliableCar.

        reliability: float between 0 and 100, representing percentage chance
        that drive will succeed.
        """
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance: float) -> float:
        """
        Attempt to drive the car.

        Generates a random number between 0 and 100.
        If this number is less than reliability, drive as normal.
        Otherwise, drive 0 km.
        Returns the distance actually driven.
        """
        random_chance = uniform(0, 100)
        if random_chance < self.reliability:
            # Car behaves like a normal Car
            return super().drive(distance)
        # Car fails to drive
        return 0
