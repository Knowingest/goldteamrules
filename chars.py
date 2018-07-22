# Notes:
# 	Comments are for ideas and explination if needed
# 	Most things are self explanitory
# 	To-Do at bottom
#  Most print statment are for error checking

import random
import sys
from enemy import *
from taketurn import *

class player(object):
	def __init__(self):
		self.hp = 20
		self.def_hp = random.randint(1,2) #changed from 0,2 cause val of 0 was possible
		self.atk_hp = random.randint(1,3)


def startMenu():
	print("Welcome to --insert game name here--")
	print("N - (N)ew game")
	print("L - (L)oad game")

if __name__ == "__main__":
	startMenu()
	i = input().lower()
	if i == 'n':
		Hero = player()
	elif i == 'l':
		0 # take in values from file to assign as hp, def, point in story?
	elif i == 's':
		showStats() #show stats feature?

	#takeTurn(Hero, 0) #if there is no enemy then use 0 to take turn of moving around map

	BadE1= mother()
	BadE2= mother()
	BadE3= mother()
	BadETeam = []
	BadETeam = [BadE1,BadE2,BadE3]
	check = takeTurn(Hero, BadETeam) 	# we stay at this line in main until enemy is dead or hero dies,
										# you dont need to recall taketurn more than once for the same enemy
	if check == 1: # check if dead
		del Hero # if died del all characters
		for x in BadETeam:
			del x
		del BadETeam
		startMenu()

	#continue on with the story

	exit(0)

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

