import random

class Player:
    def __init__(self, name, max_health, health, max_strength, strength, special):
        self.name = name
        self.max_health = max_health
        self.health = health
        self.max_strength = max_strength
        self.strength = strength
        self.special = special
p1 = Player("HERO", 100, 87, 100, 90, 10)
print(p1.name)
print(p1.max_health)
print(p1.health)
print(p1.max_strength)
print(p1.strength)
print(p1.special)

print("\n")

class Monster:
    def __init__(self, name, max_health, health, max_strength, strength, special):
        self.name = name
        self.max_health = max_health
        self.health = health
        self.max_strength = max_strength
        self.strength = strength
        self.special = special
m1 = Monster("Ogre", 50, 45, 200, 176, 1)
print(m1.name)
print(m1.max_health)
print(m1.health)
print(m1.max_strength)
print(m1.strength)
print(m1.special)
print("\n")
m2 = Monster("Goblin", 25, 22, 15, 10, 1)
print(m2.name)
print(m2.max_health)
print(m2.health)
print(m2.max_strength)
print(m2.strength)
print(m2.special)
print("\n")
m3 = Monster("Troll", 30, 25, 35, 35, 5)
print(m3.name)
print(m3.max_health)
print(m3.health)
print(m3.max_strength)
print(m3.strength)
print(m3.special)

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

# Randomly select monster
generate_monster = ["m1", "m2", "m3"]
print(random.choice(generate_monster))

# So you will want to store both the name and the healh as a result from the random.choice.
 
# Ok this is a new function to generate a room... we are going to use an array again.
# create an array of strings. Each string will be the name of the room. So you could have a "cave" or a "field" or a "castle" etc... get creative.
# you need then to randomize it... so you will use random.choice again. This will pick a random room from the array.
# then you need to return that value. This one should be simple after the ones above.
#def generate_room():

#return # remember this should be returning a string since the array is strings.


# Ok... now on the main function that runs the game.
# I left a lot of stuff here And I will try to explain it all. But I want you to problem solve.... this is a shell...
# You should have all your functions finished above before you even attempt to do this.
# Read it... review it... but I would wait until your got the functions looking good before attempting the below.
#def game():
   # print("Welcome to my game!")
    # Create an input here that takes in the players name. Then you will use it to create your player in the Player class.  There should be 2 lines of code below this.
    # The first link to take in the input and to set a variable.
    # the next line passes that value into the player class and creates the player. 
    # when you create your player... it works alot like an input variable. You will want to set it to a variable. Might I suggest using player with a lower case p.
    # then throughout this function you can use player to refer to the player class.

    #___________________________-
    # I am keeping this while loop here to give you an idea. The while loop will run as long as your player is alive.... 
    #while #player is alive
        # This is where your generates come in. The print statement runs the generate room... since the generate room is only returning a string (remember that array should be strings only)
        # you can just use the function inside of a string. So im keeping it here to show you how the rerturn can work.
        #print("\nYou enter " + generate_room() + ".")
        # Ok so on this line you want to generate your monster. I will let you figure out how to do that....
        #-------------------
        # The print statement below is an idea of what you can write... you can have fun with this anyway you want.
        # I left the {} brackets... this is where you will pull in your monster name and health. SO on the line above the break you generated your monster and SHOULD have set it to a value.
        # this is going to be a new topic for you.. how do you pull in the values from the monster you created.
       # print("A wild {} appears with {} health!")

        # Inside the top while loop... your going to run another while loop to check if BOTH the monster AND the player is alive....
        # I could not comment it out... so you need to fix it.
        #while monster is alive and player is alive: #you need to fix this line since i could not comment it out.
            # Ok... so inside this while loop will be your desison place for the player to deside what he wants to do... 
            # it is basically similar to the Printer function we made. 
            # there are 2 optinos for the player. He can attack... or he can heal. So you need to create your if, else if, and else statement here.
            # it should take in an input for the choice. 
            # if attack is selected. it should first have the player attack, so run the player.attack function. The player attack funciton takes in 1 value, which should be the monster.
            # It should then check if the monster is alive. If he is still alive, then the monster should attack the player back. Remember, when you built the monster attack above,
            # it should take in the player.
            # this is called a nested If statement.
            # now... else if you selected heal....
            # the player should heal. There is nothing that needs to be pased into heal.. remember it only took in self, so it is not needed.
            # however... the monster is still alive, and he gets his shot, so after the heal the monster should attack.
            # else... you selected an invaild option.

            # Finally before we close the while loop... we need to print the health of the player and the monster. This is so you can see what is happening.
            # To add to the challenge have it print out the player name and health, and the monster name and health.
            # so maybe something like:
            # "Brandon's health: 100"
            # "Monster's health: 30"

        # so now you are outside of the inner while loop.... You need to check if the player is alive.... 
        # I left the if statement for you...
       # if #Player is alive........
            #Print a death statement.... maybe include the monsters name you killed?
       # else:
            # You died..... print a death statement.

    # Ok so now you are outside of the while loop... this means the player is dead.... so you need to print a game over statement.
    # Remember the while loop runs as long as the player is alive. so it will be monster, after monsters after monster until the player dies....
    #print(  ) # Thanks for playing? Some type of print statement that lets the player know the game is over. 


#if __name__ == "__main__":
   # game()
