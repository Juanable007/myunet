import sys
import requests
from PyQt5.QtWidgets import (QWidget,  QLabel,QVBoxLayout,QCheckBox,QGridLayout, QScrollArea,QApplication)
from PyQt5.QtGui import  QPixmap
from PyQt5.QtCore import Qt,QSize

class Picture(QWidget):
    def __init__(self, parent=None, url=None):
        super().__init__(parent)
        self.url = url
        self.ui()

    def ui(self):
        self.setFixedSize(850,600)
        layout = QGridLayout()
        total = len(self.url)
        self.setLayout(layout)
        self.sc = QScrollArea(self)
        self.qw = QWidget()
        # if total % 5 == 0:
        #     rows = int(total/5)
        # else:
        #     rows = int(total/5) + 1
        self.qw.setMinimumSize(850,96*total)
        for i in  range(total):
            pre_url = self.url[i].split("?")[0]
            sup = pre_url.split(".")[-1]
            req = requests.get(self.url[i])
            photo = QPixmap()
            photo.loadFromData(req.content)
            width = photo.width()
            height = photo.height()
            if width==0 or height==0:
                continue
            tmp_image = photo.toImage()
            size = QSize(width,height)
            photo.convertFromImage(tmp_image.scaled(size, Qt.IgnoreAspectRatio))
            tmp = QWidget(self.qw)
            vl = QVBoxLayout()
            label= QLabel()
            label.setFixedSize(128,96)
            label.setStyleSheet("border:1px solid gray")
            label.setPixmap(photo)
            label.setScaledContents(True)
            # 复选框
            ck = QCheckBox(str(i)+"."+sup+"("+str(width)+"x"+str(height)+")", self)
            vl.addWidget(label)
            vl.addWidget(ck)
            tmp.setLayout(vl)
            tmp.move(128 * (i % 1), 96 * int(i / 1))

        self.sc.setMinimumSize(850, 600)
        self.sc.setWidget(self.qw)
    def lale(self):
        print(11111)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    url=['https://pic2.zhimg.com/aadd7b895_xs.jpg?source=1940ef5c', 'https://pic2.zhimg.com/50/v2-60f7b5c071d378a34a3a6c489c3fdacc_hd.jpg?source=1940ef5c', 'https://pic2.zhimg.com/80/v2-60f7b5c071d378a34a3a6c489c3fdacc_720w.jpg?source=1940ef5c', 'https://pic1.zhimg.com/50/v2-aa7d74fe48183d16a571278a012ff759_hd.jpg?source=1940ef5c', 'https://pic4.zhimg.com/50/v2-011ac12cbfe61ebc411ba437fac88780_hd.jpg?source=1940ef5c', 'https://pic1.zhimg.com/50/v2-dea9876e70b0a0b08b635796eb2c86da_hd.jpg?source=1940ef5c', 'https://pic2.zhimg.com/50/v2-8574116f58ac5e560da7e3656f80dcdf_hd.jpg?source=1940ef5c', 'https://pic1.zhimg.com/80/v2-10e18ff65a640175ad058b4b5dfd2867_1440w.png', 'https://picb.zhimg.com/80/v2-a448b133c0201b59631ccfa93cb650f3_1440w.png', 'https://pic2.zhimg.com/v2-0cd41264be96353da10f5aca4088aa37_xs.jpg?source=1940ef5c', 'https://pic2.zhimg.com/50/v2-74c0b99f286ef52fefe4fd0cbe78c90b_hd.jpg?source=1940ef5c', 'https://pic1.zhimg.com/50/v2-27b377ed5db6b090a9834b00ffe54b8e_hd.jpg?source=1940ef5c', 'https://pic1.zhimg.com/50/v2-c7c874b8540a5dbdd93418429c39f188_hd.jpg?source=1940ef5c', 'https://pic4.zhimg.com/50/v2-fef58d7f36acb12ff4199fa507fc166e_hd.jpg?source=1940ef5c', 'https://pic1.zhimg.com/50/v2-fcd8d49f62634cb631ac08d5d1cc11ea_hd.jpg?source=1940ef5c', 'https://pic1.zhimg.com/50/v2-74fe1b6d5362b73fcfe5b887afcad6eb_hd.jpg?source=1940ef5c', 'https://pic2.zhimg.com/50/v2-6b6213d9a94f57722642b6bed847c6a2_hd.jpg?source=1940ef5c', 'https://pic1.zhimg.com/50/v2-bad7183c3135ea26d2e8e52653ee1f1c_hd.jpg?source=1940ef5c', 'https://pic2.zhimg.com/50/v2-476f50c384e1a4c90e994e6d63f63e8a_hd.jpg?source=1940ef5c', 'https://pic1.zhimg.com/50/v2-d720e9f8984d83da0a7344fa842cafa1_hd.jpg?source=1940ef5c', 'https://pic1.zhimg.com/50/v2-e82f6e26e7b49d7d7a5a0a337e2cd613_hd.jpg?source=1940ef5c', 'https://pic4.zhimg.com/50/v2-25496d917bf08c0ebc5106bb91f376a5_hd.jpg?source=1940ef5c', 'https://pic1.zhimg.com/50/v2-36e309f84b1395933488e6fa0f6bd341_hd.jpg?source=1940ef5c', 'https://pic1.zhimg.com/80/v2-10e18ff65a640175ad058b4b5dfd2867_1440w.png', 'https://picb.zhimg.com/80/v2-a448b133c0201b59631ccfa93cb650f3_1440w.png', 'https://pic3.zhimg.com/aadd7b895_xs.jpg?source=1940ef5c', 'https://pic1.zhimg.com/50/v2-c673663f10a662afc4a09dfe0d95c62c_hd.jpg?source=1940ef5c', 'https://pic4.zhimg.com/50/v2-891dd82d13e152e6204a827362adb0ef_hd.jpg?source=1940ef5c', 'https://pic3.zhimg.com/50/v2-dba8ca86ac6aa7c8517d22ee983c6e05_hd.jpg?source=1940ef5c', 'https://pic1.zhimg.com/50/v2-f16d5a24150db2816817fa698ac4ad82_hd.jpg?source=1940ef5c', 'https://pic1.zhimg.com/80/v2-10e18ff65a640175ad058b4b5dfd2867_1440w.png', 'https://picb.zhimg.com/80/v2-a448b133c0201b59631ccfa93cb650f3_1440w.png', 'https://static.zhihu.com/heifetz/assets/sidebar-download-qrcode.7caef4dd.png', 'https://pic1.zhimg.com/70/v2-8228fff23c22a72b57d1627b7213942c.jpg', 'https://pic2.zhimg.com/aadd7b895_im.jpg?source=1940ef5c', 'https://pic3.zhimg.com/90/v2-426097a9370aad0ab673d53cca060c93_250x0.jpg', 'https://pic2.zhimg.com/90/v2-18b57487b9aca2b8e12246f67be0d138_250x0.jpg', 'https://pic2.zhimg.com/90/v2-50f7c79c972342024947936b0420b8e4_250x0.jpg', 'https://pic4.zhimg.com/v2-1945b21d09872d21de3db9c9614918b3_540x450.jpeg', 'https://pic3.zhimg.com/80/v2-d0289dc0a46fc5b15b3363ffa78cf6c7.png']


    pic = Picture(url=url)
    pic.show()
    sys.exit(app.exec_())

