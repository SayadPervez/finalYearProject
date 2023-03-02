from math import acos,degrees
from konstants import speedOfSound,equiTriangleSide as side

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