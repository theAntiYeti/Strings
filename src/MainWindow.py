import sys
import time
import math

from PyQt5 import QtWidgets 
from PyQt5 import QtCore 
from PyQt5 import QtGui 
from StringSimWidget import StringSimWidget
from Vector import Vector
from StringChain import StringChain

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, width, width_padding, height, chain, time_step=0.1, speedup=1, do_blur=False, stress_mode=False, color_hot='#FF7700', color_cold='#00FFFF',parent=None):
        super().__init__(parent)
        self.ts = time_step

        self.window = QtWidgets.QWidget() 
        self.layout = QtWidgets.QGridLayout() 
        self.setCentralWidget(self.window) 
        self.window.setLayout(self.layout)

        self.display_widget = StringSimWidget(width, width_padding, height, chain, int(1000*self.ts / speedup), do_blur=do_blur, stress_mode=stress_mode, color_hot=color_hot, color_cold=color_cold)

        self.layout.addWidget(self.display_widget, 0, 0)
