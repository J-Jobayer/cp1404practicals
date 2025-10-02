"""
CP1404/CP5632 - Practical
capitalist_conrad.py: Stock price simulator.
"""

import random

MAX_INCREASE = 0.1   # 10%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.0
MAX_PRICE = 1000.0
INITIAL_PRICE = 10.0

OUTPUT_FILE = "conrad_output.txt"

def main():
    price = INITIAL_PRICE
    day = 0
    out_file = open(OUTPUT_FILE, 'w')

    print(f"Starting price: ${price:,.2f}")
    print(f"Starting price: ${price:,.2f}", file=out_file)

    while MIN_PRICE <= price <= MAX_PRICE:
        day += 1
        if random.randint(1, 2) == 1:
            price_change = random.uniform(0, MAX_INCREASE)
        else:
            price_change = random.uniform(-MAX_DECREASE, 0)
        price *= (1 + price_change)
        print(f"On day {day} price is: ${price:,.2f}")
        print(f"On day {day} price is: ${price:,.2f}", file=out_file)

    out_file.close()

if __name__ == "__main__":
    main()
