class Lowbalance(Exception):
    pass

class BankAccount:
    
    def __init__(self):
        self.balance=50000

    def showBalance(self):
        print "Your Balance is ",self.balance

    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self,amount):
        try:
            if amount>self.balance:
                raise Lowbalance("Insufficient balance , min balance should be 50000")
            elif self.balance-amount < 50000:
                raise Lowbalance("Insufficient balance, min balance should be 50000")
            else:
                self.balance-=amount
        except Lowbalance as a:
            print a
            

obj1=BankAccount()
obj1.showBalance()
print "============================================="

print "Depositing 1000 "
obj1.deposit(1000)
obj1.showBalance()
print "============================================="

print "Withdrawing 50"
obj1.withdraw(50)
obj1.showBalance()
print "============================================="

print "Withdrawing 500000"
obj1.withdraw(500000)
obj1.showBalance()
print "============================================="

print "Withdrawing 950"
obj1.withdraw(950)
obj1.showBalance()
print "============================================="

print "Withdrawing 1"
obj1.withdraw(1)
obj1.showBalance()

