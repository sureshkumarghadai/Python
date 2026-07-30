# Program Name: Simple Calculator
# Author: Suresh Ghadai
# Version: 1.0

"""
Asks the user to enter two numbers
and a mathematical operator (+, -, *, /),
then performs the calculation and prints the result.
"""

# Step 1: Ask the user for input values
num1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

# Step 2: Perform the calculation based on the operator
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero is not allowed"
else:
    result = "Error: Invalid operator entered"

# Step 3: Display the result
print(f"Result: {num1} {operator} {num2} = {result}")
