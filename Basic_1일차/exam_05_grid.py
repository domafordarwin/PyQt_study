import sys

from PyQt5.QtWidgets import (QWidget, QGridLayout,
                             QPushButton, QApplication)

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        grid = QGridLayout()
        self.setLayout(grid) # 레이아웃을 설정한다.

        names = ['Cls', 'Bck', '', 'Close',
                    '7', '8', '9', '/',
                    '4', '5', '6', '*',
                    '1', '2', '3', '-',
                    '0', '.', '=', '+']
        
        positions = [(i,j) for i in range(5) for j in range(4)] # 버튼의 위치를 설정한다.

        for position, name in zip(positions, names): # zip() 함수는 동일한 개수로 이루어진 자료형을 묶어주는 역할을 한다.
            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position) # 버튼을 레이아웃에 추가한다.

        self.setWindowTitle('Calculator')
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    