import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hamming
from mySorter import *
from math import degrees,acos

skipEvery = 500
skipAmount = 5000

frequencyBins = []
binOffset = []

def transform(data,sample_rate = 10000,threshold=100):
    window = hamming(len(data))
    data = data * window

    spectrum = np.fft.fft(data)
    frequency = np.fft.fftfreq(len(data), 1/sample_rate)
    spectrum = abs(spectrum[:len(spectrum)//2])[10:-10]
    frequency = frequency[:len(frequency)//2][10:-10]

    sR = [_ for _ in spectrum if(_>threshold)]
    fR = [frequency[_] for _ in range(len(spectrum)) if(spectrum[_]>threshold)]

    if(len(sR)>0):
        frequencyBins.append(fR)
        binOffset.append(offset)
    else:
        return

    plt.plot(frequency, spectrum)
    plt.scatter(fR, sR, color="r")
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.pause(0.001)
    plt.clf()

def readFileAsList():
    with open("./tty.log","r") as f:
        return f.readlines()

def processData(array):
    return [float(_.split(" ")[-1])*100 for _ in array]

def getSubArray(entireData,offset,size):
    return entireData[offset:offset+size]

entireData = readFileAsList()

offset = 1
skipAmount = 1
while(offset<len(entireData)-256):

    subData = processData(getSubArray(entireData,offset,256))
    print(offset)
    if(offset%skipEvery==0):
        offset+=skipAmount
    transform(subData,44100)

    offset+=25

plt.show()

order,deltaT = infer(segregater(frequencyBins),binOffset)

directionalConstant = "".join(order[:2])

temperature = 28 # degree Celcius
speedOfSound = 331.3 * (( 1 + (temperature/273) )**0.5)
a = 75

theta = degrees(acos((deltaT[0]*speedOfSound)/a))

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

print("RESULT : ",360-abs(finalAngle) if finalAngle<0 else finalAngle,"degrees")