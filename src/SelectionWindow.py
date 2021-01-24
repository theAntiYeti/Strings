import sys

import math

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

from Vector import Vector
from StringChain import StringChain
from MainWindow import MainWindow
from DynaSelectionWidget import DynaSelectionWidget

from Division1 import Division1
from Division2 import Division2
from InputWidget import InputWidget

####
# TODO:
# Make window exit clean up simulation

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
        self.division1 = Division1(parent=self)
        self.division2 = Division2(parent=self)

        self.g_x_input   = InputWidget("Gravity x (left)", default="0", parent=self)
        self.g_y_input   = InputWidget("Gravity y", default="1", parent=self)

        self.left_dyna_selector = DynaSelectionWidget("Left", parent=self)
        self.right_dyna_selector = DynaSelectionWidget("right", parent=self)

        self.blur_label = QtWidgets.QLabel()
        self.blur_label.setText("blur")
        self.blur_check = QtWidgets.QCheckBox()

        self.stress_label = QtWidgets.QLabel()
        self.stress_label.setText("Stress mode")
        self.stress_check = QtWidgets.QCheckBox()

        self.color_hot_input = InputWidget("Colour Hot", default="FF0055", stringInput=True, parent=self)
        self.color_cold_input = InputWidget("Colour Cold", default="00FFFF", stringInput=True, parent=self)

        # Setup Grid.
        self.layout.addWidget(self.division1, 0, 0)
        self.layout.addWidget(self.division2, 0, 1)

        self.layout.addWidget(self.g_x_input, 1,0)
        self.layout.addWidget(self.g_y_input, 2,0)

        self.layout.addWidget(self.color_hot_input, 1, 1)
        self.layout.addWidget(self.color_cold_input, 2, 1)

        
        self.layout.addWidget(self.left_dyna_selector, 4, 0)
        self.layout.addWidget(self.right_dyna_selector, 4, 1)


        self.layout.addWidget(self.blur_label, 4,3); self.layout.addWidget(self.blur_check, 4,4)
        self.layout.addWidget(self.stress_label, 5,3); self.layout.addWidget(self.stress_check, 5,4)


        # Setup run button.
        self.runbutton = QtWidgets.QPushButton()
        self.runbutton.setText("Run")
        self.runbutton.clicked.connect(self.submit_selection)
        self.layout.addWidget(self.runbutton)
    
    def submit_selection(self):
        try:
            width, height, pad, number = self.division1.parse()
            stiffness, time_step, speedup, dampening = self.division2.parse()
            pos = [Vector(width*(i/(number-1)), 0) for i in range(number-1)]

            g_x       = self.g_x_input.parse()
            g_y       = self.g_y_input.parse()

            left_dyna = self.left_dyna_selector.get_dynamics(0,0)
            right_dyna = self.right_dyna_selector.get_dynamics(width, 0)

            color_hot = '#'+self.color_hot_input.parse()
            color_cold = '#'+self.color_cold_input.parse()

            do_blur = self.blur_check.isChecked()
            stress_mode = self.stress_check.isChecked()
            
            chain = StringChain(pos, Vector(g_x,-g_y), stiffness, dampening=dampening,
                                            left_dyna=left_dyna, right_dyna=right_dyna)

            self.display = MainWindow(width, pad, height, chain, time_step=time_step, speedup=speedup*2, do_blur=do_blur, stress_mode=stress_mode, color_hot=color_hot, color_cold=color_cold)
            self.display.show()
        except:
            pass

            

if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    win = SelectionWindow()
    win.show()

    sys.exit(app.exec_())