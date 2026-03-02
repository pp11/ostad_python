# Create a class BankAccount with a private attribute balance and provide methods deposit() 
# and withdraw() to modify the balance safely so that the balance cannot be accessed directly. 
# Then create two subclasses SavingsAccount and CurrentAccount, each having a method account_type() 
# that prints its respective account type. 
# Demonstrate polymorphism by calling account_type() from different account objects.



class BankAccount:
    def __init__(self):
        self.__balance=5000

    def account_type(self):
        pass

    def deposit(self, savings_amt):        
        self.__balance =self.__balance+savings_amt
        return(self.__balance)

    def withdraw(self, deposit_amt):
        if self.__balance>=deposit_amt:
            self.__balance =self.__balance-deposit_amt
            return(self.__balance)
        else:
            return "Insufficient balance"

bank1=BankAccount()

print(bank1.deposit(7500))
print(bank1.withdraw(2500))
print(bank1.deposit(200))


class SavingsAccount(BankAccount):
    def account_type(self):
        print("account type is Savings Account")

class CurrentAccount(BankAccount):
     def account_type(self):
        print("account type is current Account")

def find_account(type):
    type.account_type()

find_account(SavingsAccount())
find_account(CurrentAccount())