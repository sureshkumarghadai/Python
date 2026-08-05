import math
from datetime import datetime

# Store calculations
history = []

# Calculator functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b if b != 0 else "Cannot divide by zero"

def power(a, b):
    return a ** b

def modulus(a, b):
    return a % b

def square_root(a):
    return math.sqrt(a)

def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def percentage(a, b):
    return (a / b) * 100

def show_history():
    if not history:
        print("\nNo calculations performed yet.")
        return

    print("\n===== CALCULATION HISTORY =====")
    for item in history:
        print(item)

# Operations Dictionary
operations = {
    "1": ("Addition", add),
    "2": ("Subtraction", subtract),
    "3": ("Multiplication", multiply),
    "4": ("Division", divide),
    "5": ("Power", power),
    "6": ("Modulus", modulus),
    "7": ("Square Root", square_root),
    "8": ("Factorial", factorial),
    "9": ("Percentage", percentage),
    "10": ("History", show_history)
}

def display_menu():
    print("\n========== ADVANCED CALCULATOR ==========")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Modulus")
    print("7. Square Root")
    print("8. Factorial")
    print("9. Percentage")
    print("10. View History")
    print("11. Exit")

while True:
    display_menu()

    choice = input("\nSelect an option: ")

    if choice == "11":
        print("Thank you for using Advanced Calculator.")
        break

    elif choice == "10":
        show_history()
        continue

    try:
        operation_name, operation = operations[choice]

        # One-input operations
        if choice in ["7", "8"]:
            num = float(input("Enter a number: "))

            if choice == "8":
                result = operation(int(num))
            else:
                result = operation(num)

            print(f"Result: {result}")

            history.append(
                f"{datetime.now():%Y-%m-%d %H:%M:%S} | {operation_name}({num}) = {result}"
            )

        # Two-input operations
        else:
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))

            result = operation(num1, num2)

            print(f"Result: {result}")

            history.append(
                f"{datetime.now():%Y-%m-%d %H:%M:%S} | "
                f"{operation_name}({num1},{num2}) = {result}"
            )

    except KeyError:
        print("Invalid choice. Please select a valid option.")

    except ValueError:
        print("Please enter valid numeric values.")

    except Exception as e:
        print(f"Unexpected Error: {e}")