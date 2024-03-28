from bank_accounts import *

venkat= BankAccount("Venkat", 50000)
sail = BankAccount("Sail", 55000)

venkat.get_balance()
venkat.deposit(500)

sail.withdraw(500)
sail.withdraw(55000)