#retrofitted by Ricky D the G, saved by Dan the Man
import random

class blub(object):
    def __init__(self):
        self.name = "Blub"
        self.hp = random.randint(3,4)
        self.dmg = random.randint(1,2)
        self.msg = "Blub uses squish!"

    def take_turn(self):
        if self.hp < 3:
            x = random.randint(1, 2)
            if x == 1:
                self.hp += 1
                self.msg = "Blub is healing!"

class bigblub(object):
    def __init__(self):
        self.name = "Big Blub"
        self.hp = random.randint(1, 3)
        self.dmg = random.randint(1, 2)
        self.msg = "Blub uses squish!"

    def take_turn(self):
        if self.hp < 5:
            x = random.randint(1, 2)
            if x == 1:
                self.hp += 2
                self.msg = "Big Blub is healing!"


class spooder(object):
    def __init__(self):
        nameList = ["Spooder", "Spidey", "Spider"]
        self.name = random.choice(nameList)
        self.hp = random.randint(1, 3)
        self.dmg = random.randint(1, 2)
        self.msg = self.name + " uses poison!"

    def take_turn(self):
        x = random.randint(1, 3)
        if x == 1:
            self.msg = "You have been poisoned!"
            self.dmg += 1
        else:
            self.msg = self.name + " bites you!"

class snek(object):
    def __init__(self):
        nameList = ["Snek", "Snake", "Danger Noodle"]
        self.name = random.choice(nameList)
        self.hp = random.randint(1, 3)
        self.dmg = random.randint(1, 2)
        self.msg = self.name + " bites you!"

    def take_turn(self):
        x = random.randint(1, 3)
        if x == 1:
            self.msg = "You have been poisoned!"
            self.dmg += 2
        else:
            self.msg = self.name + " bites you!"

class skullitor(object):
    def __init__(self):
        nameList = ["Skullitor", "Creepy Skull", "Skull"]
        self.name = random.choice(nameList)
        self.hp = random.randint(1, 3)
        self.dmg = 0
        self.msg = self.name + " casts a fire spell at you!"

        self.counter = 0

    def take_turn(self):
        counter += 1
        if (counter == 3):
            self.dmg = random.randint(8, 12)
            self.msg = self.name + " casts a charged fire spell at you!"
        else:
            self.dmg = 0
            self.msg = self.name + " is charging an attack!"
            counter = 0

class mother(object):
    def __init__(self):
        self.name = "Mother"
        self.hp = random.randint(1, 3)
        self.dmg = random.randint(1, 2)
        self.msg = "Mother beats you with a belt!"

    def take_turn(self):
        if self.hp < 7:
            self.dmg *= 2