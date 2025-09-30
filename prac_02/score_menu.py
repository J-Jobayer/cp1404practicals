"""
CP1401/CP1404 - Practical
Menu-driven program for score operations
"""

def main():
    score = get_valid_score()  # Always start with a valid score
    choice = display_menu()

    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_result(score)
            print(f"Result: {result}")
        elif choice == "S":
            print("*" * score)
        else:
            print("Invalid choice, please try again.")

        choice = display_menu()

    print("Farewell! Thanks for using the program.")


def display_menu():
    """Display menu and return user's choice in uppercase."""
    print("\nMenu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")
    return input(">>> ").upper()


def get_valid_score():
    """Get a valid score between 0 and 100 inclusive."""
    score = int(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score. Must be between 0 and 100.")
        score = int(input("Enter score (0-100): "))
    return score


def determine_result(score):
    """Determine the result based on the score."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


# Run the program
if __name__ == "__main__":
    main()
