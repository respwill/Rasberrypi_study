import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED = 16
GPIO.setup(LED, GPIO.OUT)

try:
    while 1:
        GPIO.output(LED, 1)
        time.sleep(1)
        GPIO.output(LED, 0)
        time.sleep(1)
except KeyboardInterrupt:
    print('clean channel {}'.format(LED))
    GPIO.cleanup(18)
