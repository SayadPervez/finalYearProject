import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

# Define the sampling rate and duration of the recording
fs = 44100  # Hz
duration = 15  # seconds

# Start the recording
print("Recording...")
recording = sd.rec(int(fs * duration), samplerate=fs, channels=1)

# Wait for the recording to complete
sd.wait()

# Extract the audio signal and calculate its Fourier transform
audio_signal = recording[:, 0]  # Extract the first channel (mono)

audio_signal = ["[d t] "+str(_) for _ in audio_signal]

with open("./tty.log","w") as f:
    f.write("\n".join(audio_signal))