"""
CP1404/CP5632 - Practical
Program to calculate and display cumulative incomes
"""

def main():
    """Get monthly incomes and display income report."""
    number_of_months = int(input("How many months? "))

    incomes = []
    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_income_report(incomes)

def print_income_report(incomes):
    """Print a nicely formatted income report with cumulative totals."""
    print("\nIncome Report")
    print("-------------")

    total = 0
    for month, income in enumerate(incomes, 1):
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f}    Total: ${total:10.2f}")

main()
