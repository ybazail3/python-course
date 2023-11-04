# OOP Project

# Created a class named BalnceException and we are passing through Exception
class BalanceException(Exception):
    pass

# Created a class named BankAccount


class BankAccount:
    # Using init method (function) lets the class initalize the objects attributes
    # Passing through self (always), initial-amount and acct_name
    def __init__(self, initial_amount, acct_name):
        # Here we are setting the values of balance and name
        self.balance = initial_amount
        self.name = acct_name
        # Using the format method to call the name and current balance of a persons bank acct
        print(
            f"\nAccount '{self.name}'  created.\nBalance = ${self.balance:.2f}")

    # Created a function name get_balance and passing through self as an argument
    def get_balance(self):
        # This function will print the acct name and current balance
        print(
            f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    # Created a function naked deposit passing through two args of self and amount
    def deposit(self, amount):
        # Adding the current balance and new deposit amount
        self.balance = self.balance + amount
        print("\nDeposit complete.")
        # Calling the get_balance function in order to print the new balance with the deposit
        self.get_balance()

    # Creating a new function named viable_trans passing through two arguments self and amount
    def viable_trans(self, amount):
        # If statement comparing if the current balance is greater than or equal to the amount wanting to be be withdrawn it will allow the withdraw
        if self.balance >= amount:
            return
        # If the first statement is false then it will let you know that person does not hae the funds
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}")

    # Created a function name withdraw and passing through 2 args self and amount
    def withdraw(self, amount):
        # Using try block to test a block of code. This is saying if the amount wanting to be withdrawn is in tthe acct subtract the amount from the current balance. And print withdraw complete. After this is done call the balance again (after the withdraw)
        try:
            self.viable_trans(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete.")
            self.get_balance()

        # except lets you handle the error. If there is an error like maybe that person does not have the funds, Then withdraw interrupted will be printed.
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")

    # Created a function name transfer.  Passing through three args self, amount, and account. If the amount is able to be withdrawn then withdraw it and deposit it into another persons acct. Once this is completed print transfer completed.
    def transfer(self, amount, account):
        try:
            print("\n**********\n\nBeginning Transfer.. ")
            self.viable_trans(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer complete!\n\n**********")

        # except block lets you hande the error. If there is any error this will print transfer interrupted.
        except BalanceException as error:
            print(f"\nTransfer interrupted. {error}")

# Created a class named InterestRewa... Passing through the BankAccount class inheriting it


class InterestRewardsAcct(BankAccount):
    # redefining the deposit function but still passing through the same args self and amount
    def deposit(self, amount):
        # Setting every deposit to at 5%, This lin ewill add the current balance and the deposit + 5% and then print the new balance afterwards.
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete.")
        self.get_balance()

# Created a class named SavingsAcct passing through the InterestRew... class inheriting it


class SavingsAcct(InterestRewardsAcct):
    # Using another init function and passing through 3 arguments self, initial_amount, acct_name
    def __init__(self, initial_amount, acct_name):
        #
        super().__init__(initial_amount, acct_name)
        self.fee = 5

    # Creating a new withdraw function for this class with two args self and amount
    def withdraw(self, amount):
        # This try block is checking if the withdraw amount plus the fee is in the account then it will be okay to withdraw the funds
        try:
            self.viable_trans(amount + self.fee)
            # Current balance minus withdraw amount and fee
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw complete")
            # This will print the new balance after the withdraw
            self.get_balance()
        # This except block will print withdraw interuptted if the funds are not available
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")
