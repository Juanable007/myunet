import os
import sys
import traceback

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QApplication, QMessageBox
from PIL import ImageQt, Image
from unet import Unet
from MainWindows import Ui_MainWindow
import pymysql
import cv2
import time
import Compose

class PyQtMainEntry(QMainWindow, Ui_MainWindow):
    def __init__(self):

        super().__init__()
        self.setupUi(self)
        self.CutFlag = False
        self.SegmentFlag = False
      # sql = "SELECT * FROM user WHERE id=1;"
        # cur.execute(sql)
        # # 获取查询到的数据，是以字典的形式存储的，所以读取需要使用data[i][j]下标定位
        # data = cur.fetchall()
        # # 打印测试
        # print(data)
    # 打开文件方法
    def openFile(self):
        print("打开文件选择器方法")
        path, imgType = QFileDialog.getOpenFileName(self.centralwidget, "打开图片", "", "*.jpg;;All Files(*)")
        img = QtGui.QPixmap(path).scaled(self.label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        imgname=path.split('/')
        self.textEdit_2.setText(path)
        self.textEdit.setText(imgname[-1])
        self.label.setPixmap(img)
    #调用模型分割图像
    def segImg(self):
        print("分割图像方法")
        # self.textEdit_2.toPlainText()
        # ImgSegment = myFun2(self.textEdit_2.toPlainText())
        # self.label_outImg.setPixmap(
        #     ImageQt.toqpixmap(ImgSegment).scaled(self.label_outImg.size(), Qt.KeepAspectRatio,
        #                                              Qt.SmoothTransformation))
        # self.SegmentFlag = True

    # 操作数据库部分
    # 1.获取链接
    def  getLink(self):
        print("获取数据库链接")
        conn = pymysql.connect(host='bj-cdb-1in2y42y.sql.tencentcdb.com',port=60186,
                               user='root',
                               password='Zr19960628',
                               database='ImageSegmentSystem')
        cur = conn.cursor()
        return cur,conn
    # 表1:路径 时间 图片名称,参数1,参数2

    def saveImg(self):
        # 路径和名称
        print("保存图片数据")
        try:
            #全路径
            path =self.textEdit_2.toPlainText()
            name=self.textEdit.toPlainText()
            fp = open(path, 'rb')
            img=fp.read()
            fp.close()
            sql = "insert into input(path,imgName,image) values(%s,%s,%s)"  # 注意此处与前一种形式的不同
            parm = (path,name,img)
            cur, conn = self.getLink()
            cur.execute(sql, parm)
            conn.commit()
            self.messageDialog()
        except:
           self.warningDialog()
        finally:
            conn.close()
    # 下拉框刷新
    def refresh(self):
        print("下拉框刷新方法")
        # 显示最近的10条记录,
        cur, conn = self.getLink()
        sql="select  id,imgName from  input order by create_time desc  limit  10"
        cur.execute(sql)
        data= cur.fetchall()
        # self.comboBox.setItemText(0,"123")
        length = len(data)
        self.comboBox.clear()
        self.comboBox_2.clear()
        for i in range(length):
            # self.comboBox.addItem(data[i][1])
            self.comboBox.addItem(data[i][1],str(data[i][0]))
            self.comboBox_2.addItem(data[i][1],str(data[i][0]))

    # 刷新下拉选择的图片
    def refreshImg(self):
        try:
            print("刷新图片")
            id= self.comboBox.currentData()
            if(id!=None):
                # path=self.selectPath(id)
                # openPath = ''.join(path[0])
                # 查询图片
                image= self.selectImage(id)
                fout= open("temp/selected.png", "wb")
                fout.write(image[0][1])
                self.selectedImg.setPixmap(
                    ImageQt.toqpixmap("temp/selected.png").scaled(self.selectedImg.size(), Qt.KeepAspectRatio,
                                                         Qt.SmoothTransformation))
                segPath= self.selectSegPath(id)
                if(len(segPath)!=0):
                    segPath = ''.join(segPath[0])
                # 之前已经分割过了,把分割好的图像从数据库查出放到目录下.
                    self.joinOutLabel.setPixmap(ImageQt.toqpixmap(segPath).scaled(self.joinOutLabel.size(),
                                                             Qt.KeepAspectRatio,Qt.SmoothTransformation))
                else:
                    self.joinOutLabel.setPixmap(ImageQt.toqpixmap('./utils/white.png').scaled(self.joinOutLabel.size(),
                                                                                  Qt.KeepAspectRatio,
                                                                                  Qt.SmoothTransformation))
                    print("---")
        except:
            print("显示图片异常")
        finally:
            print("")

    # 分析页面刷新下拉选择的图片
    def refreshAnaImg(self):
        try:
            print("刷新分析图片")
            id= self.comboBox_2.currentData()
            if(id!=None):
                path=self.selectPath(id)
                openPath = ''.join(path[0])
                self.label_calImg.setPixmap(
                    ImageQt.toqpixmap(openPath).scaled(self.selectedImg.size(), Qt.KeepAspectRatio,
                                                         Qt.SmoothTransformation))
        except:
            print("分析页面显示图片异常")
        finally:
            print("")
    def segAndJoin(self):
        print("分割拼接方法")
        #  获取要分割图像的路径
        id = self.comboBox.currentData()
        inputPath = 'temp/input/'
        outPath = 'temp/output/'
        joinOutPath = 'temp/joinOut/'
        #输出文件名称
        outSavePathName = self.comboBox.currentText()
        path = self.selectPath(id)
        path = ''.join(path[0])
        #  裁切
        start = time.time()
        try:
            self.seg(path)
            end = time.time()
            #  拼接结果
            Compose.image_compose(outPath, joinOutPath + outSavePathName)
            #  返回页面
            self.joinOutLabel.setPixmap(
                ImageQt.toqpixmap(joinOutPath + outSavePathName).scaled(self.joinOutLabel.size(), Qt.KeepAspectRatio,
                                                                        Qt.SmoothTransformation))
            #     落表2 输出路径,输出名称
            sql = "insert into output (parentId,segPath,segName,segImage) values(%s,%s,%s,%s)"  # 注意此处与前一种形式的不同
            file= open(joinOutPath + outSavePathName,"rb")
            img = file.read()
            parm = (id, joinOutPath + outSavePathName, outSavePathName,img)
            cur, conn = self.getLink()
            cur.execute(sql, parm)
            file.close()
            conn.commit()
            conn.close()
        except:
            print("分割方法出现异常")
            traceback.print_exc()
        finally:
            print("调用模型总用时: {}".format(end - start))

    def calParm(self):
        print("计算参数parm ")
        id = self.comboBox_2.currentData()
        name= self.comboBox_2.currentText()
        path= self.selectSegPath(id)
        path=''.join(path[0])
        # 计算参数 parm
        image = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
        row = image.shape[0]
        clo = image.shape[1]
        k = 0
        for j in range(clo):
            for i in range(row):
                if (image[i,j]> 127):
                    k += 1
        sum = clo * row
        parm1 = k / sum
        self.label_parm1.setText(str(parm1))
        cur,conn= self.getLink()
        sql= "update  input set parm1={} where id ={}".format(str(parm1),id) #注意此处与前一种形式的不同
        cur.execute(sql)
        conn.commit()
        conn.close()
    # 1.插入
    def insertRecord(self):
        sql = "insert into input(path,imgName) values(%s,%s)" #注意此处与前一种形式的不同
        parm=(1,2)
        cur,conn=  self.getLink()
        cur.execute(sql,parm)
        conn.commit()


    def insertOutPutRecord(self):
        sql = "insert into output (path,imgName) values(%s,%s)"  # 注意此处与前一种形式的不同
        parm = (1, 2)
        cur, conn = self.getLink()
        cur.execute(sql, parm)
        conn.commit()

    def selectPath(self,id):
        sql = "select path from input where id={}".format(id)
        cur, conn = self.getLink()
        cur.execute(sql)
        conn.commit()
        data = cur.fetchall()
        return data

    def selectImage(self, id):
        sql = "select id,image from input where id={}".format(id)
        cur, conn = self.getLink()
        cur.execute(sql)
        conn.commit()
        image = cur.fetchall()
        return image
    def selectSegPath(self,id):
        sql = "select segPath from output where parentId={}".format(id)
        cur, conn = self.getLink()
        cur.execute(sql)
        conn.commit()
        data = cur.fetchall()
        return data

    def seg(self,path):
        print("分割并调用网络模型")
        image = cv2.imread(path)
        # 从label中读取要分割的图像

        k = 0
        for i in range(1, 9):
            print("正在裁切第行")
            for j in range(1, 11):
                dst = image[(i - 1) * 256:i * 256, (j - 1) * 256:j * 256]
                print(dst.shape)
                # cv2.waitKey()
                k += 1
                cv2.imwrite(r'temp/input/{}.jpg'.format(k), dst)

                #  送入网络
                output=self.unetSeg(r'temp/input/{}.jpg'.format(k))
                output.save(r'temp/output/{}.jpg'.format(k))
    # 表2:分割后路径 时间 图片名称

    # 弹出部分
    def messageDialog(self):
        # 核心功能代码就两行，可以加到需要的地方
        msg_box=  QMessageBox.about(self, "数据库录入", "保存成功")
        # 弹出部分

    def warningDialog(self):
        # 核心功能代码就两行，可以加到需要的地方
        msg_box = QMessageBox(QMessageBox.Warning, '警告', '保存异常')
        msg_box.exec_()

    def myFun1(self,dir):
        image = Image.open(dir).convert("RGB")
        region = image.crop((0, 0, 256, 256))
        return region


    def unetSeg(self,dir):
        image = Image.open(dir).convert("RGB")
        unet = Unet()
        img = unet.detect_image(image)
        return img


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # os.system('python ./loginapp.py')
    window = PyQtMainEntry()
    window.show()
    sys.exit(app.exec_())
