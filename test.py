# num = 25
# dec = 4.2

# print(num)
# print(type(dec))

# num_to_dec = float(num)
# import random
# rand_num = random.randint(2,5)

# print( $)

# int_to_float = float(35)
# float_to_int = int(44.2)
# int_to_complex = complex(35)
# print(int_to_float)
# print(float_to_int)
# print(int_to_complex)
# print(type(int_to_float))
# print(type(float_to_int))
# print(type(int_to_complex))

# import random
# print(random.randint(2,5)) # provides a random number between 2 and 5

# name = "Zen"
# print("My name is", name)

# name = "Zen"
# print("My name is " + name)

# x = "hello world"
# print(x.title())
# # output:
# "Hello World"

# fruits = ['apple', 'banana', 'orange', 'strawberry']
# vegetables = ['lettuce', 'cucumber', 'carrots']
# fruits_and_vegetables = fruits + vegetables
# print(fruits_and_vegetables)
# salad = 3 * vegetables
# print(salad)

# my_list = [1, 'Zen', 'hi']
# print(max(my_list))

# x = 55
# if x > 10:
#     	print("bigger than 10")
# elif x > 50:
#     	print("bigger than 50")
# else:
#     	print("smaller than 10")

# Challenge 1: Fix the range!
# for val in "string":
#     if val == "i":
#         break
#     print(val)
# # output: s, t, r

# def full_name(name='', repeat=2):
#     print(f"good morning {name}\n" * repeat)

#     full_name(name="azizBarrah", repeat=2 )

# def be_cheerful(name='', repeat=2):
# 	print(f"good morning {name}\n" * repeat)
# be_cheerful()    # output: good morning (repeated on 2 lines)
# be_cheerful("aziz")    # output: good morning tim (repeated on 2 lines)
# be_cheerful(name="barrah")    # output: good morning john (repeated on 2 lines)
# be_cheerful(repeat=6)    # output: good morning (repeated on 6 lines)
# be_cheerful(name="zizou", repeat=5)    # output: good morning michael (repeated on 5 lines)
# # NOTE: argument order doesn't matter if we are explicit when sending in our arguments!
# be_cheerful(repeat=3, name="uwu") 

# def full_name ( name='', repeat=2):
#     print(f"good morning {name}\n" * repeat)
# full_name ()
# full_name(name="aziz")

# class User:		
#     def __init__(self):
#         self.first_name = "Ada"
#         self.last_name = "Lovelace"
#         self.age = 42

# user_ada = User()
# print(user_ada.first_name)

# # Create another user called user_2!
# user_2 = User()
# print(user_2.last_name)

# declare a class and give it name Shoe
# class Shoe:		
#     def __init__(self):
#         self.brand = "Vans"
#         self.type = "Classic Sk8-Hi"
#         self.price = 69.99
#         self.in_stock = True



# skater_shoe = Shoe()
# dress_shoe = Shoe()
# # Accessing the instance's attributes
# print(skater_shoe.type) # Classic Sk8-Hi
# print(dress_shoe.type)	# Classic Sk8-Hi

# skater_shoe.type = "Low-top Trainers"
# print(skater_shoe.type)
# # output: Low-top Trainers
# dress_shoe.type = "Ballet Flats"
# print(dress_shoe.type)
# # output: Ballet Flats

# class BankAccount:
#     # Declaring a class attribute
#     # Shared among all bank accounts
#     bank_name = "First National Dojo"		
    
#     def __init__(self, int_rate, balance):
#         self.int_rate = int_rate
#         self.balance = balance

# adriensAccount = BankAccount()
# sadiesAccount = BankAccount()
# adriensAccount.bank_name = "Dojo Credit Union"
    
# print(adriensAccount.bank_name)
# # output: Dojo Credit Union
    
# print(sadiesAccount.bank_name)
# # output: First National Dojo


# BankAccount.bank_name = "Bank of Dojo"
    
# print(adriensAccount.bank_name)
# # output: Bank of Dojo
    
# print(sadiesAccount.bank_name)
# # output: Bank of Dojo

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


