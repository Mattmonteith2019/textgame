import random

class Player:
    def __init__(self, name, health, strength, special):
        self.name = name
        self.health = health
        self.strength = strength
        self.special = special
p1 = Player("HERO", 100, 100, 10)
print(p1.name)
print(p1.health)
print(p1.strength)
print(p1.special)

print("\n")
# add  a comment


class Monster:
    def __init__(self, name, health, strength, special):
        self.name = name
        self.health = health
        self.strength = strength
        self.special = special

def generate_monster():
    monster_types = [
        ("Ogre", 25, 100, 50),
        ("Goblin", 35, 50, 60),
        ("Troll", 100, 15, 75)
    ]

# generate random monster
monster_list = ["Ogre", "Goblin", "Troll"]
random_monster = random.choice(monster_list)
print(random_monster)


def player_attack():
    pass
    
def player_defend():
    pass
    
def player_heal():
    pass
    
def attack(self, xxxxxxxx):
    pass

def is_alive(self):
    pass



#if __name__ == "__main__":
   # game()
