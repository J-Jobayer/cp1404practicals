"""
guitar.py - CP1404 prac_06
Estimate: 10 minutes
Actual: <record after finish>
"""
from datetime import date


class Guitar:
    """Represent a guitar with name, year and cost."""

    def __init__(self, name: str = "", year: int = 0, cost: float = 0.0) -> None:
        self.name = name
        self.year = int(year)
        self.cost = float(cost)

    def __str__(self) -> str:
        """Return e.g. 'Gibson L-5 CES (1922) : $16,035.40'."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self, current_year: int | None = None) -> int:
        """Return how old the guitar is in years."""
        current_year = current_year if current_year is not None else date.today().year
        return current_year - self.year

    def is_vintage(self, current_year: int | None = None) -> bool:
        """Return True if the guitar is 50 or more years old."""
        return self.get_age(current_year) >= 50
