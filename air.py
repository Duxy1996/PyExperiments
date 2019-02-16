from turtle import *
import math
import sys
import numpy as np
import xml.etree.ElementTree as ET

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox
from math import radians, cos, sin, asin, sqrt

class WayPoints:

    def __init__(self, lat, long):
        self.latitude  = lat
        self.longitude = long

class Application:

    textbox2 = []
    textbox  = []
    w        = []

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

        error = False

        if (abs(latitude) > 180):
            QMessageBox.about(self.w,"Error", "The latitude should be between -180 and 180")
            error = True
        if (abs(longitude) > 90):
            QMessageBox.about(self.w,"Error", "The longitude should be between -90 and 90")
            error = True

        if (not(error)):
            goto(point_tmp[0],point_tmp[1])

    def goToMoscow(self):
        point_tmp = (math.radians(37.6173),math.radians(55.7558))
        point_tmp = self.converse_coord(point_tmp)
        goto(point_tmp[0],point_tmp[1])

    def goToAncorage(self):
        point_tmp = (math.radians(-149),math.radians(61))
        point_tmp = self.converse_coord(point_tmp)
        goto(point_tmp[0],point_tmp[1])

    def gotToHawaii(self):
        point_tmp = (math.radians(-155),math.radians(21))
        point_tmp = self.converse_coord(point_tmp)
        goto(point_tmp[0],point_tmp[1])

    def loadWayPoints(self):
        tree = ET.parse('data.xml')
        root = tree.getroot()

        waypoints = []

        for child in root:
            tmp_way = WayPoints(child[0].text,child[1].text)
            waypoints.append(tmp_way)

        print(len(waypoints))

    def __init__(self):

        #point(WE,NS)
        self.loadWayPoints()

        app = QApplication(sys.argv)

        self.w = QWidget()
        self.w.resize(250, 150)
        self.w.move(230, 295)
        self.w.setWindowTitle('Simple')

        button = QPushButton('Fly!', self.w)
        button.setToolTip('This is an example button')
        button.clicked.connect(self.on_click)
        button.move(150,100)

        label = QLabel("Longitude", self.w)
        label.move(50,40)

        self.textbox = QLineEdit(self.w)
        self.textbox.move(100, 40)
        self.textbox.resize(80,20)

        label = QLabel("Latitude", self.w)
        label.move(50,60)

        self.textbox2 = QLineEdit(self.w)
        self.textbox2.move(100, 60)
        self.textbox2.resize(80,20)

        self.w.show()

        screen = Screen()
        screen.setup(960, 490)
        screen.bgpic("world.png")

        self.goToMoscow()
        self.goToAncorage()
        self.gotToHawaii()

        done()

if __name__ == '__main__':
    app = Application()

