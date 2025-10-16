"""
CP1404/CP5632 Practical - Complete Solution
State names in a dictionary
File has been reformatted and state inputs can be any case.
Also prints all states and names neatly.
"""

CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia"
}

# Print all the states and names neatly
for code, name in CODE_TO_NAME.items():
    print(f"{code:3} is {name}")

# Ask for user input (any case)
state = input("\nEnter short state: ").upper()
while state != "":
    try:
        print(f"{state} is {CODE_TO_NAME[state]}")
    except KeyError:
        print("Invalid short state")
    state = input("Enter short state: ").upper()
