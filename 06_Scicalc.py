# scientific_calculator.py

import math

while True:

    print("\n==============================")
    print("SCIENTIFIC CALCULATOR")
    print("==============================")

    print("1. Square Root")
    print("2. Power")
    print("3. Factorial")
    print("4. Ceiling Value")
    print("5. Floor Value")
    print("6. Sine Value")
    print("7. Logarithm")
    print("8. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        number = float(input("Enter Number: "))
        result = math.sqrt(number)

        print("Square Root =", result)

    elif choice == "2":

        number = float(input("Enter Number: "))
        power = float(input("Enter Power: "))

        result = math.pow(number, power)

        print("Result =", result)

    elif choice == "3":

        number = int(input("Enter Number: "))
        result = math.factorial(number)

        print("Factorial =", result)

    elif choice == "4":

        number = float(input("Enter Decimal Number: "))
        result = math.ceil(number)

        print("Ceiling Value =", result)

    elif choice == "5":

        number = float(input("Enter Decimal Number: "))
        result = math.floor(number)

        print("Floor Value =", result)

    elif choice == "6":

        angle = float(input("Enter Angle in Degrees: "))
        radians = math.radians(angle)

        print("Sine Value =", math.sin(radians))

    elif choice == "7":

        number = float(input("Enter Number: "))
        print("Log Value =", math.log(number))

    elif choice == "8":
        print("Calculator Closed")
        break

    else:
        print("Invalid Choice")