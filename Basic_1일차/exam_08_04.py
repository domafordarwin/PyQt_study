# image 보여주는 위젯 만들기

import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QMessageBox, QPushButton
from PyQt5.QtGui import QPixmap

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        file_path = 'image/bear.jpg'  # QPixmap 객체 생성

        hbox = QHBoxLayout() # 수평 박스 레이아웃 생성
        pixmap = QPixmap(file_path) # QPixmap 객체 생성

        lbl_img = QLabel(self) # QLabel 위젯 생성
        lbl_img.setPixmap(pixmap) # QLabel에 QPixmap 표시

        hbox.addWidget(lbl_img) # 수평 박스 레이아웃에 QLabel 추가
        self.setLayout(hbox) # 수평 박스 레이아웃을 창의 레이아웃으로 설정

        self.setWindowTitle('QPixmap')
        self.move(300, 300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
