'''Example template'''


import sys
from PyQt5 import QtWidgets, QtGui, QtCore

class Window(QtWidgets.QWidget):

	def __init__(self):
		QtWidgets.QWidget.__init__(self)
		self.setup()
		
	def setup(self):
		self.setGeometry(10,10,888,684)
		self.setWindowTitle("Testing")
		self.p = Painting(self)
		self.show()
		
		
class Painting(QtWidgets.QWidget):
	def __init__(self, parent):
		QtWidgets.QWidget.__init__(self,parent)
		self.setFixedSize(888,684)
		self.setup()
		
	def setup(self):
		self.butt = QtWidgets.QPushButton("Draw a background",self)
		self.butt.move(20,20)
		self.butt.clicked.connect(self.arenaArea)
		self.back=False
		self.show()
	
	def paintEvent(self, event):
		if(self.back):
			qp = QtGui.QPainter()
			qp.begin(self)
			
			pen = qp.pen()
			pen.setColor(QtCore.Qt.transparent)
			qp.setPen(pen)
			
			bush = QtGui.QBrush()
			bush.setTextureImage(QtGui.QImage("bigarena.png"))
			qp.setBrush(bush)
			
			qp.drawPolygon(QtCore.QPoint(0,0), QtCore.QPoint(0,684),QtCore.QPoint(888,684),QtCore.QPoint(888,0))
			
			bush = QtGui.QBrush()
			bush.setTextureImage(QtGui.QImage("iliaattack.gif"))
			qp.setBrush(bush)
			
			qp.drawPolygon(QtCore.QPoint(0,0), QtCore.QPoint(0,180),QtCore.QPoint(228,180),QtCore.QPoint(228,0))
			qp.end()
			self.butt.setParent(None)
	
	def arenaArea(self,event):
		self.back=True
		self.update()
	
	def firstArea(self,event):
		
	
	def secondArea(self,event):
		
	
	def thirdArea(self,event):
		
	
	def fourthArea(self,event):
	
	
	def fifthArea(self,event):
	
	
	def sixthArea(self,event):
	
	
	def seventhArea(self,event):
	
	
		
if __name__=="__main__":
	app = QtWidgets.QApplication(sys.argv)
	win = Window()
	app.exec_()
