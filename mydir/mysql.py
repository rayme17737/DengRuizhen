"""
数据库操作模板
"""

import pymysql

# 数据库连接
args = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "123456",
    "database": "stu",
    "charset": "utf8",
}
db = pymysql.connect(**args)

# 创建游标，操作数据库数据，获取操作结果的对象
cur = db.cursor()


# 数据库读操作
cur.execute()



# 关闭游标和数据库链接
cur.close()
db.close()
















