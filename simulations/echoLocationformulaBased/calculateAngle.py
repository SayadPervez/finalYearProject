from konstants import equiTriangleSide as l,speedOfSound as v
from math import asin,degrees,acos
from sourceSimulate import calculateTime

def calculateAngle(jsonObject):
    '''
    Input format
    jsonObject = {
        "Impact1" : { "point" : "A" , "time" : 1.0 },
        "Impact2" : { "point" : "B" , "time" : 1.1 }
        "Impact3" : { "point" : "C" , "time" : 1.3 }
    }
    '''
    deltaT = (jsonObject["Impact2"]["time"]-jsonObject["Impact1"]["time"])
    directionalConstant = jsonObject["Impact1"]["point"]+jsonObject["Impact2"]["point"]
    
    theta = degrees(acos((deltaT*v)/l))

    if(directionalConstant=="AB"):
        finalAngle = 90 - theta
    if(directionalConstant=="BA"):
        finalAngle = 270 + theta
    if(directionalConstant=="AC"):
        finalAngle = 30 + theta
    if(directionalConstant=="CA"):
        finalAngle = 210 - theta
    if(directionalConstant=="BC"):
        finalAngle = 330 - theta
    if(directionalConstant=="CB"):
        finalAngle = 150 + theta

    return(360-abs(finalAngle) if finalAngle<0 else finalAngle)

#print(calculateAngle(calculateTime((0.2,0.2),90,True,False)))