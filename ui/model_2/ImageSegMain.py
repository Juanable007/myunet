import sys
import traceback
import time

import cv2
import requests

from PIL import ImageQt, Image
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QApplication, QMessageBox, QWidget, QVBoxLayout, QLabel, \
    QCheckBox, QGridLayout, QScrollArea, QPushButton, QDialog, QScrollBar, QHBoxLayout, QButtonGroup
from PyQt5.QtCore import Qt,QSize
from PyQt5.uic.properties import QtWidgets, QtCore
from PyQt5 import QtCore, QtGui, QtWidgets
import ui.db as db
from ui import Compose
from ui.model_1.custom.listWidgets import FuncListWidget
from unet import Unet
import ui.model_2.imageConfig as  config

class ImageSegment(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.url = url
        self.ui()
        self.segBtn = QPushButton(self)

        self.segBtn.setStyleSheet(
            "QPushButton{color:rgb(0,0,0)}"  # 按键前景色
            "QPushButton{background-color:rgb(255,255,255)}"  # 按键背景色
            "QPushButton:hover{color:red}"  # 光标移动到上面后的前景色
            "QPushButton{border-radius:6px}"  # 圆角半径
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
            "QPushButton{border-image: url(model_2/icon/处理.png)}"
        )
        self.segBtn.setGeometry(640, 30, 55,50)
        self.segBtn.clicked.connect(self.segAndJoin)



        # self.comboBox1 = QtWidgets.QComboBox(self)
        # self.comboBox1.setGeometry(QtCore.QRect(220, 45, 170, 20))
        # self.comboBox1.setObjectName("comboBox")
        # self.initCombobox()
        # self.comboBox1.currentIndexChanged['QString'].connect(self.refresh) # type: ignore

        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(400, 45, 170, 20))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("请选择模型")
        self.comboBox.addItem("轻量级模型")
        self.comboBox.addItem("全参数模型")

        self.iconLabel = QLabel(self)
        self.iconLabel.setGeometry(5, 10, 150, 50)
        # self.iconLabel.setText("")
        self.iconLabel.setPixmap(
            ImageQt.toqpixmap("model_2/icon/pislab.png").scaled(self.iconLabel.size(), Qt.KeepAspectRatio,
                                                                Qt.SmoothTransformation))

        self.InputLabel = QLabel(self)
        self.InputLabel.setGeometry(180, 150, 410, 308)
        self.InputLabel.setText("保存图像")
        self.InputLabel.setPixmap(ImageQt.toqpixmap("model_2/utils/white.png").scaled(self.InputLabel.size(), Qt.KeepAspectRatio,
                                                                    Qt.SmoothTransformation))

        self.OutPut = QLabel(self)
        self.OutPut.setGeometry(620, 150, 410, 308)
        self.OutPut.setText("保存图像")
        self.OutPut.setPixmap(ImageQt.toqpixmap("model_2/utils/white.png").scaled(self.InputLabel.size(), Qt.KeepAspectRatio,
                                                                          Qt.SmoothTransformation))
    def initCombobox(self):
        cur, conn = db.getLink()
        sql="select  groupId from  input group by groupId;"
        cur.execute(sql)
        data=cur.fetchall()
        length = len(data)
        self.comboBox1.addItem("请选择组别")
        for i in range(length):
            self.comboBox1.addItem(data[i][0])
    def refresh(self):
        groupId=self.comboBox1.currentText()
        config.set_groupId(groupId)
        self.ui()
        QApplication.processEvents()



    def ui(self):
        self.setFixedSize(1050,700)

        # total = len(self.url)
        num= config.get_num()
        print("+"+str(num))

        layout = QGridLayout()

        self.setLayout(layout)
        self.sc = QScrollArea(self)
        self.qw = QWidget()
        print("gid= "+str(config.get_groupId()))
        sql = "select  id ,path,imgName,parm1, groupId, create_time from  input where groupId={}".format(
            config.get_groupId())
        cur, conn = db.getLink()
        cur.execute(sql)
        data = cur.fetchall()
        total=len(data)
        self.qw.setMinimumSize(135,96*total)
        btn_group = QButtonGroup(self)
        for i in  range(total):
            tmp = QWidget(self.qw)
            vl = QVBoxLayout()
            label= QLabel()
            label.setFixedSize(120,90)
            label.setPixmap(ImageQt.toqpixmap(data[i][1]).scaled(label.size(),Qt.KeepAspectRatio,Qt.SmoothTransformation))
            btn= QPushButton(str(data[i][2]), self)
            btn.setStyleSheet(
                "QPushButton{color:rgb(0,0,0)}"  # 按键前景色
                "QPushButton{background-color:rgb(255,255,255)}"  # 按键背景色
                "QPushButton:hover{color:red}"  # 光标移动到上面后的前景色
                "QPushButton{border-radius:6px}"  # 圆角半径
                "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
            )
            btn_group.addButton(btn,data[i][0])

            vl.addWidget(label)
            vl.addWidget(btn)
            tmp.setLayout(vl)
            tmp.move(128 * (i % 1), 130 * int(i / 1))
        # btn_group.buttonClicked.connect(self.cao)  # 组中按钮被点击时发出信号
        btn_group.buttonClicked[int].connect(self.checks)  # 组中按钮被点击时发出信号，其中的int就是按钮的id号，会向槽函数传递被点击按钮的id,而不是传递按钮
        # btn_group.buttonToggled.connect(self.cao2)  # 当按钮组中的按钮被切换状态时, 发射此信号，会向槽函数传递状态发生改变的按钮

        self.sc.setMinimumSize(150, 700)
        self.sc.setGeometry(5,90,150,700)
        self.sc.setWidget(self.qw)

    def checks(self, id):
        sql = "select path,imgName from input where id={}".format(id)
        cur,conn = db.getLink()
        cur.execute(sql)
        data=cur.fetchall()

        self.InputLabel.setPixmap(ImageQt.toqpixmap(data[0][0]).scaled(self.InputLabel.size(), Qt.KeepAspectRatio,
                                                                          Qt.SmoothTransformation))
        segPath = self.selectSegPath(id)
        config.set_Id(id)
        config.set_path(data[0][0])
        config.set_name(data[0][1])
        if (len(segPath) != 0):
            segPath = ''.join(segPath[0])
            # 之前已经分割过了,把分割好的图像从数据库查出放到目录下.
            self.OutPut.setPixmap(ImageQt.toqpixmap(segPath).scaled(self.OutPut.size(),
                                                                          Qt.KeepAspectRatio, Qt.SmoothTransformation))
        else:

            self.OutPut.setPixmap(ImageQt.toqpixmap('model_2/utils/white.png').scaled(self.OutPut.size(),
                                                                                      Qt.KeepAspectRatio,
                                                                                      Qt.SmoothTransformation))
            print("---")
    def selectSegPath(self,id):
        sql = "select segPath from output where parentId={}".format(id)
        cur, conn = db.getLink()
        cur.execute(sql)
        conn.commit()
        data = cur.fetchall()
        return data

    def segAndJoin(self):
        print("分割拼接方法")
        #  获取要分割图像的路径
        id = config.get_Id()
        # inputPath = 'temp/input/'
        outPath = 'model_2/temp/output/'
        joinOutPath = 'model_2/temp/joinOut/'
        # 输出文件名称
        outSavePathName = config.get_name()
        path = config.get_path()
        # path = ''.join(path[0])
        #  裁切
        start = time.time()
        try:
            self.seg(path)
            end = time.time()
            #  拼接结果
            Compose.image_compose(outPath, joinOutPath + outSavePathName)
            #  返回页面
            self.OutPut.setPixmap(
                ImageQt.toqpixmap(joinOutPath + outSavePathName).scaled(self.OutPut.size(), Qt.KeepAspectRatio,
                                                                        Qt.SmoothTransformation))
            #     落表2 输出路径,输出名称
            sql = "insert into output (parentId,segPath,segName,segImage) values(%s,%s,%s,%s)"  # 注意此处与前一种形式的不同
            file = open(joinOutPath + outSavePathName, "rb")
            img = file.read()
            parm = (id, joinOutPath + outSavePathName, outSavePathName, img)
            cur, conn = db.getLink()
            cur.execute(sql, parm)
            file.close()
            conn.commit()
            conn.close()
        except:
            print("分割方法出现异常")
            traceback.print_exc()
        finally:
            print("调用模型总用时: {}".format(end - start))

    def seg(self, path):
        print("分割并调用网络模型")
        image = cv2.imread(path)
        # 从label中读取要分割的图像

        k = 0
        for i in range(1, 9):
            print("正在裁切第"+str(i)+"行")
            for j in range(1, 11):
                dst = image[(i - 1) * 256:i * 256, (j - 1) * 256:j * 256]
                print(dst.shape)
                # cv2.waitKey()
                k += 1
                cv2.imwrite('model_2/temp/input/{}.jpg'.format(k), dst)

                #  送入网络
                output = self.unetSeg('model_2/temp/input/{}.jpg'.format(k))
                output.save('model_2/temp/output/{}.jpg'.format(k))

    def unetSeg(self, dir):
        image = Image.open(dir).convert("RGB")
        unet = Unet()
        img = unet.detect_image(image)
        return img

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     url=['https://pic2.zhimg.com/aadd7b895_xs.jpg?source=1940ef5c', 'https://pic2.zhimg.com/50/v2-60f7b5c071d378a34a3a6c489c3fdacc_hd.jpg?source=1940ef5c', 'https://pic2.zhimg.com/80/v2-60f7b5c071d378a34a3a6c489c3fdacc_720w.jpg?source=1940ef5c', 'https://pic1.zhimg.com/50/v2-aa7d74fe48183d16a571278a012ff759_hd.jpg?source=1940ef5c', 'https://pic4.zhimg.com/50/v2-011ac12cbfe61ebc411ba437fac88780_hd.jpg?source=1940ef5c', 'https://pic1.zhimg.com/50/v2-dea9876e70b0a0b08b635796eb2c86da_hd.jpg?source=1940ef5c']
#
#     pic = Picture(url=url)
#     pic.show()
#     sys.exit(app.exec_())

