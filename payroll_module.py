# Global Variables
company_name = "ABC Corporation";

# Function Definition + Parameters + Return Values
def calculate_salary(basic_salary, hra, bonus):
    """
    Calculate the total salary of an employee.

    Parameters:
    basic_salary (float): The basic salary of the employee.
    hra (float): The house rent allowance.
    bonus (float): The bonus amount.

    Returns:
    float: The total salary of the employee.
    """
    total_salary = basic_salary + hra + bonus
    return total_salary

# Default argument function
def calculate_tax(salary, tax_rate=0.1):
    """
    Calculate the tax amount based on the salary and tax rate.

    Parameters:
    salary (float): The total salary of the employee.
    tax_rate (float, optional): The tax rate to be applied. Default is 0.1 (10%).

    Returns:
    float: The calculated tax amount.
    """
    tax_amount = salary * tax_rate
    return tax_amount    

# Positional & Keyword Arguments function
def employee_details(emp_id, name, department):
    """
    Display the details of an employee.

    Parameters:
    emp_id (int): The employee ID.
    name (str): The name of the employee.
    department (str): The department of the employee.

    Returns:
    None
    """
    print(f"Employee ID: {emp_id}")
    print(f"Name: {name}")
    print(f"Department: {department}")

# Variable Length Arguments function
def add_allowances(*allowances):
    """
    Calculate the total allowances for an employee.

    Parameters:
    *allowances (float): Variable length arguments representing different allowances.

    Returns:
    float: The total allowances.
    """
    total_allowances = sum(allowances)
    return total_allowances

# Lambda Function
salary_grade = lambda salary: ("Grade A" if salary >= 100000 else "Grade B" if salary >= 50000 else "Grade C")

# Local scope
def local_scope():
    """
    Demonstrate local scope by defining a variable within the function.

    Returns:
    str: A message indicating the local variable value.
    """
    local_variable = "I am a local variable"
    print(f"Inside the function, local_variable: {local_variable}")
    return local_variable

# Global scope
def display_company():
    """
    Display the company name using a global variable.

    Returns:
    None
    """
    print(f"Company Name: {company_name}")

# Variable-Length Keyword Arguments

def display_additional_info(**details):

    print("\nAdditional Information")
    print("----------------------")

    for key, value in details.items():
        print(f"{key} : {value}")
 