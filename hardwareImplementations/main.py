import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hamming

winners = []
winnerf = []

skipEvery = 500
skipAmount = 5000

def transform(data,sample_rate = 10000,threshold=100):
    window = hamming(len(data))
    data = data * window

    spectrum = np.fft.fft(data)
    frequency = np.fft.fftfreq(len(data), 1/sample_rate)
    spectrum = abs(spectrum[:len(spectrum)//2])[5:-10]
    frequency = frequency[:len(frequency)//2][5:-10]

    sR = [_ for _ in spectrum if(_>threshold)]
    fR = [frequency[_] for _ in range(len(spectrum)) if(spectrum[_]>threshold)]

    winners.append(sR)
    winnerf.append(fR)

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

offset = 0
skipAmount = 1
while(offset<len(entireData)-256):

    subData = processData(getSubArray(entireData,offset,256))
    print(offset)
    if(offset%skipEvery==0):
        offset+=skipAmount
    transform(subData,44100)

    offset+=1000

plt.show()

for _ in range(len(winners)):
    plt.scatter(winnerf[_],winners[_])

plt.show()