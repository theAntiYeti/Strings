import sys
import time
import math

from PyQt5 import QtWidgets 
from PyQt5 import QtCore 
from PyQt5 import QtGui 
from StringSimWidget import StringSimWidget
from Vector import Vector
from StringChain import StringChain

def bdd_sin_dyna(t):
    if t < 2*math.pi or 4*math.pi < t < 6*math.pi:
        return Vector(0, 40*math.sin(t))
    return Vector(0,0)

def right_bdd_sin_dyna(t):
    if t < 2*math.pi or 4*math.pi < t < 6*math.pi:
        return Vector(500, 40*math.sin(t))
    return Vector(500,0)

def sin_dyna(t):
    return Vector(20*math.cos(t),20*math.sin(t))

pos = [Vector(i*10, 0) for i in range(50+1)]
chain = StringChain(pos, Vector(0,0), 4, dampening=0.1, left_dyna=bdd_sin_dyna)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, width, width_padding, height, chain, time_step=0.1, speedup=1, parent=None):
        super().__init__(parent)
        self.ts = time_step

        self.window = QtWidgets.QWidget() 
        self.layout = QtWidgets.QGridLayout() 
        self.setCentralWidget(self.window) 
        self.window.setLayout(self.layout)

        self.display_widget = StringSimWidget(width, width_padding, height, chain, int(1000*self.ts / speedup))

        self.layout.addWidget(self.display_widget, 0, 0)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    win = MainWindow(500, 100, 500, chain)
    win.show()

    sys.exit(app.exec_())
