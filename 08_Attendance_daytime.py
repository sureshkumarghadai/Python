# attendance_system.py

from datetime import datetime

while True:

    print("\n=========================")
    print("EMPLOYEE ATTENDANCE SYSTEM")
    print("=========================")

    print("1. Current Date")
    print("2. Current Time")
    print("3. Current DateTime")
    print("4. Mark Attendance")
    print("5. Calculate Days")
    print("6. Age Calculator")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        today = datetime.now()

        print("Date =", today.date())

    elif choice == "2":

        now = datetime.now()

        print("Time =", now.time())

    elif choice == "3":

        now = datetime.now()

        print("Date and Time =", now)

    elif choice == "4":

        employee = input("Employee Name: ")

        login_time = datetime.now()

        print(employee, "Login Time")
        print(login_time)

    elif choice == "5":

        start_date = input(
            "Enter Start Date (YYYY-MM-DD): "
        )

        end_date = input(
            "Enter End Date (YYYY-MM-DD): "
        )

        d1 = datetime.strptime(
            start_date,
            "%Y-%m-%d"
        )

        d2 = datetime.strptime(
            end_date,
            "%Y-%m-%d"
        )

        difference = d2 - d1

        print("Days =", difference.days)

    elif choice == "6":

        birth_date = input(
            "Enter Birth Date (YYYY-MM-DD): "
        )

        dob = datetime.strptime(
            birth_date,
            "%Y-%m-%d"
        )

        today = datetime.now()

        age = today.year - dob.year

        print("Age =", age)

    elif choice == "7":

        print("Application Closed")
        break

    else:
        print("Invalid Choice")
 