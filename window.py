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
		self.butt.setParent(None)
		self.bg = "first"
		self.update()
		self.secbutt = QtWidgets.QPushButton("Forward",self)
		self.secbutt.move(400,400)
		self.secbutt.clicked.connect(self.secondArea)
		self.secbutt.setFixedWidth(100)
		self.secbutt.setFixedHeight(20)
		self.secbutt.show()

	def secondArea(self,event):
		self.firstbutt = QtWidgets.QPushButton("Back",self)
		self.firstbutt.move(20,20)
		self.secbutt.clicked.connect(self.firstArea)
		
		self.thirdbutt = QtWidgets.QPushButton("Forward",self)
		self.thirdbutt.move(20,20)
		self.thirdbutt.clicked.connect(self.thirdArea)
		
		self.bg = "second"
		self.show()
		self.update()
	
	def thirdArea(self,event):
		self.secbutt = QtWidgets.QPushButton("Back", self)
		self.secbutt.move(0,0)
		self.secbutt.clicked.connect(self.secondArea)

		self.fobutt = QtWidgets.QPushButton("Forward", self)
		self.fobutt.move(25,25)
		self.fobutt.clicked.connect(self.fourthArea)
		
		self.fivbutt = QtWidgets.QPushButton("Forward", self)
		self.fivbutt.move(35,35)
		self.fivbutt.clicked.connect(self.fifthArea)

		self.bg = "third"
		self.show()
		self.update()
	
	def fourthArea(self,event):
		self.thirdbutt = QtWidgets.QPushButton("Back", self)
		self.thirdbutt.move(0,0)
		self.thirdbutt.clicked.connect(self.thirdArea)

		self.bg = "fourth"
		self.show()
		self.update()

	def fifthArea(self,event):
		self.thirdbutt = QtWidgets.QPushButton("Back", self)
		self.thirdbutt.move(0,0)
		self.thirdbutt.clicked.connect(self.thirdArea)
		
		self.sexbutt = QtWidgets.QPushButton("Forward", self)
		self.sexbutt.move(0,0)
		self.sexbutt.clicked.connect(self.sixthArea)

		self.bg = "fifth"
		self.show()
		self.update()
	
	def sixthArea(self,event):
		self.fivbutt = QtWidgets.QPushButton("Back", self)
		self.fivbutt.move(0,0)
		self.fivbutt.clicked.connect(self.fifthArea)

		self.bg = "sixth"
		self.show()
		self.update()
	
		
if __name__=="__main__":
	app = QtWidgets.QApplication(sys.argv)
	win = Window()
	app.exec_()
