class BankAccount:
    def __init__(self,name,owner,account_no,current):
        self.name = name
        self.owner = owner
        self.account_no = account_no
        self.current_balance = current
    def deposit(self,money):
        self.current_balance += money
    def withdraw(self,money):
        self.current_balance -= money
    def printout(self):
        print(f"Current balace is {self.current_balance}")

me = BankAccount("A","B",4,100)
me.printout()