# Comments are for ideas
# and explination if needed
# most things are self explanitory

class enemy(object):
	def __init__(self):
		self.hp = 5
		self.is_dead = False

		# for attking make another function
		# return dmg output
		# set to 0 and then make random from 0-5
		# befor attacking
		# random number 0 would be a miss
		self.atk = 1
		# self.def = 1
		# damage taken = atk - def

class player(object):
	def __init__(self):
		self.is_dead = False
		self.hp = 20
		# set to 0 and then make random from 0-5
		# random number 0 would be a miss
		# for attking make another function
		# return dmg output
		self.atk = 2 
		# self.def = 1
		# damage taken = atk - def

# in main can do something like 
#  badG[enemy() for i in range(0,//random number))]
# 	to set the number of enemys
#  the something like 
#	hero = player()
