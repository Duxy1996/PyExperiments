from turtle import *
import math
import sys
import numpy as np

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit
from math import radians, cos, sin, asin, sqrt

class Application:

    textbox2 = []
    textbox = []

    def converse_coord(self,point=(0,0)):
        lat = point[0]
        lon = point[1]
        if lat > math.radians(90):
            x = 260 * sin(math.radians(90)) +  260*sin(lat-math.radians(90))
        elif lat < math.radians(-90):
            x = 230 * sin(math.radians(-90)) + 230*sin(lat+math.radians(90))
        else:
            x = 260 * sin(lat)
        y = 260 * sin(lon)
        return (x-35,y-70)

    def on_click(self):
        latitude  = float(self.textbox.text())
        longitude = float(self.textbox2.text())

        point_tmp = (math.radians(latitude),math.radians(longitude))
        point_tmp = self.converse_coord(point_tmp)

        goto(point_tmp[0],point_tmp[1])

    def __init__(self):

        #point(WE,NS)
        app = QApplication(sys.argv)

        w = QWidget()
        w.resize(250, 150)
        w.move(230, 295)
        w.setWindowTitle('Simple')

        button = QPushButton('PyQt5 button',w)
        button.setToolTip('This is an example button')
        button.clicked.connect(self.on_click)
        button.move(150,100)

        label = QLabel("Longitude", w)
        label.move(50,40)

        self.textbox = QLineEdit(w)
        self.textbox.move(100, 40)
        self.textbox.resize(80,20)

        label = QLabel("Latitude", w)
        label.move(50,60)

        self.textbox2 = QLineEdit(w)
        self.textbox2.move(100, 60)
        self.textbox2.resize(80,20)

        w.show()

        point_one = (math.radians(37.6173),math.radians(55.7558))
        point_one = self.converse_coord(point_one)

        point_two = (math.radians(-149),math.radians(61))
        point_two = self.converse_coord(point_two)

        point_three = (math.radians(-155),math.radians(21))
        point_three = self.converse_coord(point_three)

        screen = Screen()
        screen.setup(960, 490)
        screen.bgpic("world.png")

        goto(point_one[0],point_one[1])
        clear()
        color("red")
        goto(point_two[0],point_two[1])
        goto(point_three[0],point_three[1])

        done()

if __name__ == '__main__':
    app = Application()
    sys.exit(app.exec_())

