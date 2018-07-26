import random

class blub(object):
	 def __init__(self):
		  self.name = "Blub"
		  self.hp = random.randint(3,4)
		  self.dmg = random.randint(1,2)
		  self.msg = "Blub uses squish!"
		  self.counter = 0

	 def take_turn(self):
		  self.counter += 1
		  if (self.counter == 1):
				self.dmg = random.randint(1, 3)
				self.msg = self.name + "Hit!"
	if (self.counter == 2):
		self.hp += 1
		self.msg = "Blub is healing!"
		self.counter = 0

class bigblub(object):
	 def __init__(self):
		  self.name = "Big Blub"
		  self.hp = random.randint(1, 3)
		  self.dmg = random.randint(1, 2)
		  self.msg = "Blub uses squish!"
		  self.counter = 0

	 def take_turn(self):
		   if self.hp < 5:
				x = random.randint(1, 2)
				if x == 1:
					 self.hp += 2
					 self.msg = "Big Blub is healing!"
		 
			self.counter += 1
		   if (self.counter == 1):
				self.dmg = random.randint(2, 4)
				self.msg = self.name + "Hit softly!"
			if (self.counter == 2):
				self.dmg = random.randint(2, 4)
				self.msg = self.name + "Hit softly!"
			if (self.counter == 3):
				self.dmg = 0
				self.msg = self.name + " is charging an attack!" 
		   if (self.counter == 4):
				self.dmg = random.randint(8, 12)
				self.msg = self.name + " Hit hard!"
				self.counter = 0


class spooder(object):
	 def __init__(self):
		  nameList = ["Spooder", "Spidey", "Spider"]
		  self.name = random.choice(nameList)
		  self.hp = random.randint(1, 3)
		  self.dmg = random.randint(1, 2)
		  self.msg = self.name + " uses poison!"
		  self.counter = 0

	 def take_turn(self):
	 	self.counter += 1
		if (self.counter == 1):
			self.dmg = random.randint(1, 3)
			self.msg = self.name + " bites you!"
			x = random.randint(1, 3)
				if x == 1:
					self.msg = "You have been poisoned!"
						self.dmg += 1
			self.counter = 0
class snek(object):
	def __init__(self):
		nameList = ["Snek", "Snake", "Danger Noodle"]
		self.name = random.choice(nameList)
		self.hp = random.randint(1, 3)
		self.dmg = random.randint(1, 2)
		self.msg = self.name + " bites you!"

	def take_turn(self):
		self.counter += 1
		if (self.counter == 1):
			self.dmg = random.randint(1, 6)
			self.msg = self.name + " flung rock!"
		if(self.dmg > 3)
			self.hp -= random.randint(1, 2)
		self.counter = 0

class skullitor(object):
	def __init__(self):
		nameList = ["Skullitor", "Creepy Skull", "Skull"]
		self.name = random.choice(nameList)
		self.hp = random.randint(1, 3)
		self.dmg = 0
		self.msg = self.name + " casts a fire spell at you!"
		self.bool = False
		self.counter = 0

	def take_turn(self):
		if(self.bool == True)
			self.dmg += 1
		self.counter += 1
		if (self.counter == 3):
			self.dmg = random.randint(8, 12)
			self.msg = self.name + " casts a charged fire spell at you!"
			self.msg = "You have been bured!"
			self.bool = True
			self.counter = 0
		else:
			self.dmg = 0
			self.msg = self.name + " is charging an attack!"
				
class mother(object):
	def __init__(self):
		self.name = "Mother"
		self.hp = random.randint(1, 3)
		self.dmg = random.randint(1, 2)
		self.msg = "Mother beats you with a belt!"
		self.counter = 0

	 def take_turn(self):
		 if (self.hp < 7):
		 	 self.dmg *= 2
		    self.counter += 1
		 if (self.counter == 1):
			 self.dmg = random.randint(2, 4)
			 self.msg = self.name + "Hit softly!"
		 if (self.counter == 2):
			 self.dmg = random.randint(2, 4)
			 self.msg = self.name + "Hit softly!"
		 if (self.counter == 3):
			 self.dmg = 0
			 self.msg = self.name + " is charging an attack!" 
		 if (self.counter == 4):
			 self.dmg = random.randint(8, 12)
			 self.msg = self.name + " Hit hard!"
		 if (self.counter == 5):
			 self.hp += 10
			 self.msg = self.name + "Healed self!"
		 if (self.counter == 6):
			 self.dmg = 0
			 self.msg = self.name + " is charging an attack!" 
		 if (self.counter == 7):
			 self.dmg = 0
			 self.msg = self.name + " is charging an attack, WATCH OUT!" 
		 if (self.counter == 8):
			 self.dmg = interger(max)
			 self.msg = self.name + " INSTA KILLED YOU !"
