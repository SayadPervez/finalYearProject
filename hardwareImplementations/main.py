import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hamming

def transform(data):
    window = hamming(len(data))
    data = data * window

    sample_rate = 10000
    spectrum = np.fft.fft(data)
    frequency = np.fft.fftfreq(len(data), 1/sample_rate)
    spectrum = abs(spectrum[:len(spectrum)//2])
    frequency = frequency[:len(frequency)//2]

    plt.plot(frequency, spectrum)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.pause(0.01)
    plt.clf()

def readFileAsList():
    with open("./tty.log","r") as f:
        return f.readlines()

def processData(array):
    return [int(_.split(" ")[-1]) for _ in array]

def getSubArray(entireData,offset,size):
    return entireData[offset:offset+size]

entireData = readFileAsList()
for offset in range(len(entireData)-256):
    subData = processData(getSubArray(entireData,offset,256))
    transform(subData)

plt.show()