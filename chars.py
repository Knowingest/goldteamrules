# Notes:
# 	Comments are for ideas and explination if needed
# 	Most things are self explanitory
# 	To-Do at bottom
#  Most print statment are for error checking

import random
from enemy import *
from taketurn import *


class player(object):
    def __init__(self):
        self.hp = 20
        self.def_hp = random.randint(1, 2)
        self.atk_hp = random.randint(2, 3)
        #self.exp = 0
        #self.level = 0
        #self.inventory = []

def startMenu():
    print("Welcome to --insert game name here--")
    print("N - (N)ew game")
    print("L - (L)oad game")
    print(">: ", end="")


def randEnemyGen():
    numenemy = random.randint(1,5)
    enemyList = []
    choiceList = ["Spider", "Blub", "Snek", "Skull"]
    for x in range(0,numenemy):
        enemy = random.choice(choiceList)
        if enemy == "Blub":
            Baddy = blub()
            enemyList.append(Baddy)
        elif enemy == "Spider":
            Baddy = spooder()
            enemyList.append(Baddy)
        elif enemy == "Snek":
            Baddy = snek()
            enemyList.append(Baddy)
        elif enemy == "Skull":
            Baddy = skullitor()
            enemyList.append(Baddy)
        else:
            print("Fail at line 29 chars.py")

    return enemyList

if __name__ == "__main__":
    startMenu()
    i = input().lower()
    if i == 'n':
        Hero = player()
    elif i == 'l':
        0  # take in values from file to assign as hp, def, point in story?
    elif i == 's':
        showStats()

    # BadE1 = mother()
    #BadE2 = bigblub()
    #BadETeam = [BadE1, BadE2, BadE3, BadE4]
    BadETeam = randEnemyGen()
    #BadETeam = [BadE2]
    check = takeTurn(Hero, BadETeam)    # we stay at this line in main until enemy is dead or hero dies,
                                        # you dont need to recall taketurn more than once for the same enemy
    if check == 1:  # check if dead
        del Hero  # if died del all characters
        for x in BadETeam:
            del x
        del BadETeam
        startMenu()
    else: # not dead
        del BadETeam

    # continue on with the story


    # end boss
    # print("Mother Apears!")
    # BadE1 = mother()
    # BadETeam = [BadE1]
    # check = takeTurn(Hero, BadETeam)
    # if check == 1:
    #     del Hero
    #     for x in BadETeam:
    #         del x
    #     del BadETeam
    #     startMenu()

    print("You beat the game!")
    exit(0)