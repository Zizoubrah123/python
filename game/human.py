class Human:

    def __init__(self):
        self.name = "generic Human"
        self.health = 100
        self.strength = 10
        self.agility = 10
        self.defence = 5

    #method

    def attack(self, target):
        print (f"[ATTACK] {self.name} is attacking {target.name}")
        target.defend(self.strength) #! abstaction

    def defend(self, damage):
        damage -= self.defence
        self.health -= damage
        print (f"[DEFEND] {self.name} takes {damage} DMG and now has {self.health} HP")

#instantiate

player1 = Human()
player2 = Human()

player1.attack(player2)