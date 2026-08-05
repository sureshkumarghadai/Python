employees = {
    101: 50000,
    102: 60000,
    103: 70000
}

while True:

    print("\n========================")
    print("PAYROLL PROCESSING")
    print("========================")

    print("1. View Salary")
    print("2. Read Payroll File")
    print("3. Exit")

    choice = input("Enter Choice: ")

    try:

        if choice == "1":

            emp_id = int(
                input(
                    "Employee ID: "
                )
            )

            if emp_id not in employees:

                raise ValueError(
                    "Employee Not Found"
                )

            print(
                "Salary:",
                employees[emp_id]
            )

        elif choice == "2":

            file = open(
                "payroll.txt",
                "r"
            )

            print(file.read())

            file.close()

        elif choice == "3":

            print(
                "System Closed"
            )

            break

        else:

            raise ValueError(
                "Invalid Menu Option"
            )

    except ValueError as error:

        print(
            "ValueError:",
            error
        )

    except FileNotFoundError:

        print(
            "Payroll File Missing"
        )

    except TypeError:

        print(
            "Data Type Error"
        )

    except IndexError:

        print(
            "Index Error"
        )

    finally:

        print(
            "\nOperation Completed"
        )
 