# 이벤트 및 시그널 처리하기

import sys
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
                             QVBoxLayout, QApplication) 

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self) # QLCDNumber 위젯을 하나 만든다.
        sld = QSlider(Qt.Horizontal, self) # QSlider 위젯을 하나 만든다.

        vbox = QVBoxLayout() # QVBoxLayout 클래스를 이용하여 레이아웃을 생성한다.
        vbox.addWidget(lcd) # QLCDNumber 위젯을 레이아웃에 추가한다.
        vbox.addWidget(sld) # QSlider 위젯을 레이아웃에 추가한다.

        self.setLayout(vbox) # 레이아웃을 설정한다.
        sld.valueChanged.connect(lcd.display) # QSlider의 valueChanged() 시그널을 lcd.display() 슬롯에 연결한다.

        self.setWindowTitle('Signal and Slot')
        self.setGeometry(300, 300, 250, 150)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

