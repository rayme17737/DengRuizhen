"""
二进制文件写入读取操作
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
# with open("timg.jfif","rb") as f:
#     data = f.read()
# 写入图片
# sql = "update stu set image=%s where id=1;"
# cur.execute(sql, [data])
# db.commit()

# 提取图片
sql = "select image from stu where id=1;"
cur.execute(sql)
data = cur.fetchone()[0]

with open("mm.pgn","wb") as file:
    file.write(data)

# 关闭游标和数据库链接
cur.close()
db.close()
