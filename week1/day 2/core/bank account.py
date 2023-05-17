class BankAccount:
    # don't forget to add some default values for these parameters!
    bank_name = "dojo bank"
    all_accounts = []

    @classmethod
    def __init__ (self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        self.int_rate = int_rate
        self.balance = balance


        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):

        self.balance = amount + self.balance
        return self
    
        # your code here
    def withdraw(self, amount):
        self.balance = self.balance - amount 
        return self
        # your code here
    def display_account_info(self):
        print(f"balance:{self.balance}$ ")
        return self
    #     # your code here
    def yield_interest(self):
        if self.balance > 0: 
            self.balance = (self.balance * self.int_rate) + self.balance
            return self

azizBarrah = BankAccount(0.01, 0,)
maramBetaib = BankAccount(0.01, 0,)

azizBarrah.deposit(30).deposit(20).deposit(10).display_account_info().withdraw(50).yield_interest().display_account_info()
maramBetaib.deposit(100).deposit(50).display_account_info().withdraw(30).withdraw(20).withdraw(10).withdraw(30).yield_interest().display_account_info()


