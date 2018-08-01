import sys

#Important information:
#		encounter class:
#				takes parameters player_hp, and enemy_number
#		encounter.print_board():
#				prints board information

class baddie(): #stand-in enemy class
	def __init__(self):
		self.dmg = 0
		self.hp = 5
		self.msg = "Baddie does nothing"

	def take_turn(self): 
		self.dmg = 1
		self.msg = "Baddie uses Slap!"

class player(): #stand in player class
	def __init__(self, hp):
		self.hp = hp
		self.atk1 = 3

class encounter(): #basically, all combat will occur inside an instance of this class

				#we input current player hp and a list of enemies
	def __init__(self, player, enemy_list):
		self.enemy_team = enemy_list
		self.p1 = player

				#prints board information to console
				#this is mostly used for testing
	def print_board(self):
		print("********")
		for i in range(0, len(self.enemy_team)):
			if self.enemy_team[i].hp < 1:
				sys.stdout.write("XX ")
				sys.stdout.flush()
			else:
				sys.stdout.write("E" + str(i + 1) + " ")
				sys.stdout.flush()

		print("\nP1")
		print("********")

		for i in range(0, len(self.enemy_team)):
			if (self.enemy_team[i].hp > 0):
				print("E" + str(i + 1) + " HP = " + str(self.enemy_team[i].hp))

		print("Player HP = " + str(self.p1.hp))


		#dmg and target represent who the player will hit, and how much damage it deals
			#calling take_turn() with appropriate arguments is how we control the player
	def take_turn(self, dmg, target):
		self.enemy_team[target].hp -= dmg

		for e in self.enemy_team:
			if e.hp > 0:
				#e.take_turn()
				self.p1.hp -= e.dmg



				#this main function is just for testing purposes
if __name__ == "__main__":
	b = list()
	for x in range(5):
		b.append(baddie())
	p = player(20)
	test = encounter(p, b)
	#for dude in test.enemy_team:
	#	print(dude.hp)


		#print board, kill a dude, print board again
	test.print_board()
	test.take_turn(5, 1)
	test.print_board()
	test.take_turn(5, 3)
	test.print_board()
