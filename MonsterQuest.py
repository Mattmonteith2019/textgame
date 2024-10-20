import random


class Player:
    def __init__(self, name, health, strength, special):
        self.name = name
        self.health = health

        # Delete these for now and delete theme  in the init too... we can come back to this later.
        self.strength = strength
        self.special = special

    # each class gets its own functions... so you can delete these for now and come back to them later.
    def attack():
        pass

    def health():
        pass


# go ahead and delete these too
p1 = Player("HERO", 100, 100, 10)
print(p1.name)
print(p1.health)
print(p1.strength)
print(p1.special)

print("\n")


class Monster:
    def __init__(self, name, health, strength, special):
        self.name = name
        self.health = health

        # delete these and also from the init.
        self.strength = strength
        self.special = special


def generate_monster():
    # ok so this is just taking the your monster class and assigning the attribues. since you will remove strengh and special
    #  you only need the name and health so i removed the rest.  You did great with this otherwise.
    monster_types = [
        ("Ogre", 25),
        ("Goblin", 35),
        ("Troll", 100),
    ]
    # So you set up your monster type... those are already created.. so now you want t be able to randomly choose one.
    # so we set up the variables... you saying take the name and the health...  and using the monster_types go randomly generated one. from the monster_stype
    name, health = random.choice(monster_types)
    # so now we take a return statement. So this is a function... when you run this funciton it will return this class....
    # so think of it working like this. You set up monster types, you told the random class aboveo to go randomly choose one of the monster types
    # set the first value to name, and the second value to health. Which are INPUTs of your monster class.
    # then we say now that we set name and health, go set those values to the monster class and return it.
    return Monster(name, health)


##### This is great! but im going to comment out your code, and show you what to do and explain.....
# generate random monster
# monster_list = ["Ogre", "Goblin", "Troll"]
# random_monster = random.choice(monster_list)
# print(random_monster)

# im going ot move this..so delete these look at what i did in the player.....
# def player_attack():
#    pass


# def player_defend():
#    pass


# def player_heal():
#    pass


# def attack(self, xxxxxxxx):
#   pass


# def is_alive(self):
#    pass

# Now do something similar to generate room, that we did with the genereate monster.
# except you dont need to return a class.
# Just ---- return random.choice(your room)
# try this one on your own.....


# if __name__ == "__main__":
# game()
