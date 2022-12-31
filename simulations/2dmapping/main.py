from konstants import equiTriangleSide as a, speedOfSound as v
from util import polar2cart
from environment import room,bouncingCircle
from sub import basePlot
from matplotlib import pyplot as plt

# Grabbing co ordinates of the 3 sensors

ccr = circumcircleRadius = a / (3**0.5) # a / root 3

polarA = (ccr,60)
polarB = (ccr,-60)
polarC = (ccr,180)

cartA = polar2cart(polarA)
cartB = polar2cart(polarB)
cartC = polar2cart(polarC)

pointsOfInterest = [ cartA, cartB, cartC ]
pointsOfInterestX = [_[0] for _ in pointsOfInterest]
pointsOfInterestY = [_[1] for _ in pointsOfInterest]

# Creating a new room

r = room([
    lambda a, b: abs(a)**2 + abs(b)**2 <= 5**2,
    lambda a, b: a+b<=3,
    lambda a, b: b-a<2
],
[7,7])

names = ["fA","fB","fC"]

overallSensorReadingA = []
overallSensorReadingB = []
overallSensorReadingC = []

for ind,currentSource in enumerate(pointsOfInterest):

    wave = bouncingCircle(names[ind],currentSource,r,1,10**-6,pointsOfInterest[0],pointsOfInterest[1],pointsOfInterest[2])
    count = 0
    while(sum(wave.getAllIncrements())!=0):
        wave.evolveAll()
        pltObj = basePlot(r,currentSource,pointsOfInterestX,pointsOfInterestY)
        pltObj = wave.plot(pltObj)
        pltObj.savefig(f"Results/temp/fig_{ind}_{count}.png",dpi=600)
        count+=1
        pltObj.close()

    roomEdgesArray = wave.getObject()

    sensorAreading = list(filter(lambda obj:obj["sensor"]=="A",roomEdgesArray))
    sensorBreading = list(filter(lambda obj:obj["sensor"]=="B",roomEdgesArray))
    sensorCreading = list(filter(lambda obj:obj["sensor"]=="C",roomEdgesArray))

    overallSensorReadingA+=sensorAreading
    overallSensorReadingB+=sensorBreading
    overallSensorReadingC+=sensorCreading

overallSensorReadingA = sorted(overallSensorReadingA,key=lambda obj:obj["t"])
overallSensorReadingB = sorted(overallSensorReadingB,key=lambda obj:obj["t"])
overallSensorReadingC = sorted(overallSensorReadingC,key=lambda obj:obj["t"])

xA = [_["t"] for _ in overallSensorReadingA]
xB = [_["t"] for _ in overallSensorReadingB]
xC = [_["t"] for _ in overallSensorReadingC]

yA = [_["freq"] for _ in overallSensorReadingA]
yB = [_["freq"] for _ in overallSensorReadingB]
yC = [_["freq"] for _ in overallSensorReadingC]

plt.scatter(xA,yA,c="red",label="Sensor A",s=10)
plt.scatter(xB,yB,c="blue",label="Sensor B",s=7)
plt.scatter(xC,yC,c="green",label="Sensor C",s=5)
plt.legend()
#pltObj.savefig(f"Results/sensorView.png",dpi=600)
plt.show()