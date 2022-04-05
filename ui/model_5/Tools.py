import sqlite3
import os
import ui.db as db

class Tools():

    @staticmethod
    def createDb():
        print("创建数据库连接")
        # 如果路径下没有db文件，重新创建并插入示例数据
        if os.path.exists('mydata.db') == False:
            connect = sqlite3.connect('mydata.db')
            c = connect.cursor()
            c.execute('''create table mydata(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Website varchar(1000),
                username varchar(1000),
                passwd varchar(1000)
            );
            ''')
            connect.commit()
            c.execute("insert into mydata values(1,'qq','qq','test123')")
            connect.commit()
            connect.close()

    @staticmethod
    def getData():

        cur,conn  = db.getLink()
        cur.execute('select id, userName,passWord,email,role,remark,lastLoginTime,create_time,update_time from user')
        data = cur.fetchall()

        conn.close()
        return data

        # 新增的数据库操作

    @staticmethod
    def addData(username, passwd,email,role,remark):

        cur,connect = db.getLink()
        sql = "insert  into user (userName,passWord,email,role ,remark)  values (%s,%s,%s,%s,%s)"
        parm=(username,passwd,email,role,remark)
        cur.execute(sql,parm)
        connect.commit()
        connect.close()

    @staticmethod
    def editData(id,username, passwd,email,role,remark):

        cur,connect = db.getLink()
        command = "update user set userName='%s',passWord='%s',email='%s',role ='%s',remark='%s' where id=%s" % (
        username, passwd,email,role,remark, id)
        cur.execute(command)
        connect.commit()
        connect.close()

    @staticmethod
    def delData(id):
        print(33333)
        cur,conn = db.getLink()
        # connect = sqlite3.connect('mydata.db')
        # c = connect.cursor()
        # print(1)
        command = "delete from user where id = %s" % id
        print(command)
        cur.execute(command)
        conn.commit()
        conn.close()
