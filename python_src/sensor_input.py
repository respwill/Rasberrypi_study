import RPi.GPIO as GPIO
import time

sensor = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN)

try:
    while 1:
        if GPIO.input(sensor):
            print('detected')
        else:
            print('no one')
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
