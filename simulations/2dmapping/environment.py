from matplotlib import pyplot as plt, style
from util import polar2cart
from random import randint as ri
from math import dist
from konstants import speedOfSound as vSound

plt.style.use("ggplot")

class room:
    def __init__(self,boundaries=[],plottingRegion=(20,20)):
        self.boundaries = boundaries
        self.plottingRegion = plottingRegion

    def checkLimits(self,point):
        for condition in self.boundaries:
            if not (condition(point[0],point[1])):
                return(False)
        return(True)

    def plot(self,returnPlot=False):
        fig = plt.figure()
        ax = fig.add_subplot()

        plt.axhline(y=0, color='black', linestyle=':')
        plt.axvline(x=0, color='black', linestyle=':')

        step = 1

        print("Plotting Room")
        roomWave = bouncingCircle("room",(0,0),self,1,10**-6)
        while(sum(roomWave.getAllIncrements())!=0):
            roomWave.evolveAll()
        roomPoints = roomWave.getAllPositions()
        roomPointsX = [_[0] for _ in roomPoints]
        roomPointsY = [_[1] for _ in roomPoints]
        plt.plot(roomPointsX+[roomPointsX[0]],roomPointsY+[roomPointsY[0]],c="black")
        print("Plotting Room Completed")

        ax.set_aspect('equal', adjustable='box')
        ax.spines[['right', 'top']].set_visible(False)

        if(returnPlot):
            return(plt)
        plt.show()

class pointsOfTheCircle:
    def __init__(self,centerOfCircle,angle,boundaries,steps,minResolution):
        self.center = centerOfCircle
        self.angle = angle
        self.boundaries = boundaries
        self.grow = +1 # positive growth
        self.position = centerOfCircle
        self.distance = 0
        self.increment = steps
        self.index = ri(1,10000)
        self.minimumResolution = minResolution

    def offset(self,pt):
        return(pt[0]+self.center[0],pt[1]+self.center[1])

    def evolve(self): # grow or shrink
        oldPosition = self.position
        oldDistance = self.distance
        self.distance+=self.increment
        relativePolar = (self.distance,self.angle)
        relativeCartesian = polar2cart(relativePolar)
        actualCartesian = self.offset(relativeCartesian) 
        self.position = actualCartesian
        if(not self.boundaries.checkLimits(self.position)):
            self.distance = oldDistance
            self.position = oldPosition
            self.increment/=10
            if(self.increment>=self.minimumResolution):
                self.evolve()
            else:
                self.increment=0

class bouncingCircle:
    def __init__(self,name,centerOfCircle,boundaries,steps,minResolution=0.0001,pA=(0,0),pB=(0,0),pC=(0,0)):
        self.name = name
        self.center = centerOfCircle
        self.pA = pA
        self.pB = pB
        self.pC = pC
        self.x = centerOfCircle[0]
        self.y = centerOfCircle[1]
        self.points = [pointsOfTheCircle(centerOfCircle,angle,boundaries,steps,minResolution) for angle in range(361)]

    def plot(self,pltObj,line=False):
        xLi = [_.position[0] for _ in self.points]
        yLi = [_.position[1] for _ in self.points]
        if(line):
            pltObj.plot(xLi+[xLi[0]],yLi+[yLi[0]],c="red")
        else:
            pltObj.scatter(xLi+[xLi[0]],yLi+[yLi[0]],c="red",s=5)
        return(pltObj)

    def evolveAll(self):
        for point in self.points:
            point.evolve()

    def getAllPositions(self):
        return([point.position for point in self.points])

    def getAllIncrements(self):
        return([point.increment for point in self.points])

    def getObject(self):
        retArr=[]
        for point in self.points:
            tempObject = {
                "distance_to_room" : point.distance,
                "dA"               : dist(point.position,self.pA)+point.distance,
                "dB"               : dist(point.position,self.pB)+point.distance,
                "dC"               : dist(point.position,self.pC)+point.distance,
                "position"         : point.position,
                "angle"            : point.angle,
                "tA"               : (dist(point.position,self.pA)+point.distance)/vSound,
                "tB"               : (dist(point.position,self.pB)+point.distance)/vSound,
                "tC"               : (dist(point.position,self.pC)+point.distance)/vSound,
                "name"             : self.name
            }
            retArr.append({"t":tempObject["tA"],"freq":tempObject["name"],"sensor":"A","roomD":tempObject["distance_to_room"],"returnD":dist(point.position,self.pA)})
            retArr.append({"t":tempObject["tB"],"freq":tempObject["name"],"sensor":"B","roomD":tempObject["distance_to_room"],"returnD":dist(point.position,self.pB)})
            retArr.append({"t":tempObject["tC"],"freq":tempObject["name"],"sensor":"C","roomD":tempObject["distance_to_room"],"returnD":dist(point.position,self.pC)})
        return(retArr)