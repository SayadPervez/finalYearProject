from calculateAngle import calculateAngle,calculateTime
from konstants import speedOfSound as vSound,equiTriangleSide as a

loPoints = []

theoreticalAngles = []
observedAngles = []

diffLi = []
xLi = []
yLi = []

divisor = 1

# vertices : (0.028867513459481298, 0.05) (0.028867513459481298, -0.05) (-0.05773502691896258, 7.07050159149938e-18)
xLi.append(0.028867513459481298)
xLi.append(0.028867513459481298)
xLi.append(-0.05773502691896258)
yLi.append(0.05)
yLi.append(-0.05)
yLi.append(0)
diffLi.append(-10)
diffLi.append(-10)
diffLi.append(-10)

t1=[]
t2=[]

i1,i2,i3=[],[],[]

from math import cos,radians,sin,atan
def polar2cart(polarPoint):
    return(round(polarPoint[0]*cos(radians(polarPoint[1])),15),round(polarPoint[0]*sin(radians(polarPoint[1])),15))

for angle in range(0,360):
    x,y = polar2cart((0.4,angle))
    timeObject,theoreticalAngle = calculateTime((x/divisor,y/divisor),0,returnSourceAngle=True)
    observedAngle = calculateAngle(timeObject)
    print(theoreticalAngle)
    loPoints.append((x/divisor,y/divisor))
    xLi.append(x/divisor)
    yLi.append(y/divisor)
    theoreticalAngles.append(theoreticalAngle)
    observedAngles.append(observedAngle)
    diffLi.append(abs(theoreticalAngle-observedAngle))
    t1.append(timeObject["Impact2"]["time"]-timeObject["Impact1"]["time"])
    t2.append(timeObject["Impact3"]["time"]-timeObject["Impact2"]["time"])
    i1.append(timeObject["Impact1"]["time"])
    i2.append(timeObject["Impact2"]["time"])
    i3.append(timeObject["Impact3"]["time"])    



import matplotlib.pyplot as plt  
from matplotlib import cm
import numpy as np

#sumli = [abs(t1[_]+t2[_]) for _ in range(len(t1))]

#plt.plot(list(range(0,360)),t1,c="red",label="diff1")
#plt.plot(list(range(0,360)),t2,c="blue",label="diff2")
#plt.plot(list(range(0,3600)),sumli,label="sum")
#plt.plot(list(range(0,3600)),[abs(sin(radians(_/10)*3)*0.001) for _ in range(0,3600)],label="sine")

plt.plot(list(range(0,360)),i1,label="impact1")
plt.plot(list(range(0,360)),i2,label="impact2")
plt.plot(list(range(0,360)),i3,label="impact3")
#plt.plot(list(range(0,3600)),sumx:=[(i1[_]+i2[_]+i3[_]-(3*min([i1[_],i2[_],i3[_]]))) for _ in range(len(i1))],label="sum")

#print(sumx)
#print(sum(diffLi)/len(diffLi))

#print(((((3**0.5)/2)*(a)))/vSound)

#plt.plot(list(range(0,360)),[abs((sin(radians(_))*a)/vSound) for _ in range(0,360)],label="sine",c="black")
#plt.plot(list(range(0,360)),[abs((cos(radians(_+30))*a)/vSound) for _ in range(0,360)],label="cosine",c="black")
#
#plt.plot(list(range(0,360)),[abs((sin(radians(_+120))*a)/vSound) for _ in range(0,360)],label="sine",c="black")
#plt.plot(list(range(0,360)),[abs((cos(radians(_+150))*a)/vSound) for _ in range(0,360)],label="cosine",c="black")

plt.title("Impact Time Debug Plot\n( source 0.4m away from origin )")
plt.xlabel("Angle")
plt.ylabel("Time to Impact")

plt.legend()
plt.show()