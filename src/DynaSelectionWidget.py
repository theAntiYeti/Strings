from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

from Vector import Vector
from StringChain import StringChain
from MainWindow import MainWindow

from dynamics_functions import *

class DynaSelectionWidget(QtWidgets.QWidget):
    def __init__(self, chirality, parent=None):
        super().__init__(parent)
        
        self.layout = QtWidgets.QGridLayout()
        self.setLayout(self.layout)

        self.dyna_label    = QtWidgets.QLabel()
        self.dyna_label.setText(chirality +" dynamics")
        self.dyna_selector = QtWidgets.QComboBox()
        self.dyna_selector.addItems(['None', 'Ellipse', 'Sine Impulse'])
        self.dyna_selector.currentIndexChanged.connect(self.selectionchange)

        #Set up parameter selectors
        self.xn_selector = QtWidgets.QLineEdit()
        self.y_selector  = QtWidgets.QLineEdit()
        self.ts_selector = QtWidgets.QLineEdit()
        self.phase_selector = QtWidgets.QLineEdit()

        self.xn_label    = QtWidgets.QLabel()
        self.y_label     = QtWidgets.QLabel()
        self.ts_label    = QtWidgets.QLabel()
        self.phase_label = QtWidgets.QLabel()

        self.xn_label.setText("x scale")
        self.y_label.setText("y scale")
        self.ts_label.setText("time scale")
        self.phase_label.setText("phase")

        self.layout.addWidget(self.dyna_label, 0, 0); self.layout.addWidget(self.dyna_selector, 0, 1)
        self.layout.addWidget(self.xn_label, 1, 0); self.layout.addWidget(self.xn_selector, 1, 1)
        self.layout.addWidget(self.y_label, 2, 0); self.layout.addWidget(self.y_selector, 2, 1)
        self.layout.addWidget(self.ts_label, 3, 0); self.layout.addWidget(self.ts_selector, 3, 1)
        self.layout.addWidget(self.phase_label, 4, 0); self.layout.addWidget(self.phase_selector, 4, 1)

    def selectionchange(self, i):
        if i == 1:
            self.xn_label.setText("x scale")
        if i == 2:
            self.xn_label.setText("Impulses")

    def get_dynamics(self, x_0, y_0):
        i = self.dyna_selector.currentIndex()

        if i == 0:
            return None
        
        elif i == 1:
            x_scale = float(self.xn_selector.text())
            y_scale = float(self.y_selector.text())
            t_scale = float(self.ts_selector.text())
            phase   = float(self.phase_selector.text())

            return circular(x_0, y_0, x_scale, y_scale, time_scale=t_scale, phase=phase)

        elif i == 2:
            n       = int(self.xn_selector.text())
            y_scale = float(self.y_selector.text())
            t_scale = float(self.ts_selector.text())
            phase   = float(self.phase_selector.text())

            return sin_n_impulses(x_0, y_0, n, y_scale, time_scale=t_scale, phase=phase)