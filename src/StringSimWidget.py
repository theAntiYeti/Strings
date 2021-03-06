from PyQt5.QtWidgets import *
from PIL.ImageQt import ImageQt
from render import Render
from PyQt5 import QtGui, QtTest
from PIL import Image

from PyQt5 import QtCore

from StringChain import StringChain
from Vector import Vector

class StringSimWidget(QWidget):
    def __init__(self, width, width_padding, height, chain, tick=100, do_blur=False, stress_mode=False, color_hot='#FF7700', color_cold='#00FFFF', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tick = tick
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.renderer = Render(width, width_padding, height, do_blur=do_blur, color_high=color_hot, color_low=color_cold)

        self.display  = QLabel()

        self.modelChain = chain
        
        self.canvas = self.renderer.plot_points(self.modelChain.positions())
        self.pix = QtGui.QPixmap.fromImage(ImageQt(self.canvas))

        self.display.setPixmap(self.pix)

        self.layout.addWidget(self.display, 0, 0)
  
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.step)
        self.timer.start(self.tick)

        self.stress_mode = stress_mode
        # Thing for colour changing on energy
        self.max_energy_seen = 0
        
        #self.loop()

    def plot(self, points, dark_qs):
        self.canvas = self.renderer.plot_points(points, dark_qs=dark_qs, previous=self.canvas)
        qtCanvas = ImageQt(self.canvas)
        self.pix = QtGui.QPixmap.fromImage(qtCanvas)
        self.display.setPixmap(self.pix)

    def step(self, time_step=0.2):
        self.modelChain.step(time_step)

        dark_qs = self.modelChain.dark_qs(stress_mode=self.stress_mode)

        positions = self.modelChain.positions()
        self.plot(positions, dark_qs=dark_qs)
    
    def loop(self, delay=0.05):
        for i in range(10):
            QtTest.QTest.qSleep(delay * 1000)
            self.step()






