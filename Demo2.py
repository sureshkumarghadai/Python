import CurrentAccount as CA;
import SavingsAccount as SA;

# Objects
acc1 = SA.SavingsAccount(101, "Saket", 100000, 5)
acc2 = SA.SavingsAccount(102, "Rahul", 50000, 5)

# Encapsulation
print(acc1.get_balance())

# Deposit
acc1.deposit(10000)

# Withdraw
acc1.withdraw(5000)

# Polymorphism
print(acc1.add_interest())

# Magic Method __str__
print(acc1)

# Magic Method __eq__
print(acc1 == acc2)

# Magic Method __add__
print(acc1 + acc2)

# Abstract + Inheritance
accounts = [
    SA.SavingsAccount(201, "A", 30000, 10),
    CA.CurrentAccount(301, "B", 50000, 10)
]

for account in accounts:
    print(account.add_interest() if isinstance(account, SA.SavingsAccount) else 0);