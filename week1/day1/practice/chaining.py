class User:

    def __init__(self, first_name, last_name, email, age, is_rewards_member, gold_card_points  ):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = gold_card_points

    def display_info (self):
        print(f"Hello, my name is {self.first_name} {self.last_name} my email is {self.email} and im {self.age} years old ")
        return self
    def enrole (self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self
    def spend_points (self, amount):
        self.gold_card_points=self.gold_card_points-amount
        print(self.gold_card_points) 
        return self
user1 = User("aziz", "barrah", "example@gmail.com", 19, False, 0)
user1.display_info()

user2 = User("maram", "betaib", "maramBeitaib@gmail.com", 17, False,0 )
user3 = User("adem", "barrah", "adembarrah@gmail.com 16", 16, False,0)


user1.enrole()
user1.spend_points(50)
user1.display_info()


user2.display_info()
user2.enrole()
user2.spend_points(80)

user3.display_info()
user3.enrole()
user3.spend_points(80)



