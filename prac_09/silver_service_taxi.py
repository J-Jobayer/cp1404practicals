"""
SilverServiceTaxi class - fancier Taxi with higher price and flagfall.
"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """A more expensive taxi that includes a fanciness factor and flagfall."""
    flagfall = 4.50

    def __init__(self, name: str, fuel: float, fanciness: float) -> None:
        """
        Initialise a SilverServiceTaxi.

        fanciness scales the price_per_km for this taxi.
        """
        super().__init__(name, fuel)
        self.fanciness = fanciness
        # Start from the base Taxi price_per_km and scale it for this instance
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self) -> str:
        """Return string representation including flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self) -> float:
        """
        Return the price for the taxi trip including flagfall.

        Uses Taxi's get_fare (with rounding) then adds flagfall.
        """
        return super().get_fare() + self.flagfall
