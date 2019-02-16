from turtle import *
import math
import numpy as np

from math import radians, cos, sin, asin, sqrt

def converse_coord(point=(0,0)):
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

#point(WE,NS)
point_one = (math.radians(37.6173),math.radians(55.7558))
point_one = converse_coord(point_one)

point_two = (math.radians(-149),math.radians(61))
point_two = converse_coord(point_two)

point_three = (math.radians(-155),math.radians(21))
point_three = converse_coord(point_three)

screen = Screen()
screen.setup(960, 490)
screen.bgpic("world.png")

goto(point_one[0],point_one[1])
clear()
color("red")
goto(point_two[0],point_two[1])
goto(point_three[0],point_three[1])

done()