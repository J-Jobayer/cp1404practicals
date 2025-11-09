class ProgrammingLanguage:
    """Represent a programming language with typing, reflection, year and pointer arithmetic."""

    def __init__(self, name: str, typing: str, reflection: bool, year: int, pointer_arithmetic: bool):
        """
        Create a ProgrammingLanguage.

        :param name: Language name (e.g., "Python")
        :param typing: Typing discipline, usually "Dynamic" or "Static"
        :param reflection: True if the language supports reflection
        :param year: First appearance year
        :param pointer_arithmetic: True if the language supports pointer arithmetic
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    def is_dynamic(self) -> bool:
        """Return True if the language uses dynamic typing."""
        return self.typing.strip().lower() == "dynamic"

    def __str__(self) -> str:
        """Return a human-readable string for this language."""
        return (f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, "
                f"PointerArithmetic={self.pointer_arithmetic}, First appeared in {self.year}")
