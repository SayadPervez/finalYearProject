from math import cos,radians,sin,atan

def polar2cart(polarPoint):
    return(round(polarPoint[0]*cos(radians(polarPoint[1])),15),round(polarPoint[0]*sin(radians(polarPoint[1])),15))