import Account;

class CurrentAccount(Account.Account):
    def __init__(self, account_number, account_holder, balance, overdraft_limit):
        super().__init__(account_number, account_holder, balance)
        self.__overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.get_balance() + self.__overdraft_limit:
            self.set_balance(self.get_balance() - amount)
            print(f"Withdrawal of {amount} successful. New balance: {self.get_balance()}")
        else:
            print("Withdrawal failed. Insufficient funds including overdraft limit.")

    def deposit(self, amount):
        if amount > 0:
            self.set_balance(self.get_balance() + amount)
            print(f"Deposit of {amount} successful. New balance: {self.get_balance()}")
        else:
            print("Deposit failed. Amount must be positive.")

    def get_overdraft_limit(self):
        return self.__overdraft_limit

    def set_overdraft_limit(self, new_limit):
        self.__overdraft_limit = new_limit
 