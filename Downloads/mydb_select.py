import MySQLdb as mydb

db=mydb.connect('localhost', 'root', 'daks', 'sensor')
cur=db.cursor()
cur.execute('select * from sensor')
while True:
    sensor_data=cur.fetchone()
    if not sensor_data :
        break
    curtime, hum, temp=sensor_data
    print(curtime, hum, temp)
cur.close()
db.close()
