# 이미지 반전시키기

# 패키지 불러오기
import sys

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# Mypp 어플리케이션 설정하기
class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.createReflectImage()

    def initUI(self):
        # 처리할 이미지 불러오기
        self.image = QImage('bear.jpg')

        # 이미지 불러오기 오류 처리 루틴 추가하기
        if self.image.isNull():
            print('found not Image')
            sys.exit(1)

        # 이미지의 크기 설정
        self.iw = self.image.width()
        self.ih = self.image.height()

        # 윈도우즈 설정하기
        self.setWindowTitle('Image Reflect Image')
        self.setGeometry(400, 400, self.iw + 50, 2 * self.ih + 30)
        self.show()


    def createReflectImage(self):
        # 이미지 처리 루틴
        self.refImage = QImage(self.iw, self.ih, QImage.Format_ARGB32)

        # 그림 그리기   
        painter = QPainter(self.refImage)   # 페인터 객체 생성하기
        #painter.begin(self.refImage)
        painter.drawImage(0, 0, self.image)

        painter.setCompositionMode(QPainter.CompositionMode_DestinationIn)
        graient = QLinearGradient(self.iw/2, 0, self.iw/2, self.ih)
        #graient = QLinearGradient(0, 0, 0, self.ih)
        graient.setColorAt(1, QColor(0, 0, 0))
        graient.setColorAt(0, Qt.transparent)

        painter.fillRect(0, 0, self.iw, self.ih, graient)

        painter.end()
        
    def paintEvent(self, event):
        painter=QPainter(self)
        #painter.begin(self)
        self.draw(painter)
        painter.end()

    def draw(self, painter):
        painter.drawImage(25, 15, self.image)
        painter.translate(0, 2 * self.ih + 15)
        painter.scale(1, -1)
        painter.drawImage(25, 0, self.refImage)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


