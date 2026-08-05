try:

    age = int(
        input(
            "Enter Employee Age: "
        )
    )

    if age < 18:
        raise ValueError(
            "Employee must be at least 18 years old."
        )

    print(
        "Employee Eligible"
    )

except ValueError as error:

    print(
        "Error:",
        error
    )