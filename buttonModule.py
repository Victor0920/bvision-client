from gpiozero import Button
import RPi.GPIO as GPIO

button = Button(21)

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def waitUntilButtonIsPressed():
    button.wait_for_press()
    return 1


def isButtonReleased():
    isButtonReleased = GPIO.input(21)
    print(isButtonReleased)
        
    if isButtonReleased:
        return True
    else:
        return False
