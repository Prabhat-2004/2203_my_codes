class Bank:
    def __init__(self,name,age,balance):
        self.name = name
        self.age = age
        self.balance = balance
    def details(self):
        print(f"Name: {self.name}, Age: {self.age}, Balance: {self.balance}")
    def deposite(self,add):
        print(f"Deposited Amount: {add}")
        self.balance += add
        print(f"Total Amount: {self.balance}")
    def withdraw(self,withdraw):
        print(f"Withdrawl Amount: {withdraw}")
        self.balance -= withdraw
        print(f"Total Amount: {self.balance}")   
name = input("Name:")
age = int(input("Age:"))
balance = float(input("Balance:"))
add = float(input("Deposited Amount:"))
withdraw = float(input("Withdral Amount:"))
b = Bank(name,age,balance)
b.details()
b.deposite(add)
b.withdraw(withdraw)

