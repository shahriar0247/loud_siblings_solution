import sounddevice as sd
import soundfile as sf

samplerate = 192000  # Hertz
duration = 2  # seconds
filename = 'output.wav'

print("started")
mydata = sd.rec(int(samplerate * duration), samplerate=samplerate,
                channels=2, blocking=True)
print("end")

sf.write(filename, mydata, samplerate)