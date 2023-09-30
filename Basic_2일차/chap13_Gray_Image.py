# 파일제목: chap13_Gray_Image.py
# 생성일자: 2021-01-24
# 최종수정일자: 2021-01-24
# 작성자: Doma Yoon
# 설명: Gray Image
# =============================================================================

import sys, os
from PyQt5 import QtGui

from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton
from PyQt5.QtGui import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):

        # 버튼 생성
        btn = QPushButton('이미지 변경', self)
        btn.resize(btn.sizeHint())
        btn.move(20, 150)
        btn.clicked.connect(self.openFileNameDialog)

        # 이미지 불러오기
        # 현재 디렉토리 확인
        self.sid = QImage('./Study/Basic_2일차/bear.jpg').scaled(120, 120)
        if self.sid.isNull():
            print("Image not loaded!")  


        self.setWindowTitle('My First Application')
        self.setGeometry(1400, 250, 320,  200)

    
        self.show()


    def drawImage(self, painter):
        painter.drawImage(5, 15, self.sid)
        painter.drawImage(self.sid.width() + 10, 15, 
                          self.grayScale(self.sid.copy()))

    # 이미지를 그리는 함수
    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        self.drawImage(painter)
        painter.end()

    # 이미지를 불러오는 함수
    def openFileNameDialog(self):
        # 파일을 여는 다이얼로그
        fileName, _ = QFileDialog.getOpenFileName(self,"불러올 이미지를 선택하세요!", 
                                                  "","All Files (*);;Python Files (*.py)")
        if fileName:
            print(fileName)
            self.sid = QImage(fileName).scaled(120, 120)  # 이미지를 불러옴, sid는 이미지 객체

    # 그레이 이미지로 변환하는 함수
    def grayScale(self, image):
        # 이미지를 그레이 이미지로 변환
        for i in range(self.sid.width()):
            for j in range(self.sid.height()):
                color = image.pixel(i, j)
                gray = qGray(color)
                alpha = qAlpha(color)
                image.setPixel(i, j, qRgba(gray, gray, gray, alpha))
        return image


if __name__ == '__main__':
    app = QApplication([])
    ex = MyApp()
    sys.exit(app.exec_())
