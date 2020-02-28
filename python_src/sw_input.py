import RPi.GPIO as GPIO
import time

sw = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(sw, GPIO.IN)
while True:
    if GPIO.input(sw)==1:
        print('sw pressed')
    else:
        print('sw unpressed')
        
    time.sleep(1)
