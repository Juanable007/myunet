import pymysql
import redis   # 导入redis模块，通过python操作redis 也可以直接在redis主机的服务端操作缓存数据库


r = redis.Redis(host='localhost', port=6379, decode_responses=True)   # host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379
r.set('name', 'junxi')  # key是"foo" value是"bar" 将键值对存入redis缓存
print(r['name'])
print(r.get('name'))  # 取出键name对应的值
print(type(r.get('name')))

def getLink():
    print("获取数据库链接")
    conn = pymysql.connect(host='bj-cdb-1in2y42y.sql.tencentcdb.com', port=60186,
                           user='root',
                           password='Zr19960628',
                           database='ImageSegmentSystem')
    cur = conn.cursor()
    return cur, conn

def selectImage(id):
    sql = "select id,image from input where id={}".format(id)
    cur, conn = getLink()
    cur.execute(sql)
    conn.commit()
    image = cur.fetchall()
    return image

image = selectImage(65)
fout= open("ui/temp/selected.png", "wb")
fout.write(image[0][1])

r.set("65",image)
print("over ")


