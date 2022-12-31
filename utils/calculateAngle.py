from konstants import equiTriangleSide as l,speedOfSound as v,trainglePointWeights as tpw,additiveAngleWeights as aaw
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
    relativeAngle = degrees(asin((v*deltaT)/l))
    additiveAngle = aaw[int(tpw[jsonObject["Impact1"]["point"]]+tpw[jsonObject["Impact2"]["point"]])]
    print(relativeAngle,additiveAngle)
    finalAngle = relativeAngle+additiveAngle
    return(360-abs(finalAngle) if finalAngle<0 else finalAngle)

print(calculateAngle(
    calculateTime((0.1,0.1),180,debug=True)
))