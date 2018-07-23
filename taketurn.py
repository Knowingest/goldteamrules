def showStats(Hero, BadETeam):
	print("My HP:     " + str(Hero.hp))
	print("My Atk:    " + str(Hero.atk_hp))
	print("My Def:    " + str(Hero.def_hp))
	i = 1
	for x in BadETeam:
		print("-----Enemy #" + str(i) + "-----")
		print(str(x.name) + " HP:  " + str(x.attr.hp))
		print(str(x.name) + " Atk: " + str(x.attr.atk_hp))
		print(str(x.name) + " Def: " + str(x.attr.def_hp))
		i += 1

def takeTurn(Hero, BadETeam):
    if (BadETeam == 0):  # if there is no enemy do we move?
        i = input("Move (N)orth, (W)est, (E)ast, or (S)outh").lower()
        if i == 'n':
            print("You follow a path north")
        elif i == 'w':
            0
        elif i == 'e':
            0
        elif i == 's':
            0

        return 0

    else:  # a fight
        j = 0 # index+1 of which enemy you will fight
        i = input("(A)ttack, (D)efend, (R)un, use (I)tem, (S)how stats").lower()  # .lower makes input letter lowercase
        if i == "a":
            if len(BadETeam) > 1:
                while (True):
                    j = input("Which enemy would you like to hit?")
                    j = int(j)
                    if j > 0 and j <= len(BadETeam):
                        break;
                    else:
                        print("Please pick a number 1 through " + str(len(BadETeam)))
            else:
                j = 1

            # enemy j takes damage
            if Hero.atk_hp > BadETeam[j-1].attr.def_hp: # right now if attack is less than def then monster will only take 1 damage
                BadETeam[j-1].attr.hp -=  Hero.atk_hp - BadETeam[j-1].attr.def_hp

                # check if enemy j dies, if doesnt then print damage value
                if BadETeam[j - 1].attr.hp <= 0:
                    print(BadETeam[j - 1].name + " dies!")
                    del BadETeam[j - 1]
                else:
                    print(BadETeam[j - 1].name + " takes " + str(
                        Hero.atk_hp - BadETeam[j - 1].attr.def_hp) + " points of damage!")
            else:
                BadETeam[j-1].attr.hp -= 1

                # check if enemy j dies, if doesnt then print damage value
                if BadETeam[j - 1].attr.hp <= 0:
                    print(BadETeam[j - 1].name + " dies!")
                    del BadETeam[j - 1]
                else:
                    print(BadETeam[j - 1].name + " takes 1 point of damage!")


            #enemy team attacks hero
            for x in BadETeam:
                if x.attr.atk_hp > Hero.def_hp: # right now if attack is less than def then hero will not take damage
                    Hero.hp -= x.attr.atk_hp - Hero.def_hp
                    print(x.attack1)
                    print(x.name + " deals " + str(x.attr.atk_hp - Hero.def_hp) + " damage to you!")
                else:
                    print(x.attack1)
                    print(x.name + " fails to damage you!")


        elif i == "d":
            print("Defence logic not implemented") # use defense logic here if u have it or delete this conditional
        elif i == "r":
            print("run logic not implemented") # use a random num maybe as a conditional on how tough the enemy is
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