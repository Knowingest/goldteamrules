'''Example template'''


import sys
from PyQt5 import QtWidgets, QtGui, QtCore

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
		#self.grid.addWidget(self.butt,1,1)
		#self.lay.setLayout(self.grid)

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
		else: #self.bg=="arena":
			bush.setTextureImage(QtGui.QImage("bigarena.png"))
			
		qp.setBrush(bush)
			
		qp.drawPolygon(QtCore.QPoint(0,0), QtCore.QPoint(0,684),QtCore.QPoint(888,684),QtCore.QPoint(888,0))
			
		qp.end()
	
	def arenaArea(self,event):
		self.update()
	
	def firstArea(self,event):
		self.bg = "first"
		self.prev = "intro"
		self.butt.setParent(None)
		self.update()

		self.forbutt = QtWidgets.QPushButton("Forward",self)
		self.forbutt.move(0,0)
		self.forbutt.clicked.connect(self.secondArea)

		self.backbutt = QtWidgets.QPushButton("Backwards", self)
		self.backbutt.hide()
		self.backbutt.move(400,400)
		self.backbutt.clicked.connect(self.secondArea)

		self.forbutt.show()
		self.prev = "first"

	def secondArea(self,event):
		self.bg = "second"		
		self.backbutt.move(20,20)
		self.backbutt.clicked.connect(self.firstArea)
		
		self.forbutt.move(80,80)
		self.forbutt.clicked.connect(self.thirdArea)
		
		self.backbutt.show()
		self.forbutt.show()

		self.show()
		self.update()
		self.prev = "second"
	
	def thirdArea(self,event):
		self.bg = "third"
		self.backbutt.move(0,0)
		self.backbutt.clicked.connect(self.secondArea)

		self.forbutt.move(25,25)
		self.forbutt.clicked.connect(self.fourthArea)

		self.kamikaze = QtWidgets.QPushButton("fake fif", self)
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
	
	def fourthArea(self,event):
		self.bg = "fourth"	
		self.forbutt.hide()	
		self.backbutt.move(300,300)
		self.backbutt.clicked.connect(self.thirdArea)

		self.backbutt.show()

		self.show()
		self.update()
		self.prev = "fourth"

	def fifthArea(self,event):
		self.bg = "fifth"		
		self.backbutt.move(14,14)
		self.backbutt.clicked.connect(self.thirdArea)
		
		self.forbutt.move(129,129)
		self.forbutt.clicked.connect(self.sixthArea)

		self.backbutt.show()
		self.forbutt.show()

		self.show()
		self.update()
		self.prev = "fifth"
	
	def sixthArea(self,event):
		self.bg = "sixth"		
		self.forbutt.hide()
		self.backbutt.move(84,84)
		self.backbutt.clicked.connect(self.fifthArea)

		self.backbutt.show()

		self.show()
		self.update()
		self.prev = "sixth"
	
		
if __name__=="__main__":
	app = QtWidgets.QApplication(sys.argv)
	win = Window()
	app.exec_()