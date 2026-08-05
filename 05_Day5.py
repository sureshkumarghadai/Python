# Functions and Modules: Function and modules are fundamental building blocks in python that hekps organize, reuse, maintain code efficiently. Function enables the execution of specific tasks through reusable blocks of code, while modules allow the related functions, classes and variables to be grouped into separate files for better program structure and modularity.


#Functions: A function is named block of code designed to perform a specific task. Functions promote code reusability, reduce redundancy and simplyfy maintenance by allowing the same logic to be executed multiple times from different parts of a program.

# Functions support input throgh parameters, perform predefined operations, and may producte output through return values.

# Part of Function: 
    #Definition:  A function definition specifies the functions's name , the operation it performs, & any inputs it requires.
    #Parameters: Parameters are variable defined in a function declaration that reveive data when the function is invoked. They serve as placeholders for values that are passed into the function during execution.
    #Return Values:  A return values is the result produced by a function & sent back to the calling code after execution.
# Types of Arguments: Arguments are the actual values supplied to a function when it is called.
    # Positionl: Positional arguments are assigned to parameters based on the order in which they are provided.
    # Keyword: Keyword arguments explicitly associate a value with a parameter name during the function invocation.
    # Default: Default arguments are parameters that hav predefined values assigned during the function definition.
    # Variable-length: Variable-lenght arguments enabled functions to handle common scenarios automatically while still allowing customization when needed and allow the function to accept a flexible number of inputs.
# Lambda Function: A Lambda function is a small anomymous function created for short, simple operations that don't require a fomarl function definition.
# Scope: Scope refers to the region of a program where a variable or function or object can be accessed and used.
     # Local: A local scope exists within a function or block where the variable are created & used.
     # Global:A global scope contains variables, objects outside functions & accessible throughout the program.
# Global Variables:

# main.py

import payroll_module as pm

print("=================================")
print("Employee Payroll management")
print("=================================")

# Global Scope Function
pm.display_company()

# User Input

emp_id = int(input("\nEnter Employee ID: "))
name = input("Enter Employee Name: ")
department = input("Enter Department: ")

basic_salary = float(input("Enter Basic Salary: "))
hra = float(input("Enter HRA: "))
bonus = float(input("Enter Bonus: "))

# Positional Arguments
pm.employee_details(
    emp_id,
    name,
    department
)

# Function with Parameters and Return Value

gross_salary = pm.calculate_salary(
    basic_salary,
    hra,
    bonus
)

print("\nGross Salary =", gross_salary)

# Default Argument Demo

tax = pm.calculate_tax(gross_salary)

print("Tax (Default 10%) =", tax)

# Keyword Argument Demo

pm.employee_details(
    emp_id=emp_id,
    name=name,
    department=department
)

# Variable-Length Arguments Demo

num_allowances = int(
    input(
        "\nEnter Number of Extra Allowances: "
    )
)

allowance_values = []

for i in range(num_allowances):
    amount = float(
        input(f"Allowance {i+1}: ")
    )

    allowance_values.append(amount)

extra_total = pm.add_allowances(
    *allowance_values
)

print("\nTotal Allowances =", extra_total)

# Net Salary

net_salary = gross_salary + extra_total - tax

print("Net Salary =", net_salary)

# Lambda Function Demo

grade = pm.salary_grade(net_salary)

print("Salary Grade =", grade)

# Variable-Length Keyword Arguments

pm.display_additional_info(
    Email="employee@company.com",
    Location="Pune",
    Experience="5 Years",
    EmploymentType="Full Time"
)

# Local Scope Demo

pm.local_scope_demo()

print("\nProgram Completed Successfully")
 
# Variable-Length Keyword Arguments

def display_additional_info(**details):

    print("\nAdditional Information")

    print("----------------------")



    for key, value in details.items():



        print(f"{key} : {value}")