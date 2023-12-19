# Create Bankaccount.
class Bankaccount:
    def __init__(self,accno,money=0):
        self.__acc_number=accno
        self.__balance=money
    def get_account(self):
        return self.__acc_number
    def get_balance(self):
        return self.__balance
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        self.__balance-=amount
    def transfer(self,amount,acc):
        self.__balance-=amount
        acc.deposit(amount)
        