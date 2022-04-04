import traceback

import cv2
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import matplotlib.pyplot as plt

from ui.model_1.custom.stackedWidget import StackedWidget
from ui.model_1.custom.listWidgets import FuncListWidget, UsedListWidget
from ui.model_1.custom.graphicsView import GraphicsView
import ui.model_1.pathConfig as config
import ui.db as db
from ui.model_1.custom.treeView import FileSystemTreeView


class MyApp(QMainWindow):

    def __init__(self):
        super(MyApp, self).__init__()

        self.tool_bar = self.addToolBar('工具栏')
        self.action_right_rotate = QAction(QIcon("model_1/icons/右旋转.png"), "向右旋转90", self)
        self.action_left_rotate = QAction(QIcon("model_1/icons/左旋转.png"), "向左旋转90°", self)
        self.action_histogram = QAction(QIcon("model_1/icons/直方图.png"), "直方图", self)
        self.action_right_rotate.triggered.connect(self.right_rotate)
        self.action_left_rotate.triggered.connect(self.left_rotate)
        self.action_histogram.triggered.connect(self.histogram)
        self.tool_bar.addActions((self.action_left_rotate, self.action_right_rotate, self.action_histogram))

        self.useListWidget = UsedListWidget(self)
        self.funcListWidget = FuncListWidget(self)
        self.stackedWidget = StackedWidget(self)
        self.fileSystemTreeView = FileSystemTreeView(self)
        self.graphicsView = GraphicsView(self)

        self.dock_file = QDockWidget(self)
        self.dock_file.setWidget(self.fileSystemTreeView)
        self.dock_file.setTitleBarWidget(QLabel('目录'))
        self.dock_file.setFeatures(QDockWidget.NoDockWidgetFeatures)

        self.dock_func = QDockWidget(self)
        self.dock_func.setWidget(self.funcListWidget)
        self.dock_func.setTitleBarWidget(QLabel('图像操作'))
        self.dock_func.setFeatures(QDockWidget.NoDockWidgetFeatures)

        self.dock_used = QDockWidget(self)
        self.dock_used.setWidget(self.useListWidget)
        self.dock_used.setTitleBarWidget(QLabel('已选操作'))
        self.dock_used.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.dock_used.setFeatures(QDockWidget.NoDockWidgetFeatures)

        self.dock_attr = QDockWidget(self)
        self.dock_attr.setWidget(self.stackedWidget)
        self.dock_attr.setTitleBarWidget(QLabel('属性'))
        self.dock_attr.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.dock_attr.close()

        self.setCentralWidget(self.graphicsView)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dock_file)
        self.addDockWidget(Qt.TopDockWidgetArea, self.dock_func)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock_used)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock_attr)

        # 保存部分

        self.saveButton = QPushButton(self)

        self.saveButton.setGeometry(960, 62, 40, 40)
        # self.saveButton.setObjectName('start')
        # self.saveButton.setText('保存图像')

        self.saveButton.setStyleSheet(
            "QPushButton{color:rgb(0,0,0)}"  # 按键前景色
            "QPushButton{background-color:rgb(255,255,255)}"  # 按键背景色
            "QPushButton:hover{color:red}"  # 光标移动到上面后的前景色
            "QPushButton{border-radius:6px}"  # 圆角半径
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
            "QPushButton{border-image: url(./model_1/icons/baocun.png)}"
        )

        self.saveButton.clicked.connect(self.saveImg)

        self.saveLabel=QLabel(self)
        self.saveLabel.setGeometry(955, 102, 60, 20)
        self.saveLabel.setText("保存图像")


        self.groupEdit = QLineEdit(self)  # 创建对象
        self.groupEdit.setGeometry(800, 75, 60, 20)
        self.groupLabel=QLabel(self)
        self.groupLabel.setGeometry(730, 75, 60, 20)
        self.groupLabel.setText("设置组别: ")
        # self.saveButton.show()



        self.setWindowTitle('图像预处理模块')
        self.setWindowIcon(QIcon('model_1/icons/main.png'))
        self.src_img = None
        self.cur_img = None

    def update_image(self):
        print("update_image")
        if self.src_img is None:
            return
        img = self.process_image()

        self.cur_img = img
        self.graphicsView.update_image(img)

    def change_image(self, img):
        print("change_image")
        self.src_img = img
        img = self.process_image()
        self.cur_img = img
        self.graphicsView.change_image(img)

    def process_image(self):
        print("process_image")
        img = self.src_img.copy()
        for i in range(self.useListWidget.count()):
            img = self.useListWidget.item(i)(img)
        cv2.imwrite('temp/preProcess_image.png', img)
        return img

    def right_rotate(self):
        self.graphicsView.rotate(90)

    def left_rotate(self):
        self.graphicsView.rotate(-90)

    def histogram(self):
        color = ('b', 'g', 'r')
        for i, col in enumerate(color):
            histr = cv2.calcHist([self.cur_img], [i], None, [256], [0, 256])
            histr = histr.flatten()
            plt.plot(range(256), histr, color=col)
            plt.xlim([0, 256])
        plt.show()

    def saveImg(self):
        # 路径和名称
        print("保存图片数据")
        try:
            # 全路径
            path = config.get_path()
            name = path.split("/")[-1]
            groupId=self.groupEdit.text()
            fp = open("model_3/temp/preProcess_image.png", 'rb')
            img = fp.read()
            fp.close()
            sql = "insert into input(path,imgName,image,groupId) values(%s,%s,%s,%s)"  # 注意此处与前一种形式的不同
            parm = (path, name, img,groupId)
            cur, conn = db.getLink()
            cur.execute(sql, parm)
            conn.commit()
            self.messageDialog()
        except:
            traceback.print_exc()
            self.warningDialog()
        finally:
            conn.close()
        # 弹出部分

    def messageDialog(self):
        # 核心功能代码就两行，可以加到需要的地方
        msg_box = QMessageBox.about(self, "数据库录入", "保存成功")
        # 弹出部分

    def warningDialog(self):
        # 核心功能代码就两行，可以加到需要的地方
        msg_box = QMessageBox(QMessageBox.Warning, '警告', '保存异常')
        msg_box.exec_()
#
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     # app.setStyleSheet(open('./custom/styleSheet.qss', encoding='utf-8').read())
#     window = MyApp()
#     window.show()
#     sys.exit(app.exec_())
