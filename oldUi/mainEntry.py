import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QApplication, QMessageBox
from PIL import ImageQt, Image
from unet import Unet
from mainForm import Ui_MainWindow


def myFun1(dir):
    image = Image.open(dir).convert("RGB")
    region = image.crop((0, 0, 256, 256))
    return region


def myFun2(dir):
    img2 = myFun1(dir)
    unet = Unet()
    img2 = unet.detect_image(img2)
    return img2


class PyQtMainEntry(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.CutFlag = False
        self.SegmentFlag = False

    def btnOpen_Clicked(self):
        imgName, imgType = QFileDialog.getOpenFileName(self.centralwidget, "打开图片", "","*.jpg;;All Files(*)")
        img = QtGui.QPixmap(imgName).scaled(self.label_InputImg.size(),Qt.KeepAspectRatio,Qt.SmoothTransformation)
        self.lineEdit.setText(imgName)
        self.textEdit_2.setText()
        self.label_InputImg.setPixmap(img)

    def btnCut_Clicked(self):
        if self.lineEdit.text() == '':
            self.showMessageBox1()
        else:
            ImgCut = myFun1(self.lineEdit.text())
            self.label_CutImg.setPixmap(ImageQt.toqpixmap(ImgCut).scaled(self.label_CutImg.size(),Qt.KeepAspectRatio,Qt.SmoothTransformation))
            self.CutFlag = True

    def btnSegment_Clicked(self):
        if self.CutFlag is False:
            self.showMessageBox2()
        else:
            ImgSegment = myFun2(self.lineEdit.text())
            self.label_SegImg.setPixmap(ImageQt.toqpixmap(ImgSegment).scaled(self.label_SegImg.size(),Qt.KeepAspectRatio,Qt.SmoothTransformation))
            self.SegmentFlag = True

    def btnSave_Clicked(self):
        if self.SegmentFlag is False:
            self.showMessageBox3()
        else:
            screen = QApplication.primaryScreen()
            pix = screen.grabWindow(self.label_SegImg.winId())
            fd, type = QFileDialog.getSaveFileName(self.centralwidget, "保存图片", "segment.jpg", "*.jpg;;All Files(*)")
            pix.save(fd)

    def showMessageBox1(self):
        QMessageBox.warning(self, "警告", "您未选择图片，请选择！", QMessageBox.Ok, QMessageBox.Ok)

    def showMessageBox2(self):
        QMessageBox.warning(self, "警告", "您选择的图片不符合要求，请先执行切分操作！", QMessageBox.Ok, QMessageBox.Ok)

    def showMessageBox3(self):
        QMessageBox.warning(self, "警告", "您未执行分割操作，请先执行分割操作！", QMessageBox.Ok, QMessageBox.Ok)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PyQtMainEntry()
    window.show()
    sys.exit(app.exec_())
