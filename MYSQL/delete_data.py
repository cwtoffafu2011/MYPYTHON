import pymysql

db = pymysql.connect('192.168.56.101','root','123456','HR')

cursor = db.cursor()

sql = "DELETE FROM EMP WHERE SEX = '%c'" % ('W')

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()