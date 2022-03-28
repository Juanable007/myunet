import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets

from ui.model_4.Tools import *


class UserApp(QMainWindow):

    def __init__(self):
        super(UserApp, self).__init__()

        # 创建数据库
        # Tools.createDb()
        # 创建ui布局
        self.initMainUi()
        # 初始化表格
        self.initTable()

    # def initTable(self):
    #     pass
    #
    # def initTable(self):
    #     pass

    def initMainUi(self):
        # 设置主界面的大小，标题及图标
        self.resize(1200, 700)
        self.setWindowTitle('资源管理')
        self.setWindowIcon(QIcon('ui/icon/用户管理.png'))

        # 第二层的QWidget控件
        self.qwidget = QWidget()

        # 栅格布局
        grid = QGridLayout()

        # 创建表格控件和按钮控件
        self.tablewidget = QTableWidget()
        self.tablewidget2 = QTableWidget()

        # 设置控件在栅格中的位置
        grid.addWidget(self.tablewidget, 2, 1, 1, 2)
        grid.addWidget(self.tablewidget2, 4, 1, 1, 2)
        self.label1 = QLabel("已分割完成资源")
        self.label2 = QLabel("未完成资源")
        self.label1.setAlignment(Qt.AlignCenter)
        self.label2.setAlignment(Qt.AlignCenter)
        self.label1.setFont(QFont("Roman times", 18, QFont.Bold))
        self.label2.setFont(QFont("Roman times", 18, QFont.Bold))

        grid.addWidget(self.label1, 1, 1, 1, 2)
        grid.addWidget(self.label2, 3, 1, 1, 2)

        # 添加栅格布局到qwidget
        self.qwidget.setLayout(grid)

        # 设置qwidget到主界面中
        self.setCentralWidget(self.qwidget)

    def initTable(self):
        # 设置表格的列数为4
        self.tablewidget.setColumnCount(9)
        self.tablewidget2.setColumnCount(9)

        # 水平和垂直方向设置为正好填满表格
        self.tablewidget.horizontalHeader().setStretchLastSection(True)
        self.tablewidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tablewidget.setColumnWidth(8, 90)

        # 水平和垂直方向设置为正好填满表格
        self.tablewidget2.horizontalHeader().setStretchLastSection(True)
        self.tablewidget2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tablewidget2.setColumnWidth(8, 90)

        # 设置表格的表头，并设置为不可编辑
        headerlabels = ['id', 'parentId', '原图路径', '名称', '组别', '孔隙度', "分割图名", '备注', '操作']
        self.tablewidget.setHorizontalHeaderLabels(headerlabels)
        self.tablewidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablewidget.setStyleSheet(
            "QHeaderView::section{background-color:rgb(155, 194, 230);font:15pt '宋体';color: black;};")

        # 设置表格的表头，并设置为不可编辑
        headerlabels2 = ['id', 'parentId', '原图路径', '名称', '组别', '孔隙度', "分割图名", '备注', '操作']
        self.tablewidget2.setHorizontalHeaderLabels(headerlabels2)
        self.tablewidget2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablewidget2.setStyleSheet(
            "QHeaderView::section{background-color:rgb(155, 194, 230);font:15pt '宋体';color: black;};")

        # 隐藏id列，不显示数据的id也就是主键，这里的主键只用来删除和修改数据时使用
        self.tablewidget.setColumnHidden(0, True);
        self.tablewidget.setColumnHidden(1, True);

        self.tablewidget2.setColumnHidden(0, True);
        self.tablewidget2.setColumnHidden(1, True);

        # 不显示单元格
        self.tablewidget.setShowGrid(True)

        self.tablewidget2.setShowGrid(True)

        # 设置表格选择行为为 只能一行一行选择
        self.tablewidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.tablewidget2.setSelectionBehavior(QAbstractItemView.SelectRows)

        # 初始化表格数据
        self.flushTable()
        self.flushNoCompleteTable()

    def flushTable(self):
        # 从数据表中获取数据
        data = Tools.getData()

        # 设置表格的行数，和数据的数量相关
        self.tablewidget.setRowCount(len(data))

        # 设置表格的数据
        for index in range(len(data)):
            self.tablewidget.setItem(index, 0, QTableWidgetItem(str(data[index][0])))  # id
            self.tablewidget.setItem(index, 1, QTableWidgetItem(data[index][1]))
            self.tablewidget.setItem(index, 2, QTableWidgetItem(data[index][2]))
            self.tablewidget.setItem(index, 3, QTableWidgetItem(data[index][3]))
            self.tablewidget.setItem(index, 4, QTableWidgetItem(data[index][4]))
            self.tablewidget.setItem(index, 5, QTableWidgetItem(data[index][5]))
            self.tablewidget.setItem(index, 6, QTableWidgetItem(data[index][6]))
            self.tablewidget.setItem(index, 7, QTableWidgetItem(data[index][7]))
            self.tablewidget.setCellWidget(index, 8, self.buttonForRow())

    def flushNoCompleteTable(self):
        # 从数据表中获取数据
        data = Tools.getNoCompleteData()

        # 设置表格的行数，和数据的数量相关
        self.tablewidget2.setRowCount(len(data))

        # 设置表格的数据
        for index in range(len(data)):
            self.tablewidget2.setItem(index, 0, QTableWidgetItem(str(data[index][0])))  # id
            self.tablewidget2.setItem(index, 1, QTableWidgetItem(data[index][1]))
            self.tablewidget2.setItem(index, 2, QTableWidgetItem(data[index][2]))
            self.tablewidget2.setItem(index, 3, QTableWidgetItem(data[index][3]))
            self.tablewidget2.setItem(index, 4, QTableWidgetItem(data[index][4]))
            self.tablewidget2.setItem(index, 5, QTableWidgetItem(data[index][5]))
            self.tablewidget2.setItem(index, 6, QTableWidgetItem(data[index][6]))
            self.tablewidget2.setItem(index, 7, QTableWidgetItem(data[index][7]))
            self.tablewidget2.setCellWidget(index, 8, self.buttonForRow2())

    def buttonForRow(self):
        widget = QtWidgets.QWidget()
        # 修改
        self.updateBtn = QtWidgets.QPushButton('查看编辑')
        self.updateBtn.setStyleSheet("QPushButton{color:rgb(0,0,0)}"  # 按键前景色
                                     "QPushButton{background-color:rgb(30,144,255)}"  # 按键背景色
                                     "QPushButton:hover{color:white}"  # 光标移动到上面后的前景色
                                     "QPushButton{border-radius:6px}"  # 圆角半径
                                     "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
                                     )
        self.updateBtn.clicked.connect(self.editDef)

        # 删除
        self.deleteBtn = QtWidgets.QPushButton('删除')
        self.deleteBtn.setStyleSheet("QPushButton{color:rgb(0,0,0)}"  # 按键前景色
                                     "QPushButton{background-color:rgb(205,92,92)}"  # 按键背景色
                                     "QPushButton:hover{color:white}"  # 光标移动到上面后的前景色
                                     "QPushButton{border-radius:6px}"  # 圆角半径
                                     "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
                                     )
        # self.deleteBtn.clicked.connect(self.DeleteButton)
        self.deleteBtn.clicked.connect(self.delDef)
        hLayout = QtWidgets.QHBoxLayout()
        hLayout.addWidget(self.updateBtn)
        hLayout.addWidget(self.deleteBtn)
        hLayout.setContentsMargins(5, 2, 5, 2)
        widget.setLayout(hLayout)
        return widget
    def buttonForRow2(self):
        widget = QtWidgets.QWidget()
        # 修改
        self.updateBtn2 = QtWidgets.QPushButton('查看编辑')
        self.updateBtn2.setStyleSheet("QPushButton{color:rgb(0,0,0)}"  # 按键前景色
                                     "QPushButton{background-color:rgb(30,144,255)}"  # 按键背景色
                                     "QPushButton:hover{color:white}"  # 光标移动到上面后的前景色
                                     "QPushButton{border-radius:6px}"  # 圆角半径
                                     "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
                                     )
        self.updateBtn2.clicked.connect(self.editDef2)

        # 删除
        self.deleteBtn2 = QtWidgets.QPushButton('删除')
        self.deleteBtn2.setStyleSheet("QPushButton{color:rgb(0,0,0)}"  # 按键前景色
                                     "QPushButton{background-color:rgb(205,92,92)}"  # 按键背景色
                                     "QPushButton:hover{color:white}"  # 光标移动到上面后的前景色
                                     "QPushButton{border-radius:6px}"  # 圆角半径
                                     "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
                                     )
        # self.deleteBtn.clicked.connect(self.DeleteButton)
        self.deleteBtn2.clicked.connect(self.delDef)
        hLayout = QtWidgets.QHBoxLayout()
        hLayout.addWidget(self.updateBtn2)
        hLayout.addWidget(self.deleteBtn2)
        hLayout.setContentsMargins(5, 2, 5, 2)
        widget.setLayout(hLayout)
        return widget

    def addDef(self):

        # 新增的窗口,因为新增和修改共用一个对话框，所以需要在showDialog中参入参数表示这次点击的是新增按钮还是修改按钮
        self.showDialog(1)

    def showDialog(self, status,path='',name='',groupID='',parm='',segName='',comment=''):

        self.dialog = QDialog(self)
        self.dialog.resize(420, 283)
        self.dialog.setWindowIcon(QIcon('icon.png'))
        if status == 1:
            self.dialog.setWindowTitle('编辑')
        else:
            self.dialog.setWindowTitle('编辑')

        # 创建一个group盒子
        group = QGroupBox(self.dialog)

        # 标签和输入框,设置弹窗的样式的,
        lb1 = QLabel('图片ID:', group)
        # 设为只读
        self.ed1 = QLineEdit(group)
        self.ed1.setText(self.id)

        lb2 = QLabel('图片名称:', group)
        self.ed2 = QLineEdit(group)
        self.ed2.setText(name)

        lb3 = QLabel('所属组别:', group)
        self.ed3 = QLineEdit(group)
        self.ed3.setText(groupID)

        lb4 = QLabel('孔隙度值:', group)
        self.ed4 = QLineEdit(group)
        self.ed4.setText(parm)

        lb5 = QLabel('是否分割:', group)
        self.ed5 = QLineEdit(group)
        self.ed5.setText("是")

        # 创建确定和取消的按钮
        ok_button = QPushButton('确定', self.dialog)
        cancel_button = QPushButton('取消', self.dialog)

        # 创建一个垂直布局，将标签和按钮控件都添加到垂直布局里
        group_layout = QHBoxLayout()
        group_item1 = [lb1, self.ed1, lb2, self.ed2, lb3, self.ed3, lb4, self.ed4, lb5, self.ed5]
        for item in group_item1:
            group_layout.addWidget(item)

        layout1 = QHBoxLayout()
        layout1.addWidget(lb1)
        layout1.addWidget(self.ed1)

        layout2 = QHBoxLayout()
        layout2.addWidget(lb2)
        layout2.addWidget(self.ed2)

        layout3 = QHBoxLayout()
        layout3.addWidget(lb3)
        layout3.addWidget(self.ed3)

        layout4 = QHBoxLayout()
        layout4.addWidget(lb4)
        layout4.addWidget(self.ed4)

        layout5 = QHBoxLayout()
        layout5.addWidget(lb5)
        layout5.addWidget(self.ed5)
        # 将垂直布局添加到groupbox中
        # group.setLayout(group_layout)
        # group.setFixedSize(group.sizeHint())

        # 创建一个水平布局，并将两个按钮添加到布局中
        button_layout = QHBoxLayout()
        button_layout.addWidget(ok_button)
        button_layout.addWidget(cancel_button)

        # 创建一个最外层的dialog垂直布局，将盒子和按钮布局加到这个布局中
        dialog_layout = QVBoxLayout()
        dialog_layout.addLayout(layout1)
        dialog_layout.addLayout(layout2)
        dialog_layout.addLayout(layout3)
        dialog_layout.addLayout(layout4)
        dialog_layout.addLayout(layout5)
        dialog_layout.addLayout(button_layout)

        # 设置这个对话框的布局
        self.dialog.setLayout(dialog_layout)
        # self.dialog.setFixedSize(self.dialog.sizeHint())

        # 按传入的状态绑定确定按钮的功能
        if status == 1:
            ok_button.clicked.connect(self.addDialogAccept)
        else:
            ok_button.clicked.connect(self.editDialogAccept)

        # 默认选中ok按钮
        ok_button.setDefault(True)

        # 绑定取消按钮的功能
        cancel_button.clicked.connect(self.dialog.reject)

        self.dialog.exec_()
        return False

    # 新增对话框的ok按钮
    def addDialogAccept(self):

        # 如果每个输入项都不为空的表示输入正确
        if self.ed1.text() != '' and self.ed2.text() != '' and self.ed3.text() != '':
            # 关闭窗口
            self.dialog.close()
            # 在数据库中新增字段
            Tools.addData(self.ed1.text(), self.ed2.text(), self.ed3.text(), self.ed4.text(), self.ed5.text())
            # 刷新表格
            self.flushTable()
            # 提示新增成功
            self.showHint('新增成功')
        else:
            self.showHint('必填项不能为空')

        # 提示对话框

    def showHint(self, message):

        hint_msg = QMessageBox()
        hint_msg.setText(message)
        hint_msg.addButton(QMessageBox.Ok)
        hint_msg.setWindowTitle("提示")
        hint_msg.exec_()

    # 修改按钮的功能设置，和新增共用一个对话框，只是在点击ok按钮时有所不同

    def editDef(self):
        button = self.sender()
        if button:
            # 确定位置的时候这里是关键
            edit_row = self.tablewidget.indexAt(button.parent().pos()).row()
            # self.tableWidget.removeRow(row)
            # print("row"+str(row))

        # 选中某行
        selected_row = self.tablewidget.selectedItems()
        print("selected_row" + str(selected_row))

        # 如果当前选中的项数量为3时，表示只选取了一项
        # if edit_row:

        # 获取该行行号
        # edit_row = self.tablewidget.row(selected_row[0])

        # 记录当前选中项的id
        self.id = self.tablewidget.item(edit_row, 0).text()
        path = self.tablewidget.item(edit_row, 2).text()
        name = self.tablewidget.item(edit_row, 3).text()
        groupID = self.tablewidget.item(edit_row, 4).text()
        parm = self.tablewidget.item(edit_row, 5).text()
        segName=self.tablewidget.item(edit_row, 6).text()
        comment = self.tablewidget.item(edit_row, 7).text()

        # 将获取到的选中行的数据赋予给修改窗口的方法，同时返回新数据
        self.showDialog(2, path, name, groupID, parm, segName,comment)
        # else:
        #     # 如果没有选中改行时，点击编辑，弹出提示框
        #     self.showHint("请选中一行进行编辑")

    def editDef2(self):
        button = self.sender()
        if button:
            # 确定位置的时候这里是关键
            edit_row = self.tablewidget2.indexAt(button.parent().pos()).row()
            # self.tableWidget.removeRow(row)
            # print("row"+str(row))

        # 选中某行
        selected_row = self.tablewidget2.selectedItems()
        print("selected_row" + str(selected_row))

        # 如果当前选中的项数量为3时，表示只选取了一项
        # if edit_row:

        # 获取该行行号
        # edit_row = self.tablewidget.row(selected_row[0])

        # 记录当前选中项的id
        self.id = self.tablewidget2.item(edit_row, 0).text()
        path = self.tablewidget2.item(edit_row, 2).text()
        name = self.tablewidget2.item(edit_row, 3).text()
        groupID = self.tablewidget2.item(edit_row, 4).text()
        parm = self.tablewidget2.item(edit_row, 5).text()
        segName = self.tablewidget2.item(edit_row, 6).text()
        comment = self.tablewidget2.item(edit_row, 7).text()

        # 将获取到的选中行的数据赋予给修改窗口的方法，同时返回新数据
        self.showDialog(2, path, name, groupID, parm, segName, comment)
        # else:
        #     # 如果没有选中改行时，点击编辑，弹出提示框
        #     self.showHint("请选中一行进行编辑")
    def editDialogAccept(self):

        if self.ed1.text() != '' and self.ed2.text() != '' and self.ed3.text() != '':
            self.dialog.close()
            # 修改数据
            Tools.editData(self.id, self.ed1.text(), self.ed2.text(), self.ed3.text(), self.ed4.text(), self.ed5.text())
            self.flushTable()
            self.showHint('修改成功')
        else:
            self.showHint('必填项不能为空')

    def delDef(self):

        button = self.sender()
        if button:
            # 确定位置的时候这里是关键
            edit_row = self.tablewidget.indexAt(button.parent().pos()).row()
        # 选中某行
        # selected_row = self.tablewidget.selectedItems()
        # if len(selected_row) == 3:

        # del_row = self.tablewidget.row(selected_row[0])
        # del_row = self.tablewidget.row(selected_row[0])
        id = self.tablewidget.item(edit_row, 0).text()
        print(id)
        # 如果返回值为True，表示点击了确定删除
        if self.delDialog() == True:
            Tools.delData(id)
            self.flushTable()

        # else:
        #     # 如果没有选中改行时，点击编辑，弹出提示框
        #     self.showHint("请选中一行进行删除")

    # 布局和新增修改相差不大，不详细赘述
    def delDialog(self):
        delDialog = QDialog(self)
        delDialog.setWindowTitle(u'删除')
        group = QGroupBox('', delDialog)
        lb1 = QLabel(u'确定删除吗?删除后无法恢复')

        ok_button = QPushButton(u'确定', delDialog)
        cancel_button = QPushButton(u'取消', delDialog)

        ok_button.clicked.connect(delDialog.accept)
        ok_button.setDefault(True)
        cancel_button.clicked.connect(delDialog.reject)
        group_layout = QVBoxLayout()
        group_item = [lb1]
        for item in group_item:
            group_layout.addWidget(item)
        group.setLayout(group_layout)
        group.setFixedSize(group.sizeHint())

        button_layout = QHBoxLayout()
        button_layout.addWidget(ok_button)
        button_layout.addWidget(cancel_button)
        dialog_layout = QVBoxLayout()
        dialog_layout.addWidget(group)
        dialog_layout.addLayout(button_layout)
        delDialog.setLayout(dialog_layout)
        delDialog.setFixedSize(delDialog.sizeHint())

        # 当点击ok是，表示确定删除返回True
        if delDialog.exec_():
            return True
        # 否则返回False
        return False

