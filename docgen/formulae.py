from math import acos,degrees,cos,sin,radians
from konstants import speedOfSound,equiTriangleSide as side
import matplotlib.patches as patches
import numpy as np

firstHitFormulae = {
    "AB" : lambda theta:90-theta,
    "BA" : lambda theta:270+theta,
    "BC" : lambda theta:330-theta,
    "CB" : lambda theta:150+theta,
    "AC" : lambda theta:90+theta,
    "CA" : lambda theta:210-theta
}

secondHitFormulae = {
    "AB" : lambda theta:90+theta,
    "BA" : lambda theta:270-theta,
    "BC" : lambda theta:theta-30,
    "CB" : lambda theta:150-theta,
    "AC" : lambda theta:210+theta,
    "CA" : lambda theta:330+theta
}

getTheta = lambda deltaT : degrees(acos((speedOfSound*deltaT)/side))

def polar2cart(polarPoint):
    return(polarPoint[0]*cos(radians(polarPoint[1])),polarPoint[0]*sin(radians(polarPoint[1])))

def getVertices(theta=0):
    ccr = circumcircleRadius = side / (3**0.5) # a / root 3

    polarA = (ccr,60+theta)
    polarB = (ccr,-60+theta)
    polarC = (ccr,180+theta)

    cartA = polar2cart(polarA)
    cartB = polar2cart(polarB)
    cartC = polar2cart(polarC)

    return(cartA,cartB,cartC)

def drawLine(ax, angle, point, label, color="red",linewidth=2 ,linestyle="solid"):

    theta = np.deg2rad(angle)
    m = np.tan(theta)
    b = point[1] - m * point[0]
    
    x = np.linspace(-2, 2, 100)
    
    y = m * x + b
    
    ax.plot(x, y, color=color, linewidth=linewidth, linestyle=linestyle,label=label)
    
    #ax.scatter(point[0], point[1], color='blue', marker='o', s=100)
    
    # Set the x and y limits
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    
    # Add axis labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

def drawAngle(ax,center,startAngle,endAngle,radius=0.05):
    ax.add_patch(patches.Arc(center, radius*2, radius*2, angle=startAngle, theta2=endAngle-startAngle, linewidth=1, color="k"))