from konstants import equiTriangleSide as a, speedOfSound as v
from math import cos,sin,radians,dist

def polar2cart(polarPoint):
    return(polarPoint[0]*cos(radians(polarPoint[1])),polarPoint[0]*sin(radians(polarPoint[1])))

def myScatter(plt,pt,color,label,size=36):
    plt.scatter(pt[0],pt[1],c=color,s=size)
    plt.text(pt[0],pt[1],s=label,weight="bold")

def calculateTime(sourcePoint,theta=0,debug=False):
    ccr = circumcircleRadius = a / (3**0.5) # a / root 3

    polarA = (ccr,60+theta)
    polarB = (ccr,-60+theta)
    polarC = (ccr,180+theta)

    cartA = polar2cart(polarA)
    cartB = polar2cart(polarB)
    cartC = polar2cart(polarC)

    dA = dist(sourcePoint,cartA)
    dB = dist(sourcePoint,cartB)
    dC = dist(sourcePoint,cartC)

    tA = dA/v
    tB = dB/v
    tC = dC/v

    print(tA,tB,tC)

    if(debug):
        import matplotlib.pyplot as plt
        myScatter(plt,(0,0),"green","Origin",22)
        myScatter(plt,cartA,"blue","A")
        myScatter(plt,cartB,"blue","B")
        myScatter(plt,cartC,"blue","C")
        myScatter(plt,sourcePoint,"red","Source")
        plt.show()

calculateTime((0.2,0.2),debug=True)