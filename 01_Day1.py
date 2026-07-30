#Program Name: Hello World
#Author: Suresh Ghadai
#Version: 1.0

"""
This Program demonstrates
a multi-line comment.
"""

print("Hello World")
print("Hello, World!"); # This displays "Hello, World!" on terminal

# This displays "Welcome to Python Program!" on terminal.
print("Welcome to Python Program!");

def greet(name):
    """Displays a welcome message.""" # This is docstring for the function greet()
    print("Welcome, " + name)

greet("Suresh Ghadai");

print(greet.__doc__);