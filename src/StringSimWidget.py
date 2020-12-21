from PyQt5.QtWidgets import *
from PIL.ImageQt import ImageQt
from render import Render
from PyQt5 import QtGui, QtTest
from PIL import Image

from PyQt5 import QtCore

from StringChain import StringChain
from Vector import Vector

class StringSimWidget(QWidget):
    def __init__(self, width, width_padding, height, chain, tick=100, do_blur=False, color='#FF7700', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tick = tick
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.renderer = Render(width, width_padding, height, do_blur=do_blur, color=color)

        self.display  = QLabel()

        self.modelChain = chain
        
        self.canvas = self.renderer.plot_points(self.modelChain.positions())
        self.pix = QtGui.QPixmap.fromImage(ImageQt(self.canvas))

        self.display.setPixmap(self.pix)

        self.layout.addWidget(self.display, 0, 0)
  
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.step)
        self.timer.start(self.tick)
        
        #self.loop()

    def plot(self, points):
        self.canvas = self.renderer.plot_points(points, previous=self.canvas)
        qtCanvas = ImageQt(self.canvas)
        self.pix = QtGui.QPixmap.fromImage(qtCanvas)
        self.display.setPixmap(self.pix)

    def step(self, time_step=0.2):
        self.modelChain.step(time_step)
        print(self.modelChain.kinetic_energy())
        positions = self.modelChain.positions()
        self.plot(positions)
    
    def loop(self, delay=0.05):
        for i in range(10):
            QtTest.QTest.qSleep(delay * 1000)
            self.step()






