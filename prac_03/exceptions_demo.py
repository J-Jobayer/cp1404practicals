"""
CP1404/CP5632 - Practical
exceptions_demo.py
"""

# Q1. When will a ValueError occur?
# → A ValueError occurs if the user enters something that cannot be converted to an integer,
#   e.g., letters or symbols instead of digits.

# Q2. When will a ZeroDivisionError occur?
# → A ZeroDivisionError occurs if the denominator entered is 0 (division by zero is undefined).

# Q3. Could you change the code to avoid the possibility of a ZeroDivisionError?
# → Yes. You can check if the denominator is zero before performing the division
#   and keep asking until a non-zero value is entered.

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
