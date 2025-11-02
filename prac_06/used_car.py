"""
used_cars.py - CP1404 prac_06
Estimate: 8 minutes
Actual: <record after finish>

Walkthrough steps implemented:
- Create a new Car("Limo", 100)
- Add 20 fuel via add_fuel
- Print the fuel amount
- Attempt to drive 115 km
- Print the car object to confirm __str__ and name field
"""

# If running from project root with a 'prac_06' package:
from prac_06.car import Car
# If running this file from inside the same folder as car.py, use:
# from car import Car

def main():
    # Initial cars (add names as literals)
    camry = new_car("Camry", 50)
    civic = new_car("Civic", 30)

    # --- Walkthrough: Limo ---
    limo = new_car("Limo", 100)     # Create a new Car with 100 fuel
    limo.add_fuel(20)               # Add 20 more fuel
    print(f"Limo fuel after top-up: {limo.fuel}")  # Print the amount of fuel

    driven = limo.drive(115)        # Attempt to drive 115 km
    print(f"Limo actually drove: {driven} km")

    # Print objects to verify __str__ and names
    print(limo)
    print(camry)
    print(civic)

def new_car(name: str, fuel: int) -> Car:
    """Helper to create a named car with initial fuel."""
    return Car(name=name, fuel=fuel)

if __name__ == "__main__":
    main()
