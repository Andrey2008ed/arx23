import pymysql
from config import host, user, password, db_name

try:
    connection = pymysql.connect(
        host = host, #localhost из config.py
        port = 3306,
        user = user,
        password = password,
        database = db_name,
        cursorclass = pymysql.cursors.DictCursor
    )
    print("Connected")
except Exception as ex:
    print("Disconnected")
    print(ex)