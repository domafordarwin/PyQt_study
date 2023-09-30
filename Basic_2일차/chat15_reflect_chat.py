import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.createReflectImage()

    def initUI(self):
        self.image = QImage('bear.jpg')
        if self.image.isNull():
            print('Image not found!')
            sys.exit(1)
        self.iw = self.image.width()
        self.ih = self.image.height()
        self.setWindowTitle('Image Reflect Image')
        self.setGeometry(400, 400, self.iw + 50, 2 * self.ih + 30)
        self.show()

    def createReflectImage(self):
        self.refImage = QImage(self.iw, self.ih, QImage.Format_ARGB32)
        painter = QPainter(self.refImage)
        painter.drawImage(0, 0, self.image)
        painter.setCompositionMode(QPainter.CompositionMode_DestinationIn)
        gradient = QLinearGradient(0, 0, 0, self.ih)
        gradient.setColorAt(1, QColor(0, 0, 0))
        gradient.setColorAt(0, Qt.transparent)
        painter.fillRect(0, 0, self.iw, self.ih, gradient)
        painter.end()

    def paintEvent(self, event):
        painter = QPainter(self)
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
