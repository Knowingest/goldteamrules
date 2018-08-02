import sys
import random
# Important information:
# encounter class:
#  takes parameters player_hp, and enemy_number
# encounter.print_board():
#  prints board information


class player(object):  # stand in player class
    def __init__(self, hp):
        self.hp = hp
        self.atk1 = 3


class encounter(object):  # basically, all combat will occur inside an instance of this class

    # we input current player hp and a list of enemies
    def __init__(self, player, enemy_list):
        self.enemy_team = enemy_list
        self.p1 = player

        # prints board information to console
        # this is mostly used for testing

    def print_board(self):
        print("********")
        for i in range(0, len(self.enemy_team)):
            if self.enemy_team[i].hp < 1:
                sys.stdout.write("XX ")
                sys.stdout.flush()
            else:
                sys.stdout.write(self.enemy_team[i].name + " ")
                sys.stdout.flush()

        print("\nP1")
        print("********")

        for i in range(0, len(self.enemy_team)):
            if (self.enemy_team[i].hp > 0):
                print(self.enemy_team[i].name + " HP = " + str(self.enemy_team[i].hp))

        print("Player HP = " + str(self.p1.hp))

        # dmg and target represent who the player will hit, and how much damage it deals
        # calling take_turn() with appropriate arguments is how we control the player

    def take_turn(self, dmg, target):
        self.enemy_team[target].hp -= dmg
        if dmg == 7 or dmg == 16:
            print("You CRIT!\n" + "You deal " + str(dmg) + " damage to " + self.enemy_team[target].name)
        elif dmg == 0:
            print("You take a moment to catch your breath... \nBut the enemy attacks nonetheless!")
        else:
            print("You deal " + str(dmg) + " damage to " + self.enemy_team[target].name)
        if self.enemy_team[target].hp <= 0:
            print("You " + random.choice(["destroy ", "kill ", "obliviate "]) + self.enemy_team[target].name)
        for e in self.enemy_team:
            if e.hp > 0:
                e.take_turn()
                self.p1.hp -= e.dmg

        return self.p1.hp <= 0
