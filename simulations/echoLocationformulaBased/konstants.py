equiTriangleSide = 0.5 # 10 cms
temperature = 28 # degree Celcius
speedOfSound = 331.3 * (( 1 + (temperature/273) )**0.5)

from math import cos,radians,degrees,sin

def polar2cart(polarPoint):
    return(polarPoint[0]*cos(radians(polarPoint[1])),polarPoint[0]*sin(radians(polarPoint[1])))

def getVertices(theta=0):
    ccr = circumcircleRadius = equiTriangleSide / (3**0.5) # a / root 3

    polarA = (ccr,60+theta)
    polarB = (ccr,-60+theta)
    polarC = (ccr,180+theta)

    cartA = polar2cart(polarA)
    cartB = polar2cart(polarB)
    cartC = polar2cart(polarC)

    return(cartA,cartB,cartC)