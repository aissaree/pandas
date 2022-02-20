import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    db="test_programmer"
)
cur=db.cursor()
cur.execute("select * from product")
cur = cur.fetchall()
print (cur)