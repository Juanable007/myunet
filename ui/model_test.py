import os
import sys
import traceback
import requests

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QApplication, QMessageBox, QWidget, QVBoxLayout, QLabel, \
    QCheckBox, QGridLayout, QScrollArea, QPushButton, QDialog, QScrollBar, QHBoxLayout, QDockWidget
from PIL import ImageQt, Image
from unet import Unet
from model_1 import Ui_MainWindow
from imageshow import Ui_MainWindow as imageshowUi
import pymysql
import cv2
import time
import Compose
from treeView import  FileSystemTreeView


class Model_1MainEntry(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.CutFlag = False
        self.SegmentFlag = False


        self.fileSystemTreeView = FileSystemTreeView(self)

        self.dockWidget_3 = QDockWidget(self)
        self.doc
        self.dockWidget_3.setWidget(self.fileSystemTreeView)
        self.dockWidget_3.setTitleBarWidget(QLabel('目录'))
        self.dockWidget_3.setFeatures(QDockWidget.NoDockWidgetFeatures)


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    window = Model_1MainEntry()

    window.show()
    # newWin = NewWindow()
    # window.pushButton_2.clicked.connect(newWin.show)
    sys.exit(app.exec_())