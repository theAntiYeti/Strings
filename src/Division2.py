from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

from InputWidget import InputWidget

class Division2(QtWidgets.QWidget):
    """
    A widget to store and deal with stiffness, time step, speedup, dampening.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_gui()

    def init_gui(self):
        self.layout = QtWidgets.QGridLayout()
        self.setLayout(self.layout)

        self.width_input  = InputWidget("Stiffness", default="15", parent=self)
        self.height_input = InputWidget("Time step", default="0.1", parent=self)
        self.pad_input    = InputWidget("Speedup", default="1", parent=self)
        self.numel_input  = InputWidget("Dampening", default="0", parent=self)

        self.layout.addWidget(self.width_input, 0, 0)
        self.layout.addWidget(self.height_input, 1, 0)
        self.layout.addWidget(self.pad_input, 2, 0)
        self.layout.addWidget(self.numel_input, 3, 0)
    
    def parse(self):
        stiff = self.width_input.parse()
        ts = self.height_input.parse()
        speedup   = self.pad_input.parse()
        damp = self.numel_input.parse()

        return stiff, ts, speedup, damp
