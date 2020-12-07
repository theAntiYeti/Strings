from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

from InputWidget import InputWidget

class Division1(QtWidgets.QWidget):
    """
    A widget to store and deal with Width, Height, Padding, number of entries.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_gui()

    def init_gui(self):
        self.layout = QtWidgets.QGridLayout()
        self.setLayout(self.layout)

        self.width_input  = InputWidget("Width", default="1000", intInput=True, parent=self)
        self.height_input = InputWidget("Height", default="800", intInput=True, parent=self)
        self.pad_input    = InputWidget("Padding", default="196", intInput=True, parent=self)
        self.numel_input  = InputWidget("No. Elems", default="150", intInput=True, parent=self)

        self.layout.addWidget(self.width_input, 0, 0)
        self.layout.addWidget(self.height_input, 1, 0)
        self.layout.addWidget(self.pad_input, 2, 0)
        self.layout.addWidget(self.numel_input, 3, 0)
    
    def parse(self):
        width = self.width_input.parse()
        height = self.height_input.parse()
        pad   = self.pad_input.parse()
        numel = self.numel_input.parse()

        return width, height, pad, numel
