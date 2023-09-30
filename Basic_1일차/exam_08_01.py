# QInputDialog 위젯 다루기
# QInputDialog 클래스는 사용자에게 텍스트, 숫자, 항목 등을 입력받을 수 있는 대화상자를 제공
# QInputDialog 클래스의 주요 메서드
# getInt() : 정수값 입력
# getDouble() : 실수값 입력
# getItem() : 항목 선택
# getText() : 텍스트 입력
# QInputDialog 클래스의 주요 시그널
# textValueChanged : 텍스트가 변경될 때 발생
# intValueChanged : 정수값이 변경될 때 발생
# doubleValueChanged : 실수값이 변경될 때 발생
# itemSelectionChanged : 항목이 선택될 때 발생

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, 
                             QFrame, QApplication)
from PyQt5.QtGui import QColor

class Myapp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.col = QColor(0, 0, 0) # 색상 초기값을 검은색으로 설정

        redb = QPushButton('Red', self) # 버튼 3개 생성
        redb.setCheckable(True)         # 버튼을 체크 가능한 버튼으로 설정
        redb.move(10, 10)

        redb.clicked[bool].connect(self.setColor) # clicked 시그널을 setColor 메서드에 연결

        greenb = QPushButton('Green', self)
        greenb.setCheckable(True)
        greenb.move(10, 60)

        greenb.clicked[bool].connect(self.setColor)
        
        blueb = QPushButton('Blue', self)
        blueb.setCheckable(True)
        blueb.move(10, 110)

        blueb.clicked[bool].connect(self.setColor)

        self.square = QFrame(self) # QFrame 위젯 생성
        self.square.setGeometry(150, 20, 100, 100) # 위치와 크기 설정
        self.square.setStyleSheet("QWidget { background-color: %s }" %
            self.col.name())
        
        self.setWindowTitle('Toggle button')
        self.setGeometry(300, 300, 280, 170)
        self.show()

    def setColor(self, pressed): # setColor 메서드 정의
        source = self.sender() # sender() 메서드로 눌린 버튼의 객체 반환
        if pressed:
            val = 255
        else: val = 0

        if source.text() == "Red": # 눌린 버튼의 텍스트에 따라 색상 변경
            self.col.setRed(val)
        elif source.text() == "Green":
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)

        self.square.setStyleSheet("QFrame { background-color: %s }" %
            self.col.name())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Myapp()
    sys.exit(app.exec_())



