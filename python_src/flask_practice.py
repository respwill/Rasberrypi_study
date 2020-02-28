from flask import Flask
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
LED = 16

GPIO.setup(LED, GPIO.OUT)

app = Flask(__name__)
print(app)

@app.route( '/' )
def hello():
    return 'Hello World !'

@app.route('/test')
def testfunction():
    return 'test function'

@app.route('/ledon')
def ledon():
    GPIO.output(LED,1)
   
    return 'led ON'

@app.route('/ledoff')
def ledoff():
    GPIO.output(LED,0)
  
    return 'led OFF'

if __name__ == '__main__':
    app.run(host='192.168.0.157', port=80, debug=True)
    
