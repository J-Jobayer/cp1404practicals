"""
Band class for association example - Band has Musicians.
"""

from typing import List
from musician import Musician


class Band:
    """Band that contains a collection of Musicians."""

    def __init__(self, name: str) -> None:
        """Initialise Band with a name and empty list of musicians."""
        self.name = name
        self.musicians: List[Musician] = []

    def __str__(self) -> str:
        """Return string representation of Band and its Musicians."""
        musicians_text = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musicians_text})"

    def add(self, musician: Musician) -> None:
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self) -> None:
        """Tell each musician in the band to play."""
        for musician in self.musicians:
            musician.play()
