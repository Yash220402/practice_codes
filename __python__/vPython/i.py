from vpython import *
import math

# 60 rad = 180/pi * 60 deg

def degToRad(angle):
    return (pi/180)*angle

def radToDeg(angle):
    return (180/pi)*angle

for angle in range(0, 180, math.floor(180/5)):
    print(degToRad(angle))
