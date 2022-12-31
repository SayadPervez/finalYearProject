from konstants import equiTriangleSide as l,speedOfSound as v,directionalWeights as dw
from math import asin,degrees
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
    relativeAngle = degrees(asin((v*deltaT)/l))
    additiveAngle = dw[directionalConstant]
    #print(relativeAngle,additiveAngle)

    if(directionalConstant=="AB"):
        finalAngle = relativeAngle + additiveAngle
    if(directionalConstant=="BA"):
        finalAngle = additiveAngle - relativeAngle
    if(directionalConstant=="AC"):
        finalAngle = additiveAngle - relativeAngle
    if(directionalConstant=="CA"):
        finalAngle = relativeAngle + additiveAngle
    if(directionalConstant=="BC"):
        finalAngle = relativeAngle + additiveAngle
    if(directionalConstant=="CB"):
        finalAngle = -relativeAngle + additiveAngle

    return(360-abs(finalAngle) if finalAngle<0 else finalAngle)

print(calculateAngle(
    calculateTime((-0.3,-0.1),0
    ,debug=True
    )
))