class Ninja:
    def __init__(self, first_name , last_name , treats , pet_food , pet ):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self, pet, treats ):

        return print(f"{self.first_name} toke {pet} for a {treats}!!")
    def feed(self, pet_food, pet, treats):
        return print (f"{self.first_name} {treats} {pet} some {pet_food}")
    def bathe(self, treats,pet):
        return print (f"{self.first_name} toke a {treats} for {pet} ")

class pet:
    def __init__(self, name , type , tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self, sleep):
        self.energy = self.energy + sleep
        return self
    def eat(self, eat, health):
        self.energy = self.energy + eat
        self.health = self.health + health
        return self
    def play(self, play):
        self.health = self.health + play
        return self
    def noice(pet):
        return print("meow!!")
    

azizbarrah = Ninja("aziz", "barrah", "", "", "mohsen")
mohsen = pet("mohsen", "cat", "run" , 100, 100)

azizbarrah.walk("mohsen","walk")
azizbarrah.feed("sardine","mohsen", "feeded")
azizbarrah.bathe("shower", "mohsen")
mohsen.sleep(25).eat(5, 10).play(5).noice()
    # sleep() - increases the pets energy by 25
    # eat() - increases the pet's energy by 5 & health by 10
    # play() - increases the pet's health by 5
    # noise() - prints out the pet's sound