from requestsModule import createDefaultUser, createDevice
from validatorsModule import isValidJson, validateJson
import json

botId = '61cebea1b5886165bf128740'
deviceId = None
userId = None

def saveDataToFile():
    data = {'botId': botId, 'deviceId': deviceId, 'userId': userId}
    print(data)

    with open('userData.txt', 'w') as data_file:
        json.dump(data, data_file)

def setupDevice():
    device = createDevice()
    
    if isValidJson(device):
        device = validateJson(device)
        globals()['deviceId'] = device.device._id
        saveDataToFile()
        
        user = createDefaultUser()
        
        if isValidJson(user):
            user = validateJson(user)
            globals()['userId'] = user.user._id
            saveDataToFile()
    
    return
