"""
CP1404/CP5632 - Practical
List comprehensions
"""

# Example data
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Example list comprehension: squares of numbers
squares = [number ** 2 for number in numbers]
print("Squares:", squares)

# TODO: Use a list comprehension to create a new list of even numbers
evens = [number for number in numbers if number % 2 == 0]
print("Even numbers:", evens)

# TODO: Use a list comprehension to create a list of numbers greater than 5
greater_than_five = [number for number in numbers if number > 5]
print("Numbers greater than 5:", greater_than_five)

# TODO: Use a list comprehension to create a list of even numbers squared
even_squares = [number ** 2 for number in numbers if number % 2 == 0]
print("Squares of even numbers:", even_squares)
