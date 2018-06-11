#Important information:
#		encounter class:
#				takes parameters player_hp, and enemy_number
#		encounter.print_board():
#				prints board information





class baddie(): #stand in enemy class
	def __init__(self):
		self.hp = 5
		self.is_dead = False

class player(): #stand in player class
	def __init__(self, hp):
		self.hp = hp

class encounter(): #basically, all combat will occur inside an instance of this class

				#we input current player hp and how many enemies we want
	def __init__(self, player_hp, enemy_number):
		self.enemy_team = list()
		self.p1 = player(player_hp)
		for x in range(0, enemy_number):
			self.enemy_team.append(baddie())


				#prints board information to console
	def print_board(self):
		print("********")
		for i in range(0, len(self.enemy_team)):
			if self.enemy_team[i].is_dead == True:
				print("XX", end = " ")
			else:
				print("E" + str(i + 1), end = " ")

		print("\nP1")
		print("********")

		for i in range(0, len(self.enemy_team)):
			if (self.enemy_team[i].is_dead == False):
				print("E" + str(i + 1) + " HP = " + str(self.enemy_team[i].hp))

		print("Player HP = " + str(self.p1.hp))

if __name__ == "__main__":
	test = encounter(20, 4)
	#for dude in test.enemy_team:
	#	print(dude.hp)


		#print board, kill a dude, print board again
	test.print_board()
	print()
	test.enemy_team[1].is_dead = True
	test.p1.hp = 13
	test.print_board()


