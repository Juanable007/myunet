# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EasyLoad.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import sys

class Ui_Form(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.setObjectName("Form")
        self.resize(678, 450)
        self.label = QtWidgets.QLabel(self)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 去边框
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.label.setGeometry(QtCore.QRect(0, 0, 681, 451))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/Administrator/Desktop/background.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(40, 50, 151, 51))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:/Users/Administrator/Desktop/Fore.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(50, 120, 141, 41))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("C:/Users/Administrator/Desktop/tabitem-focus.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(50, 170, 141, 41))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("C:/Users/Administrator/Desktop/tabitem-hover.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(50, 270, 141, 41))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("C:/Users/Administrator/Desktop/tabitem-hover.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(50, 220, 141, 41))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("C:/Users/Administrator/Desktop/tabitem-hover.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(90, 130, 101, 21))
        self.label_7.setStyleSheet("font-family:微软雅黑;")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(90, 180, 101, 21))
        self.label_8.setStyleSheet("font-family:微软雅黑;")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self)
        self.label_9.setGeometry(QtCore.QRect(90, 280, 101, 21))
        self.label_9.setStyleSheet("font-family:微软雅黑;")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self)
        self.label_10.setGeometry(QtCore.QRect(90, 230, 101, 21))
        self.label_10.setStyleSheet("font-family:微软雅黑;")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self)
        self.label_11.setGeometry(QtCore.QRect(200, 115, 231, 121))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("C:/Users/Administrator/Desktop/background.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self)
        self.label_12.setGeometry(QtCore.QRect(190, 230, 251, 151))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("C:/Users/Administrator/Desktop/未标题-1.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self)
        self.label_13.setGeometry(QtCore.QRect(280, 260, 101, 21))
        self.label_13.setStyleSheet("font-family:微软雅黑;\n"
"color:white;\n"
"font-size:15px;")
        self.label_13.setObjectName("label_13")
        self.radioButton = QtWidgets.QRadioButton(self)
        self.radioButton.setGeometry(QtCore.QRect(230, 300, 89, 16))
        self.radioButton.setStyleSheet("font-family:微软雅黑;\n"
"color:white;")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self)
        self.radioButton_2.setGeometry(QtCore.QRect(320, 300, 89, 16))
        self.radioButton_2.setStyleSheet("font-family:微软雅黑;\n"
"color:white;")
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton_17 = QtWidgets.QPushButton(self)
        self.pushButton_17.setGeometry(QtCore.QRect(310, 330, 81, 25))
        self.pushButton_17.setStyleSheet("QPushButton{\n"
"    color:White;\n"
"    font-family:微软雅黑;\n"
"    border: 2px solid DarkGray;\n"
"    background:rgb(255, 255, 255, 60);\n"
"}\n"
"QPushButton:hover{\n"
"    border: 1px solid Gray;\n"
"    background:rgb(255, 255, 255, 90);\n"
"}\n"
"QPushButton:pressed{\n"
"    border: 2px solid DarkGray;\n"
"    background:rgb(255, 255, 255, 30);\n"
"}")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_11 = QtWidgets.QPushButton(self)
        self.pushButton_11.setGeometry(QtCore.QRect(580, 50, 16, 16))
        self.pushButton_11.setStyleSheet("QPushButton{\n"
"    background:#6C6C6C;\n"
"    color:white;\n"
"    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:16px;border-radius: 8px;font-family: 微软雅黑;\n"
"}\n"
"QPushButton:hover{                    \n"
"    background:#9D9D9D;\n"
"}\n"
"QPushButton:pressed{\n"
"    border: 1px solid #3C3C3C!important;\n"
"}")
        self.pushButton_11.setText("")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self)
        self.pushButton_12.setGeometry(QtCore.QRect(610, 50, 16, 16))
        self.pushButton_12.setStyleSheet("QPushButton{\n"
"    background:#CE0000;\n"
"    color:white;\n"
"    box-shadow: 1px 1px 3px rgba(0,0,0,0.3);font-size:16px;border-radius: 8px;font-family: 微软雅黑;\n"
"}\n"
"QPushButton:hover{                    \n"
"    background:#FF2D2D;\n"
"}\n"
"QPushButton:pressed{\n"
"    border: 1px solid #3C3C3C!important;\n"
"    background:#AE0000;\n"
"}")
        self.pushButton_12.setText("")
        self.pushButton_12.setObjectName("pushButton_12")
        self.label_14 = QtWidgets.QLabel(self)
        self.label_14.setGeometry(QtCore.QRect(290, 140, 101, 21))
        self.label_14.setStyleSheet("font-family:微软雅黑;\n"
"font-size:15px;\n"
"color:gray;")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self)
        self.label_15.setGeometry(QtCore.QRect(290, 170, 121, 21))
        self.label_15.setStyleSheet("font-family:微软雅黑;\n"
"font-size:15px;\n"
"color:gray;")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self)
        self.label_16.setGeometry(QtCore.QRect(220, 140, 61, 61))
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("res/头像.jpg"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self)
        self.label_17.setGeometry(QtCore.QRect(420, 100, 221, 291))
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap("C:/Users/Administrator/Desktop/未标题-2.png"))
        self.label_17.setScaledContents(True)
        self.label_17.setObjectName("label_17")
        self.pushButton_18 = QtWidgets.QPushButton(self)
        self.pushButton_18.setGeometry(QtCore.QRect(50, 124, 141, 33))
        self.pushButton_18.setStyleSheet("QPushButton{\n"
"    color:White;\n"
"    font-family:微软雅黑;\n"
"    border: 1px;\n"
"    background:rgb(255, 255, 255, 60);\n"
"}\n"
"QPushButton:hover{\n"
"    background:rgb(255, 255, 255, 90);\n"
"}\n"
"QPushButton:pressed{\n"
"    background:rgb(255, 255, 255, 30);\n"
"}")
        self.pushButton_18.setText("")
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self)
        self.pushButton_19.setGeometry(QtCore.QRect(50, 175, 141, 33))
        self.pushButton_19.setStyleSheet("QPushButton{\n"
"    color:White;\n"
"    font-family:微软雅黑;\n"
"    border: 1px;\n"
"    background:rgb(255, 255, 255, 60);\n"
"}\n"
"QPushButton:hover{\n"
"    background:rgb(255, 255, 255, 90);\n"
"}\n"
"QPushButton:pressed{\n"
"    background:rgb(255, 255, 255, 30);\n"
"}")
        self.pushButton_19.setText("")
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self)
        self.pushButton_20.setGeometry(QtCore.QRect(50, 270, 141, 33))
        self.pushButton_20.setStyleSheet("QPushButton{\n"
"    color:White;\n"
"    font-family:微软雅黑;\n"
"    border: 1px;\n"
"    background:rgb(255, 255, 255, 60);\n"
"}\n"
"QPushButton:hover{\n"
"    background:rgb(255, 255, 255, 90);\n"
"}\n"
"QPushButton:pressed{\n"
"    background:rgb(255, 255, 255, 30);\n"
"}")
        self.pushButton_20.setText("")
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self)
        self.pushButton_21.setGeometry(QtCore.QRect(50, 219, 141, 33))
        self.pushButton_21.setStyleSheet("QPushButton{\n"
"    color:White;\n"
"    font-family:微软雅黑;\n"
"    border: 1px;\n"
"    background:rgb(255, 255, 255, 60);\n"
"}\n"
"QPushButton:hover{\n"
"    background:rgb(255, 255, 255, 90);\n"
"}\n"
"QPushButton:pressed{\n"
"    background:rgb(255, 255, 255, 30);\n"
"}")
        self.pushButton_21.setText("")
        self.pushButton_21.setObjectName("pushButton_21")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_7.setText(_translate("Form", "DashBoard"))
        self.label_8.setText(_translate("Form", "ModManager"))
        self.label_9.setText(_translate("Form", "About"))
        self.label_10.setText(_translate("Form", "ClientLauncher"))
        self.label_13.setText(_translate("Form", "QuikStart"))
        self.radioButton.setText(_translate("Form", "Mod启动"))
        self.radioButton_2.setText(_translate("Form", "开端启动"))
        self.pushButton_17.setText(_translate("Form", "开始"))
        self.label_14.setText(_translate("Form", "Welcome, "))
        self.label_15.setText(_translate("Form", "%username% !"))
    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = e.globalPos() - self.pos()
            e.accept()
    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.m_drag = False
    def mouseMoveEvent(self, e):
        try:
            if Qt.LeftButton and self.m_drag:
                self.move(e.globalPos() - self.m_DragPosition)
                e.accept()
        except:
            print("错误代码:000x0")

def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = Ui_Form()
    gui.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()