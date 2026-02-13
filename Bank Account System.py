class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")
    def display_balance(self):
        print("Current Balance:", self.balance)
acc = BankAccount("Kumar", 10000)
acc.deposit(5000)
acc.withdraw(3000)
acc.display_balance()
