# 마우스 눌림 이벤트 처리

import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import (QMainWindow, QApplication)

class Communicate(QObject):
    closeApp = pyqtSignal() # pyqtSignal()을 이용하여 시그널을 하나 생성한다.

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.close) # Communicate 객체의 closeApp 시그널을 MyApp 클래스의 close() 슬롯에 연결한다.

        self.setWindowTitle('Emitting Signal')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def mousePressEvent(self, event):
        self.c.closeApp.emit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


