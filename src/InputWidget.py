from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

class InputWidget(QtWidgets.QWidget):
    def __init__(self, text, default="", intInput=False, stringInput=False, parent=None):
        super().__init__(parent)
        self.intInput = intInput
        self.stringInput = stringInput
        self.tag = text
        self.init_gui(default)


    def init_gui(self, default):
        self.layout = QtWidgets.QGridLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.layout)

        self.label = QtWidgets.QLabel()
        self.label.setText(self.tag+":")
        self.entry = QtWidgets.QLineEdit(default)

        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.entry, 0, 1)


    def parse(self):
        txt = self.entry.text()

        try:
            if self.intInput:
                return int(txt)
            elif self.stringInput:
                return txt
            else:
                return float(txt)
        
        except:
            t = "float"
            if self.intInput:
                t = "int"
            raise ValueError("{tag} needs to be a valid {t}".format(tag=self.tag,t=t))