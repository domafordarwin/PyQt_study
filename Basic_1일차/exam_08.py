# 다양한 위젯다루기

import sys

from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        cb = QCheckBox('Show title', self) # QCheckBox 클래스의 인스턴스 생성
        cb.move(20, 20)
        cb.toggle()                                    # 체크박스를 선택한 상태로 만듦
        cb.stateChanged.connect(self.changeTitle)       # stateChanged 시그널을 changeTitle 메서드에 연결

        self.setWindowTitle('QCheckBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def changeTitle(self, state):                       # changeTitle 메서드 정의
        if state == Qt.Checked:                         # 체크박스의 상태가 변경될 때마다 상태값을 반환
            self.setWindowTitle('QCheckBox')            # 체크박스가 선택되면 창의 타이틀을 'QCheckBox'로 변경
        else:
            self.setWindowTitle(' ')                    # 체크박스가 선택되지 않으면 창의 타이틀을 공백으로 변경

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())