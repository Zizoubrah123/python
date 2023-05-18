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
print   ("======================================")
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.01, balance=60)
    # other methods
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        # print(f"{self.name} checking balance {self.account.balance}")
        return self
    
    def make_withdraw (self, amount):
        self.account.withdraw(amount)
        # print(f"{self.name} saving balance {self.account.int_rate}")
        return self
    
    def display_user_info(self):
        print(f"welcome {self.name} ")
        print(f"email : {self.email}")
        print(f"current balance is :{self.account.balance}$ ")
        print(f"saving balance is :{self.account.int_rate}$")



azizBarrah = User("aziz barrah", "barrah@gmail.com")
maramBetaib = User("maram betiab", "maram@gmail.com")

azizBarrah.display_user_info()
print   ("======================================")
maramBetaib.display_user_info()