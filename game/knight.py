from human import Human
# print(human.Human)

class Knight(Human):
    def __init__  (self):
        super().__init__()

        self.name = "arthur"
        self.health= 110 
        self.strength += 10 #20
        self.defence +=5

    def heal(self):
        self.health += 20
        print(f"[KNIGHT] {self.name} heals for {20} HP and now has  {self.health} HP")

HolyKnight = Knight("arthur")
villan = Knight ("Lucifer")

HolyKnight.attack()