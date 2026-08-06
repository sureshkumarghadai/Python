import Account as acc;

class SavingsAccount(acc.Account):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance);
        self.interest_rate = interest_rate; # public attribute

    def deposit(self, amount):
        if amount > 0:
            new_balance = self.get_balance() + amount;
            self.set_balance(new_balance);
        else:
            raise ValueError("Deposit amount must be positive.");

    def withdraw(self, amount):
        if 0 < amount <= self.get_balance():
            new_balance = self.get_balance() - amount;
            self.set_balance(new_balance);
        else:
            raise ValueError("Withdrawal amount must be positive and less than or equal to the current balance.");

    def add_interest(self):
        interest = self.get_balance() * (self.interest_rate / 100);
        new_balance = self.get_balance() + interest;
        self.set_balance(new_balance);

    def __str__(self):
        return f"SavingsAccount(account_number={self.account_number}, account_holder={self.account_holder}, balance={self.get_balance()}, interest_rate={self.interest_rate})";

    def __repr__(self):
        return f"SavingsAccount(account_number={self.account_number}, account_holder={self.account_holder}, balance={self.get_balance()}, interest_rate={self.interest_rate})";

    def __eq__(self, other):
        if isinstance(other, SavingsAccount):
            return self.account_number == other.account_number;
        return False;

    def __add__(self, other):
        return self.get_balance() + other.get_balance() if isinstance(other, SavingsAccount) else NotImplemented;
 