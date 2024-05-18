# Bank Account
class BankAccount:
    default_accountNumber = 1
    def __init__(self,name,balance=0):
        self.name = name
        self.balance = balance
        self.accountNumber = BankAccount.default_accountNumber
        BankAccount.default_accountNumber += 1

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if self.balance < amount:
            print('Not enough balance!')
        else:
            self.balance -= amount
    def display(self):
        print(f"Welcome to ICICI bank. The name of the customer is {self.name} and Total balance is {self.balance}")

    def getbalance(self):
        print(f"your current balance is {self.balance} rupees only")

harish = BankAccount("Harish Kumar",100000)
harish.display()
harish.deposit(120000)
harish.getbalance()
harish.withdraw(20000)
harish.getbalance()

