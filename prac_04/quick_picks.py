"""
CP1404/CP5632 - Practical
Quick Pick Lottery Ticket Generator
"""

import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6

number_of_picks = int(input("How many quick picks? "))

for _ in range(number_of_picks):
    quick_pick = []
    while len(quick_pick) < NUMBERS_PER_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in quick_pick:
            quick_pick.append(number)
    quick_pick.sort()
    # Display numbers formatted neatly (width=2)
    print(" ".join(f"{number:2}" for number in quick_pick))
