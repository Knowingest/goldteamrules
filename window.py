'''Example template'''


import sys
from encounter import encounter,baddie,player
from PyQt5 import QtWidgets, QtGui, QtCore
import enemy

class Window(QtWidgets.QWidget):

	def __init__(self):
		QtWidgets.QWidget.__init__(self)
		self.width=888
		self.height=684
		self.setup()
		
	def setup(self):
		self.setGeometry(10,10,self.width,self.height)
		self.setWindowTitle("Testing")
		self.p = Painting(self)
		self.show()
		
		
class Painting(QtWidgets.QWidget):
	def __init__(self, parent):
		QtWidgets.QWidget.__init__(self,parent)
		#self.lay = QtWidgets.QWidget()
		#self.grid = QtWidgets.QGridLayout()
		self.bg = "intro"
		self.prev = "lol"
		
		self.width=888
		self.height=684
		self.setFixedSize(self.width,self.height)
		self.setup()
		
	def setup(self):
		self.butt = QtWidgets.QPushButton("Start Game",self)
		self.butt.move(400,400)
		self.butt.clicked.connect(self.firstArea)
		self.forbutt = QtWidgets.QPushButton("Up", self)
		self.backbutt = QtWidgets.QPushButton("Backwards", self)
		self.kamikaze = QtWidgets.QPushButton("Down", self)
		self.buttcleaner()
		self.encs=1

	def paintEvent(self, event):
		
		qp = QtGui.QPainter()
		qp.begin(self)
			
		pen = qp.pen()
		pen.setColor(QtCore.Qt.transparent)
		qp.setPen(pen)
			
		bush = QtGui.QBrush()
		if self.bg =="first":
			bush.setTextureImage(QtGui.QImage("background1.png"))
		elif self.bg=="second":
			bush.setTextureImage(QtGui.QImage("background2.png"))
		elif self.bg=="third":
			bush.setTextureImage(QtGui.QImage("background3.png"))
		elif self.bg=="fourth":
			bush.setTextureImage(QtGui.QImage("background4.png"))
		elif self.bg=="fifth":
			bush.setTextureImage(QtGui.QImage("background5.png"))
		elif self.bg=="sixth":
			bush.setTextureImage(QtGui.QImage("background6.png"))
		elif self.bg=="intro":
			bush.setTextureImage(QtGui.QImage("startscreen.png")
		else: 
			bush.setTextureImage(QtGui.QImage("bigarena.png"))
			
		qp.setBrush(bush)
			
		qp.drawPolygon(QtCore.QPoint(0,0), QtCore.QPoint(0,684),QtCore.QPoint(888,684),QtCore.QPoint(888,0))
			
		qp.end()
	def buttcleaner(self):
		self.backbutt.hide()
		self.forbutt.hide()
		self.kamikaze.hide()
	
	def arenaArea(self,event):
		self.update()
	
	def firstArea(self,event):
		self.bg = "first"
		self.prev = "intro"
		self.butt.setParent(None)
		self.update()
		self.buttcleaner()
		
		self.forbutt.move(0,0)
		self.forbutt.clicked.connect(self.secondArea)

		self.forbutt.show()
		self.prev = "first"
		if encs ==1:
			self.fight(1)
			self.bg="fight"
			self.update()
			self.encs+=1

	def secondArea(self,event):
		self.bg = "second"	
		self.buttcleaner()
		self.backbutt.move(20,20)
		self.backbutt.clicked.connect(self.firstArea)
		
		self.forbutt.move(80,80)
		self.forbutt.clicked.connect(self.thirdArea)
		
		self.backbutt.show()
		self.forbutt.show()

		self.show()
		self.update()
		self.prev = "second"
		if encs ==2:
			self.fight(2)
			self.bg="fight"
			self.update()
			self.encs+=1
	
	def thirdArea(self,event):
		self.bg = "third"
		self.buttcleaner()
		self.backbutt.move(0,0)
		self.backbutt.clicked.connect(self.secondArea)

		self.forbutt.move(25,25)
		self.forbutt.clicked.connect(self.fourthArea)

		self.kamikaze.move(127, 127)
		self.kamikaze.clicked.connect(self.fifthArea)

		self.backbutt.show()
		self.forbutt.show()
		self.kamikaze.show()

		'''need to do encounter counter
		when = 4'''

		self.show()
		self.update()
		self.prev = "third"
		if encs ==3:
			self.fight(3)
			self.bg="fight"
			self.update()
			self.encs+=1
	
	def fourthArea(self,event):
		self.bg = "fourth"	
		self.buttcleaner()
		self.backbutt.move(300,300)
		self.backbutt.clicked.connect(self.thirdArea)

		self.backbutt.show()

		self.show()
		self.update()
		self.prev = "fourth"
		if self.encs ==4:
			self.fight(4)
			self.bg="fight"
			self.update()
			self.encs+=1

	def fifthArea(self,event):
		self.bg = "fifth"		
		self.buttcleaner()
		self.backbutt.move(14,14)
		self.backbutt.clicked.connect(self.thirdArea)
		
		self.forbutt.move(129,129)
		self.forbutt.clicked.connect(self.sixthArea)

		self.backbutt.show()
		self.forbutt.show()
		if self.encs ==5:
			self.encs+=1
		self.show()
		self.update()
		self.prev = "fifth"
	
	def sixthArea(self,event):
		self.bg = "sixth"	
		self.buttcleaner()	
		self.backbutt.move(84,84)
		self.backbutt.clicked.connect(self.fifthArea)

		self.backbutt.show()
		if self.encs ==6:
			self.fight(6)
			self.bg="fight"
			self.update()
			self.encs+=1
		self.show()
		self.update()
		self.prev = "sixth"
		
	def fight(self, room):
		b = list()
		counter=0
		ilia = player(20)
		arena = encounter(ilia, b)
		ens=5
		#append enemies
		if room==1:
			b.append(blub())
		elif room==2:
			#blub and 2 others
			b.append(blub())
			b.append(blub())
			b.append(snek())
		elif room==3:
			#5 enemies
			b.append(snek())
			b.append(spooder())
			b.append(skullitor())
			b.append(blub())
			b.append(blub())
		elif room==4:
			#big blub and 4 other enemies
			b.append(bigblub())
			b.append(snek())
			b.append(snek())
			b.append(skullitor())
			b.append(blub())
		elif room==6:
			#mother and 4 other enemies
			b.append(mother())
			b.append(snek())
			b.append(skullitor())
			b.append(blub())
			b.append(spooder())
		charge=False
		damage = 0
		while ens !=0:
			arena.print_board()
			if(count%2==0):
				#Ilia's turn
				#ask for input
				#Hard attack
				if charge==False:
					while charge==False:
						x = int(input("Light attack (1)---takes 1 turn/nHeavy Attack (2)---takes 2 turns"))
						#Light attack
						if x==1:
							damage = 5
							break
						elif x==2:
							charge=True
							damage = 15
							break
						else:
							print("Excuse?")
					ens=b.len()
						
					while True:
						y = int(input("Choose target: " ))#enemy array
						#error check
						if y > 0 and y <= ens:
							arena.take_turn(damage, (y-1))
							if b[y-1].hp<=0:
								del b[y-1]
							break
						else:
							print("Invalid input. Excuse?")
					
				else:
					print("Too tired to move this turn.")
					charge=False
				
			else:
				for i in b:
					ilia.hp -= i.taketurn()

				print("Enemy is taking a turn")
			count+=1
		
if __name__=="__main__":
	app = QtWidgets.QApplication(sys.argv)
	win = Window()
	app.exec_()
