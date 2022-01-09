import requests
import json

apiUrl = 'https://b-vision-1-kxqg.ew.r.appspot.com/api'
headers = { 'Content-Type': 'application/json' }

botId = None
deviceId = None
userId = None

def readDataFromFile():
    with open('userData.txt') as data_file:
        data = json.load(data_file)
        globals()['botId'] = data['botId']
        globals()['deviceId'] = data['deviceId']
        globals()['userId'] = data['userId']
    
def sendInitMessage():
    readDataFromFile()
    print('init!')
    url = apiUrl + '/messages'
    body = { 'message': { 'message': 'AUTO - init-new-device', 'type': 'text' }, 'actions': {}, 'user': userId, 'language': 'es-ES' }

    response = requests.post(url, json = body, headers = headers)

    return response.text
    

def sendQrRecognitionSuccessMessage(qr):
    url = apiUrl + '/messages'
    body = { 'message': { 'message': 'AUTO - success in tupper recognition. id: ' + qr, 'type': 'text' }, 'actions': {}, 'user': userId, 'language': 'es-ES' }

    response = requests.post(url, json = body, headers = headers)

    return response.text


def sendRecordedMessage(audio64):
    url = apiUrl + '/messages'
    body = { 'message': { 'message': audio64, 'type': 'audio' }, 'actions': {}, 'user': userId, 'language': 'es-ES' }
        
    response = requests.post(url, json = body, headers = headers)

    return response.text

def createDevice():
    url = apiUrl + '/device'
    body = { 'bot': botId, 'model': 'B-VISION-C23' }
        
    response = requests.post(url, json = body, headers = headers)

    return response.text

def createDefaultUser():
    readDataFromFile()
    
    url = apiUrl + '/user'
    body = { 'name': 'default', 'phone': '000000000', 'email': 'default@default.com', 'device': deviceId }
        
    response = requests.post(url, json = body, headers = headers)

    return response.text


readDataFromFile()
