import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import soundfile as sf


fs = 48000  # sampling frequency
# record sound for desired amount of time
duration = 5  # seconds
myrecording = sd.rec(duration * fs, samplerate=fs, channels=2, dtype='float64')
print("Recording Audio")
sd.wait()
print("Audio recording complete , Play Audio")
sd.play(myrecording, fs)
sd.wait()
print("Play Audio Complete")
print(myrecording)
sf.write('myfile.wav', myrecording, fs, subtype='PCM_24')
