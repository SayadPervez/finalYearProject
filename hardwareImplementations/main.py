import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hamming

skipEvery = 500
skipAmount = 5000

def transform(data):
    window = hamming(len(data))
    data = data * window

    sample_rate = 10000
    spectrum = np.fft.fft(data)
    frequency = np.fft.fftfreq(len(data), 1/sample_rate)
    spectrum = abs(spectrum[:len(spectrum)//2])[10:]
    frequency = frequency[:len(frequency)//2][10:]

    plt.plot(frequency, spectrum)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.pause(0.001)
    plt.clf()

def readFileAsList():
    with open("./tty.log","r") as f:
        return f.readlines()

def processData(array):
    return [int(_.split(" ")[-1]) for _ in array]

def getSubArray(entireData,offset,size):
    return entireData[offset:offset+size]

entireData = readFileAsList()

offset = 1
while(offset<len(entireData)-256):

    subData = processData(getSubArray(entireData,offset,256))
    print(offset)
    if(offset%skipEvery==0):
        offset+=skipAmount
    transform(subData)

    offset+=1

plt.show()