from types import SimpleNamespace
import json

def isValidJson(jsonData):
    try:
        json.loads(jsonData)
    except:
        return False
    
    return True


def validateJson(jsonData):
    try:
        json.loads(jsonData)
    except:
        return False
    
    return json.loads(jsonData, object_hook=lambda d: SimpleNamespace(**d))