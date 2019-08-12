class BankAc:
    def __init__(self):
        self.balance=0
    def withdraw(self,amount):
        self.balance-=amount
        if self.balance<0:
            print("withdraw not possible")
            self.balance+=amount
        return self.balance
    def deposit(self,amount):
        self.balance+=amount
        return self.balance
    def display(self):
        print(self.display)
a=BankAc()
a.display()
d=int(input("enter the amount to deposit"))
a.deposit(d)
a.display()
w=int(input("enter the amount to withdraw:"))
a.withdraw(w)
a.display()
b=BankAc()
b.display()
d=int(input("enter the amount to deposit:"))
b.deposit(d)
b.display()
w=int(input("enter the amount to withdraw:"))
b.withdraw(w)
b.display()

