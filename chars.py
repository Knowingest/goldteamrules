# Notes:
# 	Comments are for ideas and explination if needed
# 	Most things are self explanitory
# 	To-Do at bottom
#  Most print statment are for error checking

import random
import sys

class enemy(object):
	def __init__(self):
		self.hp = 10
		self.is_dead = False
		self.atk_hp = self.atk()
		self.defe_hp = self.defe()
#		self.check = print("World")
	def atk(self):
		x = random.randint(1,3)
		return x
		
	def defe(self):
		y = random.randint(1,2)
		return y


		# damage taken = atk - def

class player(object):
	def __init__(self):
		self.is_dead = False
		self.hp = 20
		self.defe_hp = self.defe()
		self.atk_hp = self.atk()
#		self.check = print("Hello") 	# check
	def atk(self):
		x = random.randint(0,3)
		return x
		
	def defe(self):
		y = random.randint(0,2)


if __name__ == "__main__":
	Hero = player()
	BadE = enemy()
#	print("FooBar")	# check	
	while(True):
		print("--- NEW RUN ---")
		a = Hero.atk_hp
		b = BadE.defe_hp
		print("Hero ATK -> " , a)
		print("BadE DEF -> " , b)
		print("BadE HP -> " , BadE.hp)
		print("Hero HP -> " , Hero.hp)

#	while(True):
		if(Hero.hp <= 0):
			print("BadE wins??")
			break
		if(BadE.hp <= 0):
			print("Hero wins!!")
			break
		print("BadE_HP -> " , BadE.hp)
		print("Hero ATK -> " , a)
		print("BadE DEF -> " , b)
		BadE.hp = a - b		# this does bad math?
		print("BadE_HP -> " , BadE.hp)
	sys.exit()

# In main: 
#  -> BadE[enemy() for i in range(0,//random number))] to set the number of enemys
#  -> Fix the random infinity loop
#  -> Get the atk and def to rerandom every loop
#  
# In General:
#	-> Add menu to make for interactive
#	-> Refine and make visually better
#
#
#
