from bank_account_practice import *

John = BankAccount(1000, "John")
Jane = BankAccount(2000, "Jane")

John.get_balance()
Jane.get_balance()

Jane.deposit(400)

John.withdraw(5000)
John.withdraw(50)

John.transfer(3000, Jane)
John.transfer(300, Jane)

Jim = InterestRewardsAcct(1000, "Jim")

Jim.get_balance()

Jim.deposit(100)

Jim.transfer(100, Jane)

Noah = SavingsAcct(2000, "Noah")

Noah.get_balance()

Noah.deposit(100)

Noah.transfer(1000, Jane)
