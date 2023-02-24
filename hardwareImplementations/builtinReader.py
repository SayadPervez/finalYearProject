import sounddevice as sd
import numpy as np

timeDomainArray = []

def print_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
    timeDomainArray.append(str(volume_norm))

with sd.Stream(callback=print_sound,samplerate=10000):
    sd.sleep(2000)

with open("./tty.log","w") as f:
    f.write("\n".join(timeDomainArray))