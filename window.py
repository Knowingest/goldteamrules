'''Example template'''

import sys
import random
from encounter import encounter, player
from PyQt5 import QtWidgets, QtGui, QtCore
from enemy import *


class Window(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.width = 888
        self.height = 684
        self.setup()

    def setup(self):
        self.setGeometry(10, 10, self.width, self.height)
        self.setWindowTitle("The Game")
        self.p = Painting(self)
        self.show()


class Painting(QtWidgets.QWidget):
    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)
        self.bg = "intro"
        self.prev = "lol"

        self.dialogProgress = 0
        self.approachMother = False

        self.width = 888
        self.height = 684
        self.dead = False
        self.setFixedSize(self.width, self.height)
        self.setup()

    def setup(self):
        self.butt = QtWidgets.QPushButton("Start Game", self)
        self.butt.move(650, 400)
        self.butt.clicked.connect(self.firstArea)
        self.forbutt = QtWidgets.QPushButton("Forwards", self)
        self.backbutt = QtWidgets.QPushButton("Backwards", self)
        self.kamikaze = QtWidgets.QPushButton("Down", self)
        self.buttcleaner()
        self.encs = 1

    def paintEvent(self, event):

        qp = QtGui.QPainter()
        qp.begin(self)

        pen = qp.pen()
        pen.setColor(QtCore.Qt.transparent)
        qp.setPen(pen)

        bush = QtGui.QBrush()
        if self.bg == "first":
            bush.setTextureImage(QtGui.QImage("background1.png"))
        elif self.bg == "second":
            bush.setTextureImage(QtGui.QImage("background2.png"))
        elif self.bg == "third":
            bush.setTextureImage(QtGui.QImage("background3.png"))
        elif self.bg == "fourth":
            bush.setTextureImage(QtGui.QImage("background4.png"))
        elif self.bg == "fifth":
            bush.setTextureImage(QtGui.QImage("background5.png"))
        elif self.bg == "sixth":
            bush.setTextureImage(QtGui.QImage("background6.png"))
        elif self.bg == "intro":
            bush.setTextureImage(QtGui.QImage("startscreen.png"))
        else:
            bush.setTextureImage(QtGui.QImage("bigarena.png"))

        qp.setBrush(bush)

        qp.drawPolygon(QtCore.QPoint(0, 0), QtCore.QPoint(0, 684), QtCore.QPoint(888, 684), QtCore.QPoint(888, 0))

        qp.end()

    def buttcleaner(self):
        self.backbutt.hide()
        self.forbutt.hide()
        self.kamikaze.hide()

    def arenaArea(self, event):
        self.update()

    def firstArea(self, event):
        if self.dialogProgress < 1:
            self.dialogProgress = 1;
            print("Ilia: *groggily waking up* What happened?")
            print("Ilia: Huh--? A cave-in?")
            print("Ilia: This isn't good...")
            print("Ilia: Guess I need to find a way out.")
            print("Ilia: What is this place even? All these swirls...")
            print("\nBlub: *squish*")
            print("\nIlia: What... is that?")
            print("\nBlub: *squiiiish*")
            print("\nIlia: Gross. *pokes it with her sword*")
            print("\nBlub: *SQUASH*")
            print("\nIlia: Oh no. Good thing I brought this sword.")
            print("\nBattle start!")

        self.bg = "first"
        self.prev = "intro"
        self.butt.setParent(None)
        self.update()
        self.buttcleaner()

        app.processEvents()

        self.forbutt.move(800, 290)
        self.forbutt.clicked.connect(self.secondArea)

        self.forbutt.show()
        self.prev = "first"
        if self.encs == 1:
            self.bg = "fight"
            app.processEvents()
            self.update()
            self.fight(1)
            self.encs += 1
            self.bg = "first"
            self.update()
            app.processEvents()

    def secondArea(self, event):
        self.bg = "second"
        self.buttcleaner()

        app.processEvents()

        if self.dialogProgress < 2 and not self.dead:
            self.dialogProgress = 2
            print("Ilia: Hey, water. Now I'll only starve to death.")
            print("Ilia: ...? There's something in here.")
            print("Ilia: ....")
            print("Ilia: \"Beware of mother...?\" What does that mean?")

        app.processEvents()

        self.backbutt.move(0, 290)
        self.backbutt.clicked.connect(self.firstArea)

        self.forbutt.move(800, 290)
        self.forbutt.clicked.connect(self.thirdArea)

        self.backbutt.show()
        self.forbutt.show()

        self.show()
        self.update()
        self.prev = "second"
        if self.encs == 2:
            self.bg = "fight"
            self.update()
            self.fight(2)
            self.encs += 1
            self.bg = "second"
            self.update()

    def thirdArea(self, event):
        self.bg = "third"
        self.buttcleaner()

        app.processEvents()

        if self.dialogProgress < 3 and not self.dead:
            self.dialogProgress = 3
            print("\nIlia: A crossroads... That's neat. Which way, then?")
            print("\nSpooder: *hiss*")
            print("\nIlia: Oh, this again. Guess I'll decide afterwards.")

        self.backbutt.move(50, 550)
        self.backbutt.clicked.connect(self.secondArea)

        self.forbutt.move(700, 100)
        self.forbutt.clicked.connect(self.fourthArea)

        self.kamikaze.move(800, 620)
        self.kamikaze.clicked.connect(self.fifthArea)

        self.backbutt.show()
        self.forbutt.show()
        self.kamikaze.show()

        '''need to do encounter counter
        when = 4'''

        self.show()
        self.update()
        self.prev = "third"
        if self.encs == 3:
            self.bg = "fight"
            self.update()
            self.fight(3)
            self.encs += 1
            self.bg = "third"
            self.update()

    def fourthArea(self, event):
        self.bg = "fourth"
        self.buttcleaner()

        app.processEvents()

        self.backbutt.move(0, 290)
        self.backbutt.clicked.connect(self.thirdArea)

        self.backbutt.show()

        self.show()
        self.update()
        self.prev = "fourth"
        if self.encs == 4:
            self.bg = "fight"
            self.update()
            self.fight(4)
            self.encs += 1
            self.bg = "fourth"
            self.update()

    def fifthArea(self, event):
        self.bg = "fifth"
        self.buttcleaner()

        app.processEvents()

        self.backbutt.move(0, 290)
        self.backbutt.clicked.connect(self.thirdArea)

        self.forbutt.move(800, 290)
        self.forbutt.clicked.connect(self.sixthArea)

        self.backbutt.show()
        self.forbutt.show()
        if self.encs == 5:
            self.encs += 1
        self.show()
        self.update()
        self.prev = "fifth"

    def sixthArea(self, event):
        self.bg = "sixth"
        self.buttcleaner()

        app.processEvents()

        if self.dialogProgress < 6 and not self.dead:
            dialogProgress = 6
            print("\nIlia: Whoa... This is beautiful.")
            print("\nMother: Hello, my child. Are you alright?")
            print("\nIlia: Who are you?")
            print("\nMother: My name is Mother. I've been watching your struggle. Are you hurt at all?")
            print("\nIlia: I'm a little scuffed up, yeah, but I'm fine.")
            print("\nMother: Come here. Let me heal you.")
            print("\nApproach Mother? [Y/N]")

            yesno = input()
            while yesno != "Y" and yesno != "y" and yesno != "N" and yesno != "n":
                yesno = input("Only enter [Y/N]")

            if yesno == "y" or yesno == "Y":
                self.approachMother = True
            else:
                self.approachMother = False

        self.backbutt.move(300, 620)
        self.backbutt.clicked.connect(self.fifthArea)

        self.backbutt.show()
        if self.encs == 6:
            self.bg = "fight"
            app.processEvents()
            self.update()
            self.fight(6)
            self.encs += 1
            self.bg = "sixth"
            app.processEvents()
            self.update()
        self.show()
        app.processEvents()
        self.update()
        self.prev = "sixth"

        if self.encs == 7:
            print("You Win!")
            sys.exit()

    def fight(self, room):
        self.bg = "fight"
        self.update()
        b = list()
        counter = 0
        ilia = player(42)
        ens = 5
        # append enemies
        if room == 1:
            b.append(blub())
        elif room == 2:
            # blub and 2 others
            b.append(blub())
            b.append(blub())
            b.append(snek())
        elif room == 3:
            # 5 enemies
            b.append(snek())
            b.append(spooder())
            b.append(skullitor())
            b.append(blub())
            b.append(blub())
        elif room == 4:
            # big blub and 4 other enemies
            b.append(bigblub())
            b.append(snek())
            b.append(snek())
            b.append(skullitor())
            b.append(blub())
        elif room == 6:
            # mother and 4 other enemies
            b.append(mother())
            b.append(snek())
            b.append(skullitor())
            b.append(blub())
            b.append(spooder())
        arena = encounter(ilia, b)
        charge = False
        damage = 0
        isdead = False

        while ens != 0 and not isdead:
            arena.print_board()
            if charge == False:
                while charge == False:
                    while True:
                        tmp = input("Light attack (1)---takes 1 turn\nHeavy Attack (2)---takes 2 turns\n>: ")
                        if tmp.isdigit():
                            if int(tmp) in range(1, 3):
                                x = int(tmp)
                                break
                            else:
                                print("Try again! (1 or 2)")
                        else:
                            print("Try again! (1 or 2)")
                    # Light attack
                    if x == 1:
                        damage = random.randint(4, 7)
                        break
                    elif x == 2:
                        charge = True
                        damage = random.randint(13, 16)
                        break
                    else:
                        print("Excuse?")
                ens = len(b)

                while True:
                    if len(b) > 1:
                        while True:
                            temp = input("Choose target: \n>: ")
                            if temp.isdigit():
                                y = int(temp)  # enemy array
                                break
                            else:
                                print("Please pick an number starting from 1")
                    else:
                        y = 1
                    # error check
                    if y > 0 and y <= ens:
                        isdead = arena.take_turn(damage, (y - 1))
                        if b[y - 1].hp <= 0:
                            del b[y - 1]
                            ens -= 1
                        break
                    else:
                        print("Invalid input. Excuse?")

            else:
                print("Too tired to move this turn.")
                charge = False
                arena.take_turn(0, 0)

            if ens == 0:
                print("Battle is over!")
            if isdead:
                print("You Died!")
                self.dead = True
                exit(0) # comment if not want to quit
                # return 1 uncomment this if u comment out line above


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    app.exec_()