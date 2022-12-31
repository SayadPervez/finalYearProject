equiTriangleSide = 0.1 # 10 cms
temperature = 28 # degree Celcius
speedOfSound = 331.3 * (( 1 + (temperature/273) )**0.5)

trainglePointWeights = {
    "A" : 1,
    "a" : 1,
    "B" : 2,
    "b" : 2,
    "C" : 3,
    "c" : 3
}

additiveAngleWeights = {
    3 : 0,
    4 : 120,
    5 : -120
}