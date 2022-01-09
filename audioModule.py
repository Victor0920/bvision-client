import pyaudio
import wave
import base64
import os
import time
from buttonModule import isButtonReleased  

CHUNK = 4096
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = 'recordedUserAudio.mp3'

def recordAudio():
    os.system('aplay defaultBeep.wav')
    time.sleep(0.2)
    
    mic = pyaudio.PyAudio()
    stream = mic.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print('recording start')

    frames = []
    
    while True:
        print('hey')
        data = stream.read(CHUNK)
        frames.append(data)

        
        if isButtonReleased():     
            os.system('aplay defaultBeep.wav')
            time.sleep(0.2)
            break
    
    print('recording stop')

    stream.stop_stream()
    stream.close()
    mic.terminate()

    outputFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    outputFile.setnchannels(CHANNELS)
    outputFile.setsampwidth(mic.get_sample_size(FORMAT))
    outputFile.setframerate(RATE)
    outputFile.writeframes(b''.join(frames))
    outputFile.close()

    encoded = base64.b64encode(open('recordedUserAudio.mp3', 'rb').read())
      
    return encoded
    
def playAudio(audioBase64):
    data = base64.b64decode(audioBase64)
    wavFile = open('botResponse.wav', 'wb')
    wavFile.write(data)
   
    os.system('aplay botResponse.wav')
    return 1


