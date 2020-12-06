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

        # Create entries.
        self.width_selector = QtWidgets.QLineEdit()
        self.pad_selector   = QtWidgets.QLineEdit()
        self.height_selector= QtWidgets.QLineEdit()
        self.number_selector= QtWidgets.QLineEdit()

        self.stiff_selector = QtWidgets.QLineEdit()
        self.ts_selector    = QtWidgets.QLineEdit()
        self.su_selector    = QtWidgets.QLineEdit() # Speedup
        self.g_y_selector   = QtWidgets.QLineEdit()

        # Create labels.
        self.width_label    = QtWidgets.QLabel()
        self.pad_label      = QtWidgets.QLabel()
        self.height_label   = QtWidgets.QLabel()
        self.number_label   = QtWidgets.QLabel()

        self.stiff_label    = QtWidgets.QLabel()
        self.ts_label       = QtWidgets.QLabel()
        self.su_label       = QtWidgets.QLabel()
        self.g_y_label      = QtWidgets.QLabel()

        self.width_label.setText("Width: ")
        self.height_label.setText("Height: ")
        self.pad_label.setText("Padding: ")
        self.number_label.setText("No. elements: ")

        self.stiff_label.setText("Stiffness: ")
        self.ts_label.setText("Time Step: ")
        self.su_label.setText("Speed Up: ")
        self.g_y_label.setText("Gravity: ")


        # Setup Grid.
        self.layout.addWidget(self.width_label,0,0);  self.layout.addWidget(self.width_selector,0,1)
        self.layout.addWidget(self.height_label,1,0); self.layout.addWidget(self.height_selector,1,1)
        self.layout.addWidget(self.pad_label,2,0);    self.layout.addWidget(self.pad_selector,2,1)
        self.layout.addWidget(self.number_label,3,0); self.layout.addWidget(self.number_selector,3,1)

        self.layout.addWidget(self.stiff_label,0,2); self.layout.addWidget(self.stiff_selector,0,3)
        self.layout.addWidget(self.ts_label,1,2); self.layout.addWidget(self.ts_selector,1,3)
        self.layout.addWidget(self.su_label,2,2); self.layout.addWidget(self.su_selector,2,3)
        self.layout.addWidget(self.g_y_label,3,2); self.layout.addWidget(self.g_y_selector,3,3)


        # Setup run button.
        self.runbutton = QtWidgets.QPushButton()
        self.runbutton.setText("Run")
        self.runbutton.clicked.connect(self.submit_selection)
        self.layout.addWidget(self.runbutton)
    
    def submit_selection(self):
        try:
            width = int(self.width_selector.text())
            pad   = int(self.pad_selector.text())
            height = int(self.height_selector.text())
            number = int(self.number_selector.text())

            pos = [Vector(width*(i/(number-1)), 0) for i in range(number-1)]

            stiffness = float(self.stiff_selector.text())
            time_step = float(self.ts_selector.text())
            speedup   = float(self.su_selector.text())
            g_y       = float(self.g_y_selector.text())

            chain = StringChain(pos, Vector(0,-g_y), stiffness)

            self.display = MainWindow(width, pad, height, chain, time_step=time_step, speedup=speedup)
            self.display.show()
        except:
            # Insert error screen here.
            pass
            

if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    win = SelectionWindow()
    win.show()

    sys.exit(app.exec_())