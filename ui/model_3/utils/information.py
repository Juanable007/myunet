from PyQt5.QtWidgets import QMessageBox


class Info:
    # 弹出部分
    def messageDialog(self, str1, str2):
        # 核心功能代码就两行，可以加到需要的地方
        msg_box = QMessageBox.about(self, "数据库录入", "保存成功")
        # 弹出部分

    def warningDialog( str):
        # 核心功能代码就两行，可以加到需要的地方
        msg_box = QMessageBox(QMessageBox.Warning, '警告', str)
        msg_box.exec_()