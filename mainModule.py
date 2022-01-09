from setupModule import setupDevice
from audioModule import recordAudio, playAudio
from buttonModule import waitUntilButtonIsPressed
from requestsModule import sendRecordedMessage, sendQrRecognitionSuccessMessage, sendInitMessage
from cameraModule import searchQr
from validatorsModule import isValidJson, validateJson
import json
import time

import os

currentQrCode = None
userId = None

with open('userData.txt') as user_data:
    globals()['userId'] = json.load(user_data)['userId']

def playBotResponseAndCheckPayload(botMessage):
    if isValidJson(botMessage):
        botMessage = validateJson(botMessage)
        
        if hasattr(botMessage, 'response'):   
            playAudio(botMessage.response.message.audio)
            print('audio played', botMessage.response)
              
            if hasattr(botMessage.response.payload, 'activateCamera'):
                globals()['currentQrCode'] = None
                globals()['currentQrCode'] = searchQr()
                print('qr', globals()['currentQrCode'])
                
                if currentQrCode:
                    newMessage = sendQrRecognitionSuccessMessage(globals()['currentQrCode'])
                    playBotResponseAndCheckPayload(newMessage)
                    globals()['currentQrCode'] = None
                
        else:
            os.system('aplay didNotUnderstandResponse.wav')
            
if userId == None:
    os.system('aplay initDevice.wav')
    setupDevice()
    botMessage = sendInitMessage()
    print(botMessage)
    playBotResponseAndCheckPayload(botMessage) 
else:
    os.system('aplay helloAgain.wav')
    
while True:
    print('start')
    waitUntilButtonIsPressed()

    audio64 = recordAudio()
    print('audio64', audio64)
    
    botMessage = sendRecordedMessage(audio64)
    print('message', botMessage)
    playBotResponseAndCheckPayload(botMessage)
    
    time.sleep(1)
