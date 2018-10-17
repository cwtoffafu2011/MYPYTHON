import pymysql

db = pymysql.connect('192.168.56.101','root','123456','HR')

cursor = db.cursor()

sql = "UPDATE EMP SET AGE =1 WHERE SEX = '%c'" % ('M')

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()