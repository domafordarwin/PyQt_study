# 드래그 앤 드롭 기능 구현하기

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import Qt, QMimeData                              # QMimeData: 드래그 앤 드롭을 위한 클래스
from PyQt5.QtGui import QDrag                                       # QDrag: 드래그 앤 드롭을 위한 클래스

class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)

    def mouseMoveEvent(self, e):
        if e.buttons() != Qt.RightButton:
            return

        mimeData = QMimeData()

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() - self.rect().topLeft())

        dropAction = drag.exec_(Qt.MoveAction)

    def mousePressEvent(self, e):
        super().mousePressEvent(e)

        if e.button() == Qt.LeftButton:
            print('press')

class Myapp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setAcceptDrops(True)               # 위젯이 다른 위젯으로부터 드롭을 받아들일 수 있도록 설정

        self.button = Button('Button', self)    # Button 클래스의 인스턴스 생성
        self.button.move(100, 65)

        self.setWindowTitle('Click or Move')
        self.setGeometry(300, 300, 280, 150)
        # self.show()                           # 이전까지는 이 단에서 show() 메서드를 호출했지만, 이번에는 호출하지 않음, 대신 Myapp 클래스의 인스턴스를 생성한 후 show() 메서드를 호출

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        position = e.pos()
        self.button.move(position)

        e.setDropAction(Qt.MoveAction)
        e.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Myapp()                                # Myapp 클래스의 인스턴스 생성
    ex.show()                                   # Myapp 클래스의 인스턴스를 생성한 후 show() 메서드를 호출
    app.exec_()                                 # 이전까지는 sys.exit(app.exec_())를 호출했지만, 이번에는 app.exec_()를 호출
                                                # 이유: app.exec_()는 이벤트 루프를 실행시켜주는 메서드이며, 이벤트 루프는 애플리케이션의 이벤트를 처리하고