class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited {amount}. New balance is {self.balance}."
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew {amount}. New balance is {self.balance}."
        else:
            return "Insufficient funds or invalid amount."

    def check_balance(self):
        return f"Current balance is {self.balance}."

    def __str__(self):
        return f"Account Number: {self.account_number}, Account Holder: {self.account_holder}, Balance: {self.balance}"

def create_account():
    account_number = input("Enter account number: ")
    account_holder = input("Enter account holder name: ")
    initial_deposit = float(input("Enter initial deposit amount: "))
    return BankAccount(account_number, account_holder, initial_deposit)
