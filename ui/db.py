import pymysql

# def getLink():
#     print("获取数据库链接")
#     conn = pymysql.connect(host='bj-cdb-1in2y42y.sql.tencentcdb.com', port=60186,
#                            user='root',
#                            password='Zr19960628',
#                            database='ImageSegmentSystem')
#     cur = conn.cursor()
#     return cur, conn

def getLink():
    print("获取数据库链接")
    conn = pymysql.connect(host='localhost', port=3306,
                           user='root',
                           password='admin123',
                           database='ImageSegmentSystem')
    cur = conn.cursor()
    return cur, conn