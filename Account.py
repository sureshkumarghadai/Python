from abc import ABC, abstractmethod;

class Account(ABC):
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number; # public attribute
        self.account_holder = account_holder; # public attribute
        self.__balance = balance; # private attribute

    @abstractmethod
    def deposit(self, amount):
        pass;

    @abstractmethod
    def withdraw(self, amount):
        pass;

    def get_balance(self): # Concrete method to access the private attribute balance
        return self.__balance;

    def set_balance(self, amount): # Concrete method to modify the private attribute balance
        if amount >= 0:
            self.__balance = amount;
        else:
            raise ValueError("Balance cannot be negative.");