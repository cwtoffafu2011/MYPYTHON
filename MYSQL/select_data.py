#!/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect('192.168.56.101','root','123456','HR')

# 使用cursor()方法获取操作游标
cursor = db.cursor()
sql = """
    SELECT * FROM EMP 
    WHERE INCOME > '%d '""" % (1000)

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for r in results:
        fname = r[0]
        lname = r[1]
        age = r[2]
        sex = r[3]
        income = r[4]
        print("fname = %s ,lname = %s ,age = %d ,sex = %s ,income = %d" % \
              (fname, lname, age, sex, income))
except:
    print("Error : unable to fetche dta")

db.close()
