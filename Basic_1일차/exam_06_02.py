import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QApplication, QGridLayout, QLabel)

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(10)

        x = 0
        y = 0

        self.text = "x: {0}, y: {1}".format(x, y) # x, y 좌표를 나타내는 문자열을 만든다.

        self.label = QLabel(self.text, self) # 라벨을 만들고 위젯에 추가한다.
        grid.addWidget(self.label, 0, 0, Qt.AlignTop) # 라벨을 (0, 0) 위치에 추가한다.

        self.setMouseTracking(True) # 마우스 추적 기능을 켠다.

        self.setLayout(grid)

        self.setWindowTitle('Reimplementing event handler')
        self.setGeometry(300, 300, 350, 200)
        self.show()

    def mouseMoveEvent(self, e): # 마우스를 움직일 때 발생하는 이벤트를 처리하기 위해 mouseMoveEvent() 메서드를 재구현한다.
        x = e.x()
        y = e.y()

        text = "x: {0}, y: {1}".format(x, y) # x, y 좌표를 나타내는 문자열을 만든다.
        self.label.setText(text) # 라벨의 텍스트를 설정한다.

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    

