import MySQLdb 
    
con = MySQLdb.connect(host='localhost', user='', passwd='', db = '')

cur = db.cursor()

cur.execute("SELECT * FROM final")

for row in cur.fetchall():
    print (row[0])

db.close()
