import MySQLdb as mydb
db=mydb.connect("localhost", "root", "daks", "sensor")
cur=db.cursor()
sql = "insert into sensor values(now(), %f,%f )"
temp = 23.7
humi = 56.7
cur.execute( sql % (humi, temp))
db.commit()
db.close()
