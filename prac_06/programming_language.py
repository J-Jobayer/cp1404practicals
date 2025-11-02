"""
programming_language.py - CP1404 prac_06
Estimate: 10 minutes
Actual: <record after you finish>
"""

class ProgrammingLanguage:
    """Represent a programming language with typing discipline, reflection support, and first-year."""

    def __init__(self, name: str, typing: str, reflection: bool, year: int) -> None:
        self.name = name
        self.typing = typing
        self.reflection = bool(reflection)
        self.year = int(year)

    def is_dynamic(self) -> bool:
        """Return True if the language uses dynamic typing."""
        return self.typing.strip().lower() == "dynamic"

    def __str__(self) -> str:
        """Return a nicely formatted string."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

