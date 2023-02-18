equiTriangleSide = 0.1 # 10 cms
temperature = 28 # degree Celcius
speedOfSound = 331.3 * (( 1 + (temperature/273) )**0.5)

directionalWeights = {
    "AB" : 0,
    "BA" : 0,
    "AC" : 120,
    "CA" : 120,
    "BC" : -120,
    "CB" : -120
}