from __future__ import annotations
from dataclasses import dataclass
from datetime import date

CURRENT_YEAR = date.today().year

@dataclass(order=False)
class Guitar:
    """Represent a Guitar with name, year, and cost."""
    name: str
    year: int
    cost: float

    def age(self) -> int:
        """Return the guitar's age in years."""
        return CURRENT_YEAR - self.year

    def is_vintage(self) -> bool:
        """Return True if the guitar is 50+ years old."""
        return self.age() >= 50

    def __lt__(self, other: "Guitar") -> bool:
        """Order guitars by year (older first)."""
        return self.year < other.year

    def __str__(self) -> str:
        vintage_text = " (vintage)" if self.is_vintage() else ""
        return f"{self.name:>20} ({self.year}), worth ${self.cost:10,.2f}{vintage_text}"
