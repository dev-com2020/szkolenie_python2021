import pymysql as mysql

con = mysql.Connect(host='locahost',user='admin',passwd="dj9f7989@", db='klienci')

cur = con.cursor()

cur.execute("USE database_name")
cur.execute("SHOW TABLES")

for record in cur:
    print(record[0])

cur.close()