class Player:
    def __init__(self, dictionary):
        self.name = dictionary["name"]
        self.age =dictionary["age"] 
        self.position =dictionary["position"] 
        self.team =dictionary["team"] 

    def __repr__(self):
        display = f"Player: {self.name}, {self.age} y/o, pos: {self.position}, team: {self.team}"

        return display

kevin = {
    "name": "Kevin Durant", 
	"age":34, 
    "position": "small forward", 
	"team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum", 
	"age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving", 
	"age":32,
        "position": "Point Guard", 
    "team": "Brooklyn Nets"
}


player_Kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

print(player_jason)
print(player_Kevin)
print(player_kyrie)
