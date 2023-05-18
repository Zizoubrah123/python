class user:

    def __init__(self, first_name, last_name, email, age, is_rewards_member, gold_card_points  ):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member : False
        self.gold_card_points = gold_card_points

    def display_info (self):
        print(f"Hello, my name is {self.first_name} {self.last_name} my email is {self.email} and im {self.age} years old")

    def spend_points (self, amount):
        self.gold_card_points=self.gold_card_points-amount
        print(self.gold_card_points) 

user1 = user("aziz", "barrah", "example@gmail.com", 19, True, 200)
user2 = user("maram", "betaib", "maramBeitaib@gmail.com", 17,True,200 )

user1.display_info();
user1.spend_points(50);

user2.display_info();
user2.spend_points(80)
