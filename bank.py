class Bank:
    def get_account(self):
        self.id = input("Enter the ID : ")
        self.type = input("Enter the type of account : ")
        self.balance = float(input("Enter the balance : "))
        
    def show_account(self):
        print("\nAccount Details : ")
        print("Account ID : ",self.id)
        print("Account type : ",self.type)
        print("Balance : ",self.balance)
        
    def transaction(self):
        count = 0
        choice = input(print("\nPlease select the type of tansaction : \n1. Deposit \n2. Withdraw \n3. Exit \nEnter your choice : "))
        if (choice == 1):
            amount = float(input(print("\nEnter the amount you want to deposit : ")))
            print("Amount deposited successfully")
            print("Updated balance : ",self.balance + amount)
            count += 1
            self.transaction()
        elif (choice == 2):
            debit = float(input(print("\nEnter the amount you want to withdraw : ")))
            print("Amount withdrawn successfully")
            print("Updated balance : ",self.balance - debit)
            count += 1
            self.transaction()
        else:
            exit
    
b = Bank()
b.get_account()
b.show_account()
b.transaction()    

