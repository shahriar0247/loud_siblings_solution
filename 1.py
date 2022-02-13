import pyaudio
import sys
from array import array
from playsound import playsound
import time



chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS, 
                rate=RATE, 
                input=True,
                output=True,
                frames_per_buffer=chunk)

while True:
    try:
        data = stream.read(chunk)

        threshold = 10 
        max_value = 0

        as_ints = array('h', data)
        max_value = max(as_ints)
        if max_value > 10000:
            playsound('output.wav')
            print(max_value)
    except:
        pass


stream.stop_stream()
stream.close()
p.terminate()