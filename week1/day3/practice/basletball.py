class Player:
    def __init__(self, dictionary):
        self.name = dictionary["name"]
        self.age =dictionary["age"] 
        self.position =dictionary["position"] 
        self.team =dictionary["team"] 



players = [
    {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
    },
    {
    "name": "Kyrie Irving", 
    "age":32,
        "position": "Point Guard", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Damian Lillard", 
    "age":33,
    "position": "Point Guard", 
    "team": "Portland Trailblazers"
    },
    {
    "name": "Joel Embiid", 
    "age":32,
        "position": "Power Foward", 
    "team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]

p_Kevin = Player(players[0])

print(p_Kevin.name)
print("--------------------")
class Player1:
    def __init__(self, dictionary):
        self.name = dictionary["name"]
        self.age =dictionary["age"] 
        self.position =dictionary["position"] 
        self.team =dictionary["team"] 

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


player_Kevin = Player1(kevin)
print  (player_Kevin.team)
print ("---------------------")

player_jason = Player1(jason)
print (player_jason.position)
print ("------------------------")
player_kyrie = Player1(kyrie)
print(player_kyrie.age)

print("-------------------------------------------------")

class Player2:
    def __init__(self, dictionary):
        self.name = dictionary["name"]
        self.age =dictionary["age"] 
        self.position =dictionary["position"] 
        self.team =dictionary["team"] 

damain = {
    "name": "Damian Lillard", 
    "age":33,
    "position": "Point Guard", 
    "team": "Portland Trailblazers"
}

player_damain = Player1(damain)
print(player_damain.position)

print("--------------------------------------")

class team:
    def __init__(self, dictionary):
        self.name = dictionary["name"]
        self.age =dictionary["age"] 
        self.position =dictionary["position"] 
        self.team =dictionary["team"] 
new_team = []
for i in range (len(players)):
    new_team.append(team(players[i]))

