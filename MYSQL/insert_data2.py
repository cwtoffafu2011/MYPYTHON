#!/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect('192.168.56.101','root','123456','HR')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句
sql = "INSERT INTO EMP(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
      ('Mac', 'Mohan', 20, 'M', 2000)
try:
    # 执行sql语句
    #循环从  1 到  2
    for i in range(2,200):
        #cursor.execute(sql)
        #插入男生
        cursor.execute( "INSERT INTO EMP(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
      ('Chen'+str(i), 'WenTing'+str(i), 20+i, 'M', 2000+i))
        # 插入女生
        cursor.execute( "INSERT INTO EMP(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
      ('Chen'+str(i), 'Ting'+str(i), 20+i, 'W', 2000+i))
    # 执行sql语句
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()

# 关闭数据库连接
db.close()