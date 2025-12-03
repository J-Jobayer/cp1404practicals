"""
CP1404/CP5632 Practical - Testing demo and functions.

This module demonstrates:
1) assert based tests
2) doctest tests
3) simple functions to debug/fix: repeat_string, is_long_word, format_as_sentence
"""

from __future__ import annotations
import doctest

from car import Car  # uses your existing Car class from earlier pracs


def repeat_string(s: str, n: int) -> str:
    """
    Return string s repeated n times.

    >>> repeat_string("hi", 1)
    'hi'
    >>> repeat_string("hi", 3)
    'hihihi'
    >>> repeat_string("", 5)
    ''
    >>> repeat_string("a", 0)
    ''
    """
    # Correct, simple implementation using string multiplication
    return s * max(0, n)


def is_long_word(word: str, length: int = 5) -> bool:
    """
    Determine if the word is as long as or longer than the given length.

    >>> is_long_word("hello")
    True
    >>> is_long_word("hi")
    False
    >>> is_long_word("Python", 6)
    True
    >>> is_long_word("py", 2)
    True
    """
    return len(word) >= length


def format_as_sentence(phrase: str) -> str:
    """
    Format a phrase as a sentence: first letter capital, single full stop at end.

    Rules:
    - Strip leading/trailing spaces
    - Capitalise the first character
    - Ensure there is exactly one '.' at the end (no '..' or '...')
    - Keep the rest of the phrase unchanged except for first letter

    >>> format_as_sentence("hello")
    'Hello.'
    >>> format_as_sentence("hello.")
    'Hello.'
    >>> format_as_sentence("hello world")
    'Hello world.'
    >>> format_as_sentence("   already capitalised   ")
    'Already capitalised.'
    >>> format_as_sentence("MULTIPLE. full stops...")
    'Multiple. full stops.'
    """
    phrase = phrase.strip()
    if not phrase:
        return ""

    # Capitalise first character only, keep rest as-is
    phrase = phrase[0].upper() + phrase[1:]

    # Remove existing full stops at the end, then add exactly one
    while phrase.endswith("."):
        phrase = phrase[:-1]
    return phrase + "."


def run_tests() -> None:
    """Run simple assert-based tests."""
    # Tests for repeat_string
    assert repeat_string("hi", 2) == "hihi"
    assert repeat_string("x", 5) == "xxxxx"
    assert repeat_string("a", 0) == ""

    # Tests for is_long_word
    assert is_long_word("hello") is True
    assert is_long_word("hi") is False
    assert is_long_word("python", 3) is True

    # Tests for format_as_sentence
    assert format_as_sentence("hello") == "Hello."
    assert format_as_sentence("Hello.") == "Hello."
    assert format_as_sentence("  test  ") == "Test."

    # At least two asserts to show Car sets fuel correctly
    # Using your existing Car class from car.py
    default_car = Car()
    assert default_car.fuel == 0, "Default car fuel should be 0"

    car_with_fuel = Car("Test", 50)
    assert car_with_fuel.fuel == 50, "Car should store initial fuel value"

    negative_fuel_car = Car("Bad Fuel", -10)
    assert negative_fuel_car.fuel == 0, "Fuel should not be negative"

    print("All assert tests passed!")


if __name__ == '__main__':
    run_tests()
    # Run doctests in this module
    doctest.runmod(verbose=True)
