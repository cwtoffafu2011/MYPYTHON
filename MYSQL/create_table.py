import pymysql
# 打开数据库连接
db = pymysql.connect('192.168.56.101','root','123456','HR')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS EMP")

# 使用预处理语句创建表
sql = """
    CREATE TABLE EMP(
    FIRST_NAME CHAR(20) NOT NULL,
    LAST_NAME CHAR(20),
    AGE INT,
    SEX CHAR(1),
    INCOME FLOAT 
    )
"""
cursor.execute(sql)

# 关闭数据库连接
db.close()