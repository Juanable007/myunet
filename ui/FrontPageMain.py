import sys
sys.path.append("/Users/bryan/Code/pycharm/myunet/ui/model_1/custom")
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMainWindow
from PIL import ImageQt
from FrontPage import Ui_MainWindow
from ui.model_1 import main as model_1
class FrontMainEntry(QMainWindow, Ui_MainWindow):
    def __init__(self):

        super().__init__()
        self.setupUi(self)
        self.CutFlag = False
        self.SegmentFlag = False
        # self.pushButton_2.setStyleSheet("QPushButton{border-image: url(shezhi.png)}")
        # self.button.setStyleSheet("QPushButton{background-image: url(img/1.png)}")

        # self.btn.setStyleSheet("QPushButton{border-image: url(shezhi.png)}")
        self.btn.setStyleSheet(
            "QPushButton{color:rgb(0,0,0)}"  # 按键前景色
            "QPushButton{background-color:rgb(255,255,255)}"  # 按键背景色
            "QPushButton:hover{color:red}"  # 光标移动到上面后的前景色
            "QPushButton{border-radius:6px}"  # 圆角半径
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
            "QPushButton{border-image: url(./icon/tupianchuli.png)}"
        )
        self.btn2.setStyleSheet(
            "QPushButton{color:rgb(0,0,0)}"  # 按键前景色
            "QPushButton{background-color:rgb(255,255,255)}"  # 按键背景色
            "QPushButton:hover{color:red}"  # 光标移动到上面后的前景色
            "QPushButton{border-radius:6px}"  # 圆角半径
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
            "QPushButton{border-image: url(./icon/图像处理.png)}"
        )
        self.btn3.setStyleSheet(
            "QPushButton{color:rgb(0,0,0)}"  # 按键前景色
            "QPushButton{background-color:rgb(255,255,255)}"  # 按键背景色
            "QPushButton:hover{color:red}"  # 光标移动到上面后的前景色
            "QPushButton{border-radius:6px}"  # 圆角半径
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
            "QPushButton{border-image: url(./icon/数据处理.png)}"
        )
        self.btn4.setStyleSheet(
            "QPushButton{color:rgb(0,0,0)}"  # 按键前景色
            "QPushButton{background-color:rgb(255,255,255)}"  # 按键背景色
            "QPushButton:hover{color:red}"  # 光标移动到上面后的前景色
            "QPushButton{border-radius:6px}"  # 圆角半径
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
            "QPushButton{border-image: url(./icon/资源管理.png)}"
        )
        self.btn5.setStyleSheet(
            "QPushButton{color:rgb(0,0,0)}"  # 按键前景色
            "QPushButton{background-color:rgb(255,255,255)}"  # 按键背景色
            "QPushButton:hover{color:red}"  # 光标移动到上面后的前景色
            "QPushButton{border-radius:6px}"  # 圆角半径
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
            "QPushButton{border-image: url(./icon/用户管理.png)}"
        )
        self.btn6.setStyleSheet(
            "QPushButton{color:rgb(0,0,0)}"  # 按键前景色
            "QPushButton{background-color:rgb(255,255,255)}"  # 按键背景色
            "QPushButton:hover{color:red}"  # 光标移动到上面后的前景色
            "QPushButton{border-radius:6px}"  # 圆角半径
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
            "QPushButton{border-image: url(./icon/系统设置.png)}"
        )
        self.label.setPixmap(
            ImageQt.toqpixmap("./icon/油田.jpeg").scaled(self.label.size(), Qt.KeepAspectRatio,
                                                                    Qt.SmoothTransformation))

        # self.btn.resize(self.btn.sizeHint())
        # self.btn.setShortcut('L')
        # self.btn.enterEvent()
        # self.btn.clicked.connect(self.model_1)
    # def enterEvent(self):
    #     print("鼠标悬停")'


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = FrontMainEntry()

    window.show()
    WinModel_1=model_1.MyApp()
    # newWin = NewWindow()
    window.btn.clicked.connect(WinModel_1.show)
    sys.exit(app.exec_())