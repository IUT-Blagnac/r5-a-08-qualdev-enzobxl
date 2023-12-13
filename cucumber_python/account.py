class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Amount cannot be negative or null")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print("Insufficient funds!")
        else:
            print("Amount cannot be negative or null")

    def transfer(self, target_account, amount):
        if amount <= self.balance:
            self.balance -= amount
            target_account.deposit(amount)
            print(f"Transferred ${amount} to {target_account.name}. New balance: ${self.balance}")
        else:
            print("Insufficient funds!")
