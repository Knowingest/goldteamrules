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
	def print_board(self):
		print("********")
		for i in range(0, len(self.enemy_team)):
			if self.enemy_team[i].hp < 1:
				print("XX", end = " ")
			else:
				print("E" + str(i + 1), end = " ")

		print("\nP1")
		print("********")

		for i in range(0, len(self.enemy_team)):
			if (self.enemy_team[i].hp > 0):
				print("E" + str(i + 1) + " HP = " + str(self.enemy_team[i].hp))

		print("Player HP = " + str(self.p1.hp))

	def take_turn(self, move, target):
		if move == 1:
			self.enemy_team[target].hp -= self.p1.atk1

		for e in self.enemy_team:
			if e.hp > 0:
				e.take_turn()
				self.p1.hp -= e.dmg




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
	test.take_turn(1, 2)
	test.print_board()
	test.take_turn(1, 2)
	test.print_board()

