from flask import Flask, render_template, request
import RPi.GPIO as GPIO
import MySQLdb as mydb

db = mydb.connect('localhost', 'root', 'daks', 'sensor')
cur = db.cursor()
cur.execute('select * from sensor')
data_tuple = []
while True:
        sensor_data = cur.fetchone()
        if not sensor_data:
                break
        data_tuple.append(sensor_data)
cur.close()
db.close()

app = Flask(__name__)


@app.route("/get_HT_data")
def main1():
	return render_template('HT.html', data=data_tuple)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8888, debug=True)

