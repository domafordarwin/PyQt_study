import sys
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QApplication)

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Event Handler')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def keyPressEvent(self,key_pressed):          # 키보드를 누를 때 발생하는 이벤트를 처리하기 위해 keyPressEvent() 메서드를 재구현한다.
        if key_pressed.key() == Qt.Key_Escape:    # Qt.Key_Escape는 ESC 키를 나타낸다.
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

