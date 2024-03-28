class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self,accName,initiatlAmount):
        self.balance = initiatlAmount
        self.name= accName
        print("{}'s account created. \n Balance= {}".format(self.name, self.balance))
    

    def get_balance(self):
        print(f"{self.name}'s balace ={self.balance}")
    def deposit(self, amount):
        self.balance= self.balance+amount
        self.get_balance()

    def viableTransaction (self, withdrawamount):
        if self.balance<withdrawamount:
            raise BalanceException(
                f"sorry you insuffienct funds.\n {self.name} have only balance={self.balance}"
            )
        else:
            return
        

    def withdraw(self, withdrawamount):
        try :
            self.viableTransaction( withdrawamount)
            self.balance= self.balance-withdrawamount
            self.get_balance()

        except BalanceException as error:
            print (f"withdraw request declined.\n {error} ")





