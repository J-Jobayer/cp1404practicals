"""
CP1404/CP5632 - Practical
files.py: Simple file reading/writing tasks.
"""

def main():
    # Part 1: Get name and write to file
    name = input("Enter your name: ")
    with open("name.txt", "w", encoding="utf-8") as file:
        file.write(name)

    # Part 2: Read name back and greet
    with open("name.txt", "r", encoding="utf-8") as file:
        name_from_file = file.read().strip()
    print(f"Hi {name_from_file}!")

    # Part 3: Read first two numbers and print their sum
    with open("numbers.txt", "r", encoding="utf-8") as file:
        first_line = file.readline().strip()
        second_line = file.readline().strip()
    first_number = int(first_line)   # will raise if not an integer
    second_number = int(second_line) # will raise if not an integer
    print(first_number + second_number)

    # Part 4: Read all numbers (ignore blank lines) and print their sum
    total = 0
    with open("numbers.txt", "r", encoding="utf-8") as file:
        for line in file:
            s = line.strip()
            if s:  # skip empty lines
                total += int(s)  # will raise if a non-integer is present
    print(total)

if __name__ == "__main__":
    main()
