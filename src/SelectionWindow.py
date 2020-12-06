import sys

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

from Vector import Vector
from StringChain import StringChain
from MainWindow import MainWindow
class SelectionWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_gui()

    def setup_gui(self):
        self.window = QtWidgets.QWidget()
        self.layout = QtWidgets.QGridLayout()
        self.setCentralWidget(self.window)
        self.window.setLayout(self.layout)

        self.width_selector = QtWidgets.QLineEdit()
        self.pad_selector   = QtWidgets.QLineEdit()
        self.height_selector= QtWidgets.QLineEdit()
        self.number_selector= QtWidgets.QLineEdit()

        self.width_label    = QtWidgets.QLabel()
        self.pad_label      = QtWidgets.QLabel()
        self.height_label   = QtWidgets.QLabel()
        self.number_label   = QtWidgets.QLabel()

        self.width_label.setText("Width: ")
        self.height_label.setText("Height: ")
        self.pad_label.setText("Padding: ")
        self.number_label.setText("No. elements: ")

        self.layout.addWidget(self.width_label,0,0)
        self.layout.addWidget(self.width_selector,0,1)
        self.layout.addWidget(self.height_label,1,0)
        self.layout.addWidget(self.height_selector,1,1)
        self.layout.addWidget(self.pad_label,2,0)
        self.layout.addWidget(self.pad_selector,2,1)
        self.layout.addWidget(self.number_label,3,0)
        self.layout.addWidget(self.number_selector,3,1)

        self.runbutton = QtWidgets.QPushButton()
        self.runbutton.setText("Run")
        self.runbutton.clicked.connect(self.submit_selection)
        self.layout.addWidget(self.runbutton)
    
    def submit_selection(self):
        width = int(self.width_selector.text())
        pad   = int(self.pad_selector.text())
        height = int(self.height_selector.text())
        number = int(self.number_selector.text())
            
        pos = [Vector(width*(i/(number-1)), 0) for i in range(number-1)]

        chain = StringChain(pos, Vector(0,-1), 4)

        self.display = MainWindow(width, pad, height, chain)
        self.display.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    win = SelectionWindow()
    win.show()

    sys.exit(app.exec_())