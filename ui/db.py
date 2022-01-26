import pymysql

def getLink(self):
    print("获取数据库链接")
    conn = pymysql.connect(host='bj-cdb-1in2y42y.sql.tencentcdb.com', port=60186,
                           user='root',
                           password='Zr19960628',
                           database='ImageSegmentSystem')
    cur = conn.cursor()
    return cur, conn