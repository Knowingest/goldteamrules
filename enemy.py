import random

class enemy(object):
    def __init__(self, _hp=10, _atk_hp=random.randint(1, 3), _def_hp=random.randint(1, 2)):
        self.hp = _hp
        self.atk_hp = _atk_hp
        self.def_hp = _def_hp


class blub(object):
    def __init__(self):
        self.name = "Blub"
        # attr = enemy(hp, atk, def)
        self.attr = enemy(random.randint(1,3), random.randint(1,2), random.randint(0,2))
        self.quote = "Woof"
        self.attack1 = "Blub uses squish!"
        self.attack2 = "Blub throws a gelatinous glob!"

class bigblub(object):
    def __init__(self):
        self.name = "Big Blub"
        self.attr = enemy(random.randint(7, 9), random.randint(1, 2), random.randint(2, 3))
        self.quote = "Woof"
        self.attack1 = self.name + " uses squish!"

class spooder(object):
    def __init__(self):
        nameList = ["Spooder", "Spidey", "Spider"]
        self.name = random.choice(nameList)
        self.attr = enemy(random.randint(5, 8), random.randint(4, 5), random.randint(1, 2))
        self.quote = "Woof"
        self.attack1 = self.name + " uses poison!"

class snek(object):
    def __init__(self):
        nameList = ["Snek", "Snake", "Danger Noodle"]
        self.name = random.choice(nameList)
        self.attr = enemy(random.randint(3, 5), random.randint(2, 4), random.randint(2, 3))
        self.quote = "Woof"
        self.attack1 = self.name + " bites you!"

class skullitor(object):
    def __init__(self):
        nameList = ["Skullitor", "Creepy Skull", "Skull"]
        self.name = random.choice(nameList)
        self.attr = enemy(random.randint(6, 9), random.randint(5, 8), random.randint(1, 3))
        self.quote = "Woof"
        self.attack1 = self.name + " casts a fire spell at you!"

class mother(object):
    def __init__(self):
        self.name = "Mother"
        self.attr = enemy(random.randint(13, 15), random.randint(2, 4), random.randint(6, 9))
        self.quote = "Woof"
        self.attack1 = "Mother beats you with a belt!"
        self.attack2 = "Mother looks disappointingly you!"
