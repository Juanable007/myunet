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
import ui.model_3.imageConfig as  config
from PyQt5.QtChart import QChart, QChartView, QSplineSeries, QValueAxis
from PyQt5.QtWidgets import QApplication,QWidget, QVBoxLayout, QMainWindow
from PyQt5.QtCore import QPointF, Qt, QTimer
from PyQt5.QtGui import QPainter
import sys
import random

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
            "QPushButton{border-image: url(./icon/处理.png)}"
        )
        self.segBtn.setGeometry(640, 30, 55,50)


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
            ImageQt.toqpixmap("./icon/pislab.png").scaled(self.iconLabel.size(), Qt.KeepAspectRatio,
                                                                Qt.SmoothTransformation))

        self.InputLabel = QLabel(self)
        self.InputLabel.setGeometry(180, 150, 410, 308)
        self.InputLabel.setText("保存图像")
        self.InputLabel.setPixmap(ImageQt.toqpixmap("./utils/white.png").scaled(self.InputLabel.size(), Qt.KeepAspectRatio,
                                                                    Qt.SmoothTransformation))

    def ui(self):
        self.setFixedSize(1050,700)
        layout = QGridLayout()

        self.setLayout(layout)
        self.sc = QScrollArea(self)
        self.qw = QWidget()

        total=10
        self.qw.setMinimumSize(135,96*total)
        btn_group = QButtonGroup(self)
        for i in  range(total):
            tmp = QWidget(self.qw)
            vl = QVBoxLayout()
            label= QLabel()
            label.setFixedSize(120,90)
            label.setPixmap(ImageQt.toqpixmap("./utils/white.png").scaled(label.size(),Qt.KeepAspectRatio,Qt.SmoothTransformation))
            btn= QPushButton(str(i), self)
            btn.setStyleSheet(
                "QPushButton{color:rgb(0,0,0)}"  # 按键前景色
                "QPushButton{background-color:rgb(255,255,255)}"  # 按键背景色
                "QPushButton:hover{color:red}"  # 光标移动到上面后的前景色
                "QPushButton{border-radius:6px}"  # 圆角半径
                "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
            )
            btn_group.addButton(btn,1)

            vl.addWidget(label)
            vl.addWidget(btn)
            tmp.setLayout(vl)
            tmp.move(128 * (i % 1), 130 * int(i / 1))

        self.sc.setMinimumSize(150, 700)
        self.sc.setGeometry(5,90,150,700)
        self.sc.setWidget(self.qw)

    def checks(self, id):
        sql = "select path,imgName from input where id={}".format(id)




if __name__ == '__main__':
    app = QApplication(sys.argv)

    pic = ImageSegment()
    pic.show()
    sys.exit(app.exec_())

