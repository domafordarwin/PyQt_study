import sys
from PyQt5.QtWidgets import (QWidget, QLabel, 
                             QLineEdit, QTextEdit, QGridLayout, QApplication)


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit() # 한 줄의 텍스트를 입력할 수 있는 위젯이다.
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit() # 여러 줄의 텍스트를 입력할 수 있는 위젯이다.

        grid = QGridLayout() # QGridLayout 클래스를 이용하여 레이아웃을 생성한다.
        grid.setSpacing(10) # 위젯 사이의 간격을 10px로 설정한다.

        grid.addWidget(title, 1, 0) # (1, 0) 위치에 title 라벨을 추가한다.
        grid.addWidget(titleEdit, 1, 1) # (1, 1) 위치에 titleEdit 위젯을 추가한다.

        grid.addWidget(author, 2, 0) # (2, 0) 위치에 author 라벨을 추가한다.
        grid.addWidget(authorEdit, 2, 1) # (2, 1) 위치에 authorEdit 위젯을 추가한다.

        grid.addWidget(review, 3, 0) # (3, 0) 위치에 review 라벨을 추가한다.
        grid.addWidget(reviewEdit, 3, 1, 5, 1) # (3, 1) 위치에 reviewEdit 위젯을 추가한다. (5, 1) 크기의 공간을 차지한다.

        self.setLayout(grid) # 레이아웃을 설정한다.

        self.setWindowTitle('QGridLayout')
        self.setGeometry(300, 300, 350, 300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

    