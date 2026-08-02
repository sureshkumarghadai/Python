# import random
# # Define range
# Min_Number = 1
# Max_Number = 100
# # Generate random number
# secret_number = random.randint(Min_Number, Max_Number)
# # Initialize counter
# attempts = 0
# print("====================================")
# print(" Welcome to Number Guessing Game ")
# print("====================================")
# print(f"Guess a number between {Min_Number} and {Max_Number}")
# while True:
#     guess = input("\nGuess the number: ")
#     # Validate numeric input
#     if not guess.isdigit():
#         print("Invalid input. Please enter a numeric Number.")
#         continue
#     guess = int(guess)
#     # Validate range
#     if guess < Min_Number or guess > Max_Number:
#         print(f"Please enter a number between {Min_Number} and {Max_Number}.")
#         continue
#     # Count valid attempts
#     attempts += 1
#     # Compare numbers
#     if guess < secret_number:
#         print("Too Low")
#     elif guess > secret_number:
#         print("Too High")
#     else:
#         print("\nCongratulations!")
#         print(f"You guessed the correct number: {secret_number}")
#         print(f"Total Attempts: {attempts}")
#         break
 #Assessment # 2
 # Generate Multiplication Tables
  
# number = int(input("Enter a number: "))

# print("\nMultiplication Table")
# print("-" * 12)

# for i in range(1, 11):
#     result = number * i
#     print(f"{number} x {i} = {result}")
# Generate Functional Requirements - Custom table from and to
# number = int(input("Enter the table Number: "))
# startcolumn = int(input("Enter the starting multiplier: "))
# Endcolumn = int(input("Enter the ending multiplier :"))
# print("\nMultiplication Table")
# print("-" * 20)
# for i in range(startcolumn,Endcolumn+1):
#     print(f"{number} x {i}= {number * i} ")

# Reverse Multiplication Table
number= int(input("Enter the table number: "))
print("\nReverse Multiplication Table")
print("-" * 20)
for i in range(10,0,-1):
    print(f"{number} x {i}= {number * i} ")