import cv2
import numpy as np
from pyzbar.pyzbar import decode
import os

qr = None

def searchQr():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

    while True:
        success, img = cap.read()
        
        for barcode in decode(img):
            globals()['qr'] = barcode.data.decode('utf-8')
            
            if not isinstance(qr, type(None)):
                scannedQr = globals()['qr']
                globals()['qr'] = None
                os.system('aplay defaultBeep.wav')
                
                cap.release()
                cv2.destroyAllWindows()
                
                return scannedQr
                