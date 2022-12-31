from konstants import equiTriangleSide as a, speedOfSound as v
from math import cos,sin,degrees,radians,dist,atan

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

    sourceAngle = degrees(atan(sourcePoint[1]/sourcePoint[0]))# wrt (0,0)
    print(sourceAngle)

    if(debug):
        from matplotlib import pyplot as plt, patches

        fig = plt.figure()
        ax = fig.add_subplot()

        plt.axhline(y=0, color='black', linestyle=':')
        plt.axvline(x=0, color='black', linestyle=':')

        myScatter(ax,cartA,"blue",f"A ({round(tA*1000,3)} ms)")
        myScatter(ax,cartB,"blue",f"B ({round(tB*1000,3)} ms)")
        myScatter(ax,cartC,"blue",f"C ({round(tC*1000,3)} ms)")
        myScatter(ax,sourcePoint,"red","Source")

        circleA = patches.Circle(sourcePoint,dA,color="red",fill=False)
        circleB = patches.Circle(sourcePoint,dB,color="red",fill=False)
        circleC = patches.Circle(sourcePoint,dC,color="red",fill=False)

        ax.add_patch(circleA)
        ax.add_patch(circleB)
        ax.add_patch(circleC)

        ax.set_aspect('equal', adjustable='box')
        ax.spines[['right', 'top']].set_visible(False)

        plt.title("Source Debug Plot")
        plt.xlabel("X Axis")
        plt.ylabel("Y Axis")

        plt.show()

calculateTime((0.3,3**0.4/10),273,debug=True)