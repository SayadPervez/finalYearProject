from konstants import equiTriangleSide as l,speedOfSound as v,trainglePointWeights as tpw,additiveAngleWeights as aaw
from math import asin

def calculateAngle(jsonObject):
    '''
    jsonObject = {
        "Impact1" : { "point" : "A" , "time" : 1.0 },
        "Impact2" : { "point" : "B" , "time" : 1.1 }
        "Impact3" : { "point" : "C" , "time" : 1.3 }
    }
    '''
    deltaT = (jsonObject["Impact2"]["time"]-jsonObject["Impact1"]["time"])
    relativeAngle = asin((v*deltaT)/l)
    additiveAngle = aaw[int(tpw[jsonObject["Impact1"]["point"]]+tpw[jsonObject["Impact2"]["point"]])]
    print(relativeAngle,additiveAngle)
    return(relativeAngle+additiveAngle)

print(calculateAngle(
    {
        "Impact1" : {
            "point" : "B", "time" : 0.2 * (10**-3)
        },
        "Impact2" : {
            "point" : "C", "time" : 0.4 * (10**-3)
        },
        "Impact3" : {
            "point" : "A", "time" : 0.4 * (10**-3)
        }
    }
))