from enemy import blub
import random

def showStats(Hero, BadETeam):
	print("My HP:  " + str(Hero.hp))
	print("My Atk: " + str(Hero.atk_hp))
	print("My Def: " + str(Hero.def_hp))
	i = 1
	for x in BadETeam:
		print("-----Enemy #" + str(i) + "-----")
		print(str(x.name) + " HP:  " + str(x.attr.hp))
		print(str(x.name) + " Atk: " + str(x.attr.atk_hp))
		print(str(x.name) + " Def: " + str(x.attr.def_hp))
		i += 1

def takeTurn(Hero, BadETeam):
    check = True #for motherV2
    if (BadETeam == 0):  # if there is no enemy do we move?
        i = input("Move (N)orth, (W)est, (E)ast, or (S)outh\n>: ").lower()
        if i == 'n':
            print("You follow a path north")
        elif i == 'w':
            0
        elif i == 'e':
            0
        elif i == 's':
            00.

        return 0

    else: # a fight
        j = 0 # index+1 of which enemy you will fight
        i = input("(A)ttack, (D)efend, (R)un, use (I)tem, (S)how stats\n>: ").lower()  # .lower makes input letter lowercase
        if i == "a":
            if len(BadETeam) > 1:
                while (True):
                    j = input("Which enemy would you like to hit? (1-" + str(len(BadETeam)) + ")\n>: ")
                    j = int(j)
                    if j > 0 and j <= len(BadETeam):
                        break;
                    else:
                        print("Please pick a number 1 through " + str(len(BadETeam)))
            else:
                j = 1

            # enemy j takes damage
            if Hero.atk_hp > BadETeam[j-1].attr.def_hp: # right now if attack is less than def then monster will only take 1 damage
                damage =  Hero.atk_hp - BadETeam[j-1].attr.def_hp + random.randint(0,2)
                BadETeam[j - 1].attr.hp -= damage
                print(BadETeam[j - 1].name + " takes " + str(damage) + " points of damage!")

                # check if enemy j dies, if doesnt then print damage value
                if BadETeam[j - 1].attr.hp <= 0:
                    # for bigblub
                    if BadETeam[j - 1].name == "Big Blub":
                        print("Big Blub splits!")
                        blub1 = blub()
                        blub2 = blub()
                        BadETeam.append(blub1)
                        BadETeam.append(blub2)

                    print(BadETeam[j - 1].name + " dies!")
                    del BadETeam[j - 1]
                else:

                    #motherV2
                    if BadETeam[j - 1].name == "Mother" and BadETeam[j - 1].attr.hp < 5 and check:
                        BadETeam[j - 1].attr.hp += 10
                        BadETeam[j - 1].attr.def_hp += 2
                        BadETeam[j - 1].attr.atk_hp += 2
                        print("Mother is evolving!")
                        check = False
            else: # if hero atk <= enemy.def
                damage = random.randint(0,1)
                if damage == 1:
                    BadETeam[j-1].attr.hp -= damage

                    # check if enemy j dies, if doesnt then print damage value
                    if BadETeam[j - 1].attr.hp <= 0:
                        # for bigblub
                        print(BadETeam[j - 1].name + " takes 1 point of damage!")

                        if BadETeam[j - 1].name == "Big Blub":
                            print("Big Blub splits!")
                            blub1 = blub()
                            blub2 = blub()
                            BadETeam.append(blub1)
                            BadETeam.append(blub2)

                        print(BadETeam[j - 1].name + " dies!")
                        del BadETeam[j - 1]
                    else:
                        print(BadETeam[j - 1].name + " takes 1 point of damage!")
                else:
                    print("You missed")




            #enemy team attacks hero
            for x in BadETeam:
                if x.attr.atk_hp > Hero.def_hp: # right now if attack is less than def then hero will not take damage
                    damage = x.attr.atk_hp - Hero.def_hp + random.randint(-1,1)
                    Hero.hp -= damage
                    print(x.attack1)
                    print(x.name + " deals " + str(damage) + " damage to you!")
                else:
                    print(x.attack1)
                    print(x.name + " fails to damage you!")


        elif i == "d":
            print("Defence logic not implemented") # use defense logic here if u have it or delete this conditional
        elif i == "r":
            tothealth = 0
            bool1 = False
            for x in BadETeam:
                tothealth += x.attr.hp
                if x.name == "Mother" or x.name == "Big Blub" or x.name == "Blub's older brother" or x.name == "Blub, but bigger":
                    bool1 = True

            if bool1 or tothealth > 20:
                print("Failed to run away")
            else:
                print("Escaped Successfully")
                return 0
        elif i == "i":
            print("item logic not implemented") # items?
        elif i == "s":
            showStats(Hero, BadETeam)

    if Hero.hp < 1:
        print("You Died")
        return 1
    elif len(BadETeam) == 0:
        print("Enemy Team Defeated!")
        return 0

    return takeTurn(Hero, BadETeam) #recursive until enemy is dead or hero is dead