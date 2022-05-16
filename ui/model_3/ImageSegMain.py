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
    QCheckBox, QGridLayout, QScrollArea, QPushButton, QDialog, QScrollBar, QHBoxLayout, QButtonGroup, QGroupBox, \
    QLineEdit
from PyQt5.QtCore import Qt,QSize
from PyQt5.uic.properties import QtWidgets, QtCore
from PyQt5 import QtCore, QtGui, QtWidgets
import ui.db as db
from ui import Compose
from ui.model_1.custom.listWidgets import FuncListWidget
from unet import Unet
import ui.model_3.imageConfig as  config
from PyQt5.QtChart import QChart, QChartView, QSplineSeries, QValueAxis
from PyQt5.QtWidgets import QApplication,QWidget, QVBoxLayout, QMainWindow
from PyQt5.QtCore import QPointF, Qt, QTimer
from PyQt5.QtGui import QPainter
import sys
import random
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
class ImageSegment(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.url = url
        self.ui()
        self.analysisOneBtn = QPushButton(self)

        self.analysisOneBtn.setStyleSheet(
            "QPushButton{color:rgb(0,0,0)}"  # 按键前景色
            "QPushButton{background-color:rgb(255,255,255)}"  # 按键背景色
            "QPushButton:hover{color:red}"  # 光标移动到上面后的前景色
            "QPushButton{border-radius:6px}"  # 圆角半径
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
            "QPushButton{border-image: url(model_3/icon/bingzhuangtu.png)}"
        )
        self.analysisOneBtn.clicked.connect(self.analysisOne)
        self.analysisOneBtn.setGeometry(650, 30, 55, 50)

        self.label1=QLabel(self)
        self.label1.setText("查看孔隙占比 ")
        self.label1.setGeometry(550, 33, 100, 50)

        self.label2 = QLabel(self)
        self.label2.setText("查看该组孔隙分布 ")
        self.label2.setGeometry(770, 33, 120,50)


        self.analysisGroupBtn=QPushButton(self)
        self.analysisGroupBtn.setGeometry(900, 30, 55,50)
        self.analysisGroupBtn.setStyleSheet(
            "QPushButton{color:rgb(0,0,0)}"  # 按键前景色
            "QPushButton{background-color:rgb(255,255,255)}"  # 按键背景色
            "QPushButton:hover{color:red}"  # 光标移动到上面后的前景色
            "QPushButton{border-radius:6px}"  # 圆角半径
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
            "QPushButton{border-image: url(model_3/icon/fenzu.png)}"
        )
        self.analysisGroupBtn.clicked.connect(self.analysisByGroup)


        self.iconLabel = QLabel(self)
        self.iconLabel.setGeometry(5, 10, 150, 50)
        # self.iconLabel.setText("")
        self.iconLabel.setPixmap(
            ImageQt.toqpixmap("model_3/icon/pislab.png").scaled(self.iconLabel.size(), Qt.KeepAspectRatio,
                                                                Qt.SmoothTransformation))

        self.InputLabel = QLabel(self)
        self.InputLabel.setGeometry(180, 150, 410, 308)
        self.InputLabel.setText("保存图像")
        self.InputLabel.setPixmap(ImageQt.toqpixmap("model_3/utils/white.png").scaled(self.InputLabel.size(), Qt.KeepAspectRatio,
                                                                    Qt.SmoothTransformation))
        self.OutPut = QLabel(self)
        self.OutPut.setGeometry(620, 150, 410, 308)
        self.OutPut.setText("保存图像")
        self.OutPut.setPixmap(
            ImageQt.toqpixmap("model_3/utils/white.png").scaled(self.InputLabel.size(), Qt.KeepAspectRatio,
                                                          Qt.SmoothTransformation))

    def ui(self):
        self.setFixedSize(1200,800)
        layout = QGridLayout()

        self.setLayout(layout)
        self.sc = QScrollArea(self)
        self.qw = QWidget()
        sql = "select id,path,imgName from input "
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
            btn= QPushButton(data[i][2], self)
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
        btn_group.buttonClicked[int].connect(self.checks)  # 组中按钮被点击时发出信号，其中的int就是按钮的id号，会向槽函数传递被点击按钮的id,而不是传递按钮

        self.sc.setMinimumSize(150, 700)
        self.sc.setGeometry(5,90,150,700)
        self.sc.setWidget(self.qw)

    def checks(self, id):
        print("checks")
        sql = "select path,imgName from input where id={}".format(id)
        cur, conn = db.getLink()
        cur.execute(sql)
        data = cur.fetchall()
        config.set_Id(id)

        self.InputLabel.setPixmap(ImageQt.toqpixmap(data[0][0]).scaled(self.InputLabel.size(), Qt.KeepAspectRatio,
                                                                       Qt.SmoothTransformation))
    def analysisByGroup(self):
        groupId= config.get_groupId()
        print("分组分析 组别"+ str(groupId))
        sql="select parm1,imgName from input where groupId={} order by imgName".format(groupId)
        cur,conn = db.getLink()
        cur.execute(sql)
        data= cur.fetchall()
        y=[]
        x=[]
        for i in range(len(data)):
            y.append(float(data[i][0]))
            x.append(str(i))
        print(y)
        print(x)

        # 创建画布
        plt.figure()
        plt.ylim(0.2, 0.7)
        plt.plot(x, y, marker='o', color='b', label='y1-data')
        # my_y_ticks = np.arange(0, 1, 0.1)
        # plt.yticks(my_y_ticks)
        # 横坐标名称
        plt.xlabel('图像序号')
        # 纵坐标名称
        plt.ylabel('孔隙度')
        # 保存图片到本地
        plt.savefig('pci.png')
        self.showDialog()

    def analysisOne(self):

        print("单一计算参数parm ")
        path=self.getSegPath()
        print("path "+path)
        # 计算参数 parm /Users/bryan/Code/pycharm/myunet/ui/model_2/temp/joinOut/500μm.png
        path="/Users/bryan/Code/pycharm/myunet/ui/"+path
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
        print("parm1 "+str(format(parm1, '.4f')))
        # self.label_parm1.setText(str(parm1))
        cur,conn= db.getLink()
        sql= "update  input set parm1={} where id ={}".format(str(format(parm1, '.4f')),config.get_Id()) #注意此处与前一种形式的不同

        y = np.array([parm1, 1-parm1])

        plt.pie(y,
                labels=['Pore', 'Rock'],  # 设置饼图标签
                colors=["#d5695d", "#5d8ca8", "#65a479", "#a564c9"],  # 设置饼图颜色
                explode=(0, 0.03),  # 第二部分突出显示，值越大，距离中心越远
                autopct='%.2f%%',  # 格式化输出百分比
                )
        plt.legend(['Pore', 'Rock'])
        plt.legend(loc='lower right')
        plt.title("岩石颗粒孔隙度占比饼状图")  # 设置标题
        # plt.show()
        plt.savefig('pie.png')
        self.OutPut.setPixmap(ImageQt.toqpixmap("./pie.png").scaled(self.OutPut.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        cur.execute(sql)
        conn.commit()
        conn.close()
    def getSegPath(self):
        print("获取分割 后的图片路径")
        sql="select segPath from  output where parentId={}".format(config.get_Id())
        cur,conn= db.getLink()
        cur.execute(sql)
        path = cur.fetchall()

        return  path[0][0]

    def showDialog(self):

        self.dialog = QDialog(self)
        self.dialog.resize(500, 350)
        self.dialog.setWindowIcon(QIcon('icon.png'))
        self.dialog.setWindowTitle('第'+str(config.get_groupId())+"组孔隙度分布折线图")
        self.picLabel=QLabel(self)
        # self.picLabel.setGeometry(5,5,450,330)

        self.picLabel.setPixmap(ImageQt.toqpixmap("./pci.png"))



        # # 创建确定和取消的按钮
        # ok_button = QPushButton('确定', self.dialog)
        # cancel_button = QPushButton('取消', self.dialog)

        # 将垂直布局添加到groupbox中
        # group.setLayout(group_layout)
        # group.setFixedSize(group.sizeHint())

        # 创建一个水平布局，并将两个按钮添加到布局中
        labe_layout=QHBoxLayout()
        labe_layout.addWidget(self.picLabel)

        button_layout = QHBoxLayout()
        # button_layout.addWidget(ok_button)
        # button_layout.addWidget(cancel_button)


        # 创建一个最外层的dialog垂直布局，将盒子和按钮布局加到这个布局中
        dialog_layout = QVBoxLayout()
        dialog_layout.addLayout(labe_layout)
        dialog_layout.addLayout(button_layout)

        # 设置这个对话框的布局
        self.dialog.setLayout(dialog_layout)
        self.dialog.exec_()
        return False



# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#
#     pic = ImageSegment()
#     pic.show()
#     sys.exit(app.exec_())

