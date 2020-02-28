from flask import Flask, render_template, request
import RPi.GPIO as GPIO

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
led=22
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, GPIO.LOW)

def get_ledstate():
	status=GPIO.input(led)
	if status == 1 :
		ledstate='on'
 	else:
		ledstate='off'
	return ledstate


@app.route("/")
def index():
	ledstate = get_ledstate()
	return render_template('main1.html', state=ledstate, msg='welcome')

@app.route("/ledon")
def main():
	GPIO.output(led, 1)
	return render_template('main1.html', state='on', msg='Please Turn Off' )


@app.route("/ledoff")
def main1():
	GPIO.output(led, 0)
	return render_template('main1.html', state='off', msg='Please Turn on' )

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8888, debug=True)

