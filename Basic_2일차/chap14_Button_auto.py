# 파일제목: Button_auto.py
# 생성일자: 2021-01-24
# 최종수정일자: 2021-01-24
# 작성자: Doma Yoon
# 설명: Button_auto
# =============================================================================

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Button auto')
        self.setGeometry(1400, 250, 320,  200)


        # 버튼 리스트 생성
        self.btnList = []

        self.btnTop =100
        self.cnt = 0

        self.lbl = QLabel('생성할 버튼의 수를 입력하세요.', self)
        self.lbl.move(5, 5)

        self.txt = QLineEdit("", self)
        self.txt.move(10, self.lbl.height())

        self.btn = QPushButton('생성', self)
        self.btn.resize(QSize(80, 25))
        self.btn.move(10, self.lbl.height() + self.txt.height())

        self.btn.clicked.connect(self.createBtn)

        self.show()


    # 버튼을 생성하는 함수
    def createBtn(self):
        self.cnt = int(self.txt.text())
        for i in range(self.cnt):
            self.btnList.append(QPushButton(str(i + 1)+'n번째 버튼', self))
            self.btnList[i].resize(QSize(80, 25))
            self.btnList[i].move(10, self.btnTop+(i*25))
            self.btnList[i].show()
            



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())