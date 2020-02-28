from flask import Flask
from flask import render_template
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

app = Flask(__name__)

@app.route("/read/<port>")
def readGpio(port):
	try:
		GPIO.setup(int(port), GPIO.IN)

		if GPIO.input(int(port)) == True:
			res = "GPIO " + port + " is high."
		else:
			res = "GPIO " + port + " is low."
	except:
		res = "Read error from GPIO " + port + "."


	return render_template('gpio.html', title='GPIO ' + port + ' status.', res=res)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8888, debug=True)

