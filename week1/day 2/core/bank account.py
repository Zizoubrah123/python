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
        print(f"balance:{self.balance} ")
    #     # your code here
    def yield_interest(self):
        if self.balance > 0: 
            self.balance = (self.balance * self.int_rate) + self.balance

azizBarrah = BankAccount(0.01, 0,)

azizBarrah.deposit(100).withdraw(20).yield_interest().display_account_info()
# azizBarrah
# azizBarrah
# azizBarrah


