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
	
	def hideyobutts(self):
		if self.bg =="first":
			self.butt.setParent(None)
			self.secbutt.setParent(None)
		elif self.bg=="second":
			self.secbutt.setParent(None)
			self.thirdbutt.setParent(None)
			self.fobutt.setParent(None)
			self.fivbutt.setParent(None)
		elif self.bg=="third":
			self.secbutt.setParent(None)
			self.thirdbutt.setParent(None)
			self.fobutt.setParent(None)
			self.fivbutt.setParent(None)
		elif self.bg=="fourth":
			self.thirdbutt.setParent(None)
		elif self.bg=="fifth":
			self.secbutt.setParent(None)
			self.thirdbutt.setParent(None)
			self.fobutt.setParent(None)
			self.fivbutt.setParent(None)
		elif self.bg=="sixth":
			self.fivbutt.setParent(None)
		else: #self.bg=="arena":
			if self.prev =="first":
				self.butt.setParent(None)
				self.secbutt.setParent(None)
			elif self.prev=="second":
				self.secbutt.setParent(None)
				self.thirdbutt.setParent(None)
				self.fobutt.setParent(None)
				self.fivbutt.setParent(None)
			elif self.prev=="third":
				self.secbutt.setParent(None)
				self.thirdbutt.setParent(None)
				self.fobutt.setParent(None)
				self.fivbutt.setParent(None)
			elif self.prev=="fourth":
				self.thirdbutt.setParent(None)
			elif self.prev=="fifth":
				self.secbutt.setParent(None)
				self.thirdbutt.setParent(None)
				self.fobutt.setParent(None)
				self.fivbutt.setParent(None)
			elif self.prev="sixth":
				self.fivbutt.setParent(None)





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
		self.hideyobutts()
		self.bg = "first"
		self.update()
		self.secbutt = QtWidgets.QPushButton("Forward",self)
		self.secbutt.move(400,400)
		self.secbutt.clicked.connect(self.secondArea)
		self.secbutt.setFixedWidth(100)
		self.secbutt.setFixedHeight(20)
		self.secbutt.show()
		self.prev = "first"

	def secondArea(self,event):
		self.hideyobutts()
		self.firstbutt = QtWidgets.QPushButton("Back",self)
		self.firstbutt.move(20,20)
		self.secbutt.clicked.connect(self.firstArea)
		
		self.thirdbutt = QtWidgets.QPushButton("Forward",self)
		self.thirdbutt.move(20,20)
		self.thirdbutt.clicked.connect(self.thirdArea)
		
		self.firstbutt.show()
		self.thirdbutt.show()
		self.bg = "second"
		self.show()
		self.update()
		self.prev = "second"
	
	def thirdArea(self,event):
		self.hideyobutts()
		self.secbutt = QtWidgets.QPushButton("Back", self)
		self.secbutt.move(0,0)
		self.secbutt.clicked.connect(self.secondArea)

		self.fobutt = QtWidgets.QPushButton("Forward", self)
		self.fobutt.move(25,25)
		self.fobutt.clicked.connect(self.fourthArea)
		
		self.fivbutt = QtWidgets.QPushButton("Forward", self)
		self.fivbutt.move(35,35)
		self.fivbutt.clicked.connect(self.fifthArea)

		self.secbutt.show()
		self.fobutt.show()
		self.fivbutt.show()
		self.bg = "third"
		self.show()
		self.update()
		self.prev = "third"
	
	def fourthArea(self,event):
		self.hideyobutts()
		self.thirdbutt = QtWidgets.QPushButton("Back", self)
		self.thirdbutt.move(0,0)
		self.thirdbutt.clicked.connect(self.thirdArea)

		self.thirdbutt.show()
		self.bg = "fourth"
		self.show()
		self.update()
		self.prev = "fourth"

	def fifthArea(self,event):
		self.hideyobutts()
		self.thirdbutt = QtWidgets.QPushButton("Back", self)
		self.thirdbutt.move(0,0)
		self.thirdbutt.clicked.connect(self.thirdArea)
		
		self.sexbutt = QtWidgets.QPushButton("Forward", self)
		self.sexbutt.move(0,0)
		self.sexbutt.clicked.connect(self.sixthArea)

		self.thirdbutt.show()
		self.sexbutt.show()
		self.bg = "fifth"
		self.show()
		self.update()
		self.prev = "fifth"
	
	def sixthArea(self,event):
		self.hideyobutts()
		self.fivbutt = QtWidgets.QPushButton("Back", self)
		self.fivbutt.move(0,0)
		self.fivbutt.clicked.connect(self.fifthArea)

		self.fivbutt.show()
		self.bg = "sixth"
		self.show()
		self.update()
		self.prev = "sixth"
	
		
if __name__=="__main__":
	app = QtWidgets.QApplication(sys.argv)
	win = Window()
	app.exec_()
