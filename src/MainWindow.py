import sys
import time
import math

from PyQt5 import QtWidgets 
from PyQt5 import QtCore 
from PyQt5 import QtGui 
from StringSimWidget import StringSimWidget
from Vector import Vector
from StringChain import StringChain


def sin_dyna(t):
    return Vector(20*math.cos(t),20*math.sin(t))

pos = [Vector(i*20, 0) for i in range(25+1)]
chain = StringChain(pos, Vector(-1, -1), 2, dampening=1, left_dyna=sin_dyna)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ts = 0.1
        self.init_gui()

    def init_gui(self):
        self.window = QtWidgets.QWidget() 
        self.layout = QtWidgets.QGridLayout() 
        self.setCentralWidget(self.window) 
        self.window.setLayout(self.layout)

        self.display_widget = StringSimWidget(500, 100, 500, chain)

        self.layout.addWidget(self.display_widget, 0, 0)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    win = MainWindow()
    win.show()

    sys.exit(app.exec_())
