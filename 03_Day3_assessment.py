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
# number= int(input("Enter the table number: "))
# print("\nReverse Multiplication Table")
# print("-" * 20)
# for i in range(10,0,-1):
#     print(f"{number} x {i}= {number * i} ")
# Generate Multiple Tables
# starting_number = int(input("Enter starting number: "))
# ending_number = int(input("Enter ending number: "))

# for num in range(starting_number, ending_number + 1):

#     print(f"\nMultiplication Table of {num}")
#     print("-" * 30)

#     for i in range(1, 11):
#         print(f"{num} x {i} = {num * i}")

# Prime Number
# number = int(input("Enter a number: "))

# for i in range(2,number):
#     if number%i == 0:
#         print(number," is not a prime number")
#         break
#     else:
#         print(number,"is a prime number")
#         break

# """
# Simple ATM Banking System
# --------------------------
# Author: Python Developer
# Description:
#     A menu-driven ATM simulator with:
#       - PIN verification
#       - Check Balance / Deposit / Withdraw / Exit
#       - Transaction history
#       - Daily withdrawal limit
#       - Input validation (non-numeric, negative, zero)
#       - Displays current date & time on the menu
# """

# from datetime import datetime   # needed to get today's date and current time

# # ---------- Step 1: Starting account data ----------
# balance = 5000.0
# correct_pin = "1234"
# transaction_history = []      # list of strings describing each transaction
# daily_withdrawn = 0.0         # total withdrawn so far in this session ("today")
# DAILY_WITHDRAWAL_LIMIT = 20000.0


# # ---------- Step 1b: Helper to get a timestamp for logging ----------
# def get_timestamp():
#     """Return the current date and time as a formatted string, for use in logs."""
#     return datetime.now()


# # ---------- Step 2: Helper to safely read a number ----------
# def get_amount(prompt):
#     """
#     Ask the user for an amount and validate it is a number.
#     Returns None if invalid, so the caller can handle the error.
#     """
#     value = input(prompt).strip()
#     try:
#         return float(value)
#     except ValueError:
#         print("Invalid input. Please enter a numeric value (e.g., 500 or 500.50).")
#         return None


# # ---------- Step 3: PIN verification ----------
# def verify_pin():
#     """Ask for a PIN up to 3 times before locking the user out."""
#     for attempt in range(3):
#         pin = input("Enter your 4-digit PIN: ").strip()
#         if pin == correct_pin:
#             print("PIN verified successfully.\n")
#             return True
#         else:
#             print(f"Incorrect PIN. {2 - attempt} attempt(s) remaining.")
#     print("Too many incorrect attempts. Exiting for security reasons.")
#     return False


# # ---------- Step 4: Core ATM features ----------
# def check_balance(balance):
#     print(f"\nYour current balance is: {balance:.2f}")
#     timestamp = get_timestamp()
#     transaction_history.append(f"[{timestamp}] Balance inquiry -> Balance: {balance:.2f}")
#     return balance


# def deposit_money(balance):
#     amount = get_amount("Enter amount to deposit: ")
#     if amount is None:
#         return balance

#     if amount <= 0:
#         print("Deposit amount must be greater than zero.")
#         return balance

#     balance += amount
#     timestamp = get_timestamp()
#     transaction_history.append(f"[{timestamp}] Deposited {amount:.2f} -> New Balance: {balance:.2f}")
#     print(f"Deposit successful! Updated balance: {balance:.2f}")
#     return balance


# def withdraw_money(balance, daily_withdrawn):
#     amount = get_amount("Enter amount to withdraw: ")
#     if amount is None:
#         return balance, daily_withdrawn

#     if amount <= 0:
#         print("Withdrawal amount must be positive.")
#         return balance, daily_withdrawn

#     if amount > balance:
#         print(f"Insufficient funds. Your current balance is {balance:.2f}")
#         return balance, daily_withdrawn

#     if (daily_withdrawn + amount) > DAILY_WITHDRAWAL_LIMIT:
#         remaining = DAILY_WITHDRAWAL_LIMIT - daily_withdrawn
#         print(f"Daily withdrawal limit exceeded. You can withdraw up to {remaining:.2f} more today.")
#         return balance, daily_withdrawn

#     balance -= amount
#     daily_withdrawn += amount
#     timestamp = get_timestamp()
#     transaction_history.append(f"[{timestamp}] Withdrew {amount:.2f} -> New Balance: {balance:.2f}")
#     print(f"Withdrawal successful! Updated balance: {balance:.2f}")
#     return balance, daily_withdrawn


# def show_transaction_history():
#     print("\n----- Transaction History -----")
#     if not transaction_history:
#         print("No transactions yet.")
#     else:
#         for i, record in enumerate(transaction_history, start=1):
#             print(f"{i}. {record}")
#     print("--------------------------------")


# # ---------- Step 5: Menu display ----------
# def show_menu():
#     current_datetime = datetime.now().strftime("%d-%b-%Y %I:%M:%S %p")
#     print("\n===== ATM MENU =====")
#     print(f"Date & Time: {current_datetime}")
#     print("1. Check Balance")
#     print("2. Deposit Money")
#     print("3. Withdraw Money")
#     print("4. View Transaction History")
#     print("5. Exit")


# # ---------- Step 6: Main program (menu loop) ----------
# def main():
#     global balance  # not strictly needed since we reassign via return, kept for clarity

#     print("Welcome to the Simple ATM Banking System")

#     if not verify_pin():
#         return   # stop the program if PIN verification fails

#     bal = balance
#     withdrawn_today = daily_withdrawn

#     while True:
#         show_menu()
#         choice = input("Enter your choice (1-5): ").strip()

#         if choice == "1":
#             bal = check_balance(bal)
#         elif choice == "2":
#             bal = deposit_money(bal)
#         elif choice == "3":
#             bal, withdrawn_today = withdraw_money(bal, withdrawn_today)
#         elif choice == "4":
#             show_transaction_history()
#         elif choice == "5":
#             print("\nThank you for banking with us. Have a great day!")
#             break
#         else:
#             print("Invalid choice. Please select an option between 1 and 5.")


# if __name__ == "__main__":
#     main()




    
