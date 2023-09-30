# 이벤트 처리 및 메시지 박스 처리하기

import sys
from PyQt5 import QtCore, QtGui

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtCore import QCoreApplication  # 이벤트 처리를 위해 필요하다.

class Myapp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # 윈도우 설정
        self.setWindowTitle('PyQt5 Exam')
        self.resize(400, 300)

        # 버튼 설정 
        btn = QPushButton('Click', self)
        btn.move(50, 50)

        btn.clicked.connect(QApplication.instance().quit)  # 버튼 이미지 처리   

        btn.resize(btn.sizeHint())
        btn.setToolTip('Click to quit')
    
        self.show()

    def closeEvent(self, QCloseEvent):
        ans = QMessageBox.question(self, "종료 확인", "종료하시겠습니까?", 
                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if ans == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Myapp()
    sys.exit(app.exec_())
# Compare this snippet from exam_01.py: