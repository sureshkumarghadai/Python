"""
Employee Salary Calculator
---------------------------
Calculates an employee's total salary (Basic Salary + Bonus) and
determines whether the employee qualifies as a "High Earner"
(Total Salary >= 100000).
"""

# Predefined threshold for High Earner classification
HIGH_EARNER = 100000


def get_employee_details():
    """Accepts and returns employee name, basic salary, and bonus from the user."""
    name = input("Enter Employee Name: ").strip()

    # Loop until a valid numeric value is entered for basic salary
    while True:
        try:
            basic_salary = float(input("Enter Basic Salary: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for Basic Salary.")

    # Loop until a valid numeric value is entered for bonus
    while True:
        try:
            bonus = float(input("Enter Bonus: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for Bonus.")

    return name, basic_salary, bonus


def calculate_total_salary(basic_salary, bonus):
    """Returns the total salary given basic salary and bonus."""
    return basic_salary + bonus


def is_high_earner(total_salary, threshold=HIGH_EARNER):
    """Returns True if total_salary meets or exceeds the threshold, else False."""
    return total_salary >= threshold


def display_summary(name, basic_salary, bonus, total_salary, high_earner):
    """Prints a formatted summary of the employee's salary details."""
    print("\n----- Employee Summary -----\n")
    print(f"Employee Name : {name}")
    print(f"Basic Salary  : {basic_salary:.2f}")
    print(f"Bonus         : {bonus:.2f}")
    print(f"Total Salary  : {total_salary:.2f}")
    print(f"High Earner   : {high_earner}")


def main():
    name, basic_salary, bonus = get_employee_details()
    total_salary = calculate_total_salary(basic_salary, bonus)
    high_earner = is_high_earner(total_salary)
    display_summary(name, basic_salary, bonus, total_salary, high_earner)


if __name__ == "__main__":
    main()
