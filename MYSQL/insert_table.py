import pymysql
# 打开数据库连接
db = pymysql.connect('192.168.56.101','root','123456','HR')
# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句
sql = """
    INSERT INTO EMP(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME)
    VALUES('Chen','WenTing11',12,'W',1000)
"""

try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
    print('提交到数据库执行')
except:
    # 如果发生错误则回滚
    db.rollback()
    print('如果发生错误则回滚')

db.close()