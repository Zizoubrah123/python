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

# class BankAccount:
#     # don't forget to add some default values for these parameters!
#     bank_name = "dojo bank"
#     all_accounts = []

#     @classmethod
#     def __init__ (self, int_rate, balance): 
#         # your code here! (remember, instance attributes go here)
#         self.int_rate = int_rate
#         self.balance = balance


#         # don't worry about user info here; we'll involve the User class soon
#     def deposit(self, amount):

#         self.balance = amount + self.balance
#         return self
    
#         # your code here
#     def withdraw(self, amount):
#         self.balance = self.balance - amount 
#         return self
#         # your code here
#     def display_account_info(self):
#         print(f"balance:{self.balance}$ ")
#         return self
#     #     # your code here
#     def yield_interest(self):
#         if self.balance > 0: 
#             self.balance = (self.balance * self.int_rate) + self.balance
#             return self

# azizBarrah = BankAccount(0.01, 0,) 
# maramBetaib = BankAccount(0.01, 0,)

# azizBarrah.deposit(30).deposit(20).deposit(10).display_account_info().withdraw(50).yield_interest().display_account_info()
# maramBetaib.deposit(100).deposit(50).display_account_info().withdraw(30).withdraw(20).withdraw(10).withdraw(30).yield_interest().display_account_info()
# print   ("======================================")
# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         self.account = BankAccount(int_rate=0.01, balance=60)
#     # other methods
    
#     def make_deposit(self, amount):
#         self.account.deposit(amount)
#         # print(f"{self.name} checking balance {self.account.balance}")
#         return self
    
#     def make_withdraw (self, amount):
#         self.account.withdraw(amount)
#         # print(f"{self.name} saving balance {self.account.int_rate}")
#         return self
    
#     def display_user_info(self):
#         print(f"welcome {self.name} ")
#         print(f"email : {self.email}")
#         print(f"current balance is :{self.account.balance}$ ")
#         print(f"saving balance is :{self.account.int_rate}$")



# azizBarrah = User("aziz barrah", "barrah@gmail.com")
# maramBetaib = User("maram betiab", "maram@gmail.com")

# azizBarrah.display_user_info()
# print   ("======================================")
# maramBetaib.display_user_info()


# def countdown(n):
#     return list(range(n, -1, -1))

# countdown_list = countdown(5)
# print(countdown_list)

# ===========================================

# def print_and_return(z):
#     print(a[0])
#     return (a[1])

# a = [1,2]
# print_return = print_and_return(a)

# # ===========================================

# def plus_list(a):
#     return a[0] + len(a)

# a = [1,2,3,4,5]
# b = plus_list(a)
# print (b)

# # =============================================

# def new_list (aze):
#     sum = aze
#     if len(aze) > 2:
#         for i in range(len(aze)):
#             print(aze[2])
#             return (aze[::-2])

# aze = [1,2,3,4,5]
# ab = new_list(aze)
# print(ab)

# # =============================================

# def integers (size, value):
#     return [value] * size

# az = integers (5,1)
# print (az)

# person = {"first": "Ada", "last": "Lovelace", "age": 42, "is_organ_donor": True}
# # Adds a new key value pair for email to person
# person["email"] = "alovelace@codingdojo.com"
        
# # Changes person's "last" value to "Bobada"

# person["last"] = "Bobada"


# print(person["first"])
# person = full_name = person["first"] + " " + person["last"]

# print(person)


# capitals = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}
# # another way to iterate through the keys
# for key in capitals.keys():
#     print(key)
# # output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
# #to iterate through the values
# for val in capitals.values():
#     print(val)
# # output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
# #to iterate through both keys and values
# for key, val in capitals.items():
#     print(key, " = ", val)
# # output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc

# Player class with updated constructor

class dojo_Store :
    store_name = "dojoStore"
    
    def __init__(self,name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def price_update(self, percent_change, is_increased):
        if self.price > 25:
            self.price = (self.price / percent_change) *100
            print (f"{self.name} is now {self.price}")
            return self
        elif self.price < 25:
            self.price = self.price + is_increased
            return print (f"{self.name} is {self.price}$ now ({self.category})")



food_potato = dojo_Store ("chicken_breast", 20, "chicken")

food_potato.price_update(20, 10)


