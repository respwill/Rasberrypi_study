from flask import Flask, render_template
import datetime


app = Flask(__name__)

@app.route('/')
def hello():
	return 'hello world'

@app.route('/today')
def today():
	localtime=datetime.datetime.now()
	strTime=localtime.strftime("%Y-%m-%d")
	return strTime

@app.route('/cake') 
def cake():
	return render_template('main.html', title='cake')

@app.errorhandler(404)
def show_error(error):
	print( "404 Error")

if __name__== '__main__':
	app.run()
