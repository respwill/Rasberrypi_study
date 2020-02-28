from flask import Flask, render_template
import datetime
import MySQLdb as mydb

app = Flask(__name__)

def getWeather():
        db=mydb.connect('localhost', 'root', 'Amkor123!', 'sensor')
        cur=db.cursor()
        cur.execute('select * from sensor')
        temp_list = []
        while True:
                sensor_data=cur.fetchone()
                if not sensor_data:
                        break
                c_time, humidity, temperature=sensor_data
                temp_list.append('date:' + str(c_time) + ' Humidity:' + str(humidity) + ' Temperature:' + str(temperature))

        cur.close()
        db.close()
        return temp_list

@app.route('/')
@app.route('/weather') 
def weather():
        temp_list = getWeather()
        print(temp_list[1:3])
        return render_template('weather.html', weather=temp_list)

if __name__== '__main__':
	app.run(host='0.0.0.0', port=80, debug=True)
