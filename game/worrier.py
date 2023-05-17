from human import Human

class Warrior(Human):
    def __init__(self):
        super().__init__()

        self.strength += 20
        self.health +=30
