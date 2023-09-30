# 제12강 테이블 위젯(Table Widget) 1
#   테이블 위젯(Table Widget)은 행과 열로 구성된 2차원 표 모양의 위젯이다.

import sys, pickle
from PyQt5.QtWidgets import (QApplication, QWidget, QTableWidget, QVBoxLayout,
                             QTableWidgetItem, QBoxLayout, QPushButton)

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.size = 4
        self.initUI()

    def initUI(self):

        self.setWindowTitle('테이블 위젯에 대해 알아보기')
        self.setGeometry(300, 300, 640, 240)

        # 테이블 위젯 생성
        self.createTable()
        self.btn = QPushButton('저장')
        self.btn.clicked.connect(on_cl)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.table)
        self.layout.addWidget(self.btn)

        self.setLayout(self.layout)
        self.show()

    def createTable(self):
        self.table = QTableWidget()
        self.table.setRowCount(self.size)
        self.table.setColumnCount(self.size)
        self.table.setHorizontalHeaderLabels(('이름', '국어', '영어', '수학'))

        try:
            fp = open('out_001.txt', 'rb')
            for r in range(self.size):
                for c in range(self.size):
                   self.table.setItem(r, c,
                        QTableWidgetItem(str(pickle.load(fp))))
            fp.close()
        except:
            for r in range(self.size):
                for c in range(self.size):
                    self.table.setItem(r, c, QTableWidgetItem(''))

def on_cl():
    try:
        fp = open('out_001.txt', 'wb')
        for r in range(ex.size):
            for c in range(ex.size):
                pickle.dump(ex.table.item(r, c).text(), fp)
        fp.close()
    except:
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

