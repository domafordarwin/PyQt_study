import sys, pickle
from PyQt5.QtWidgets import (QApplication, QWidget, QTableWidget, QVBoxLayout,
                             QTableWidgetItem, QPushButton)

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.size = 4
        self.initUI()

    def initUI(self):
        self.setWindowTitle('테이블 위젯에 대해 알아보기')
        self.setGeometry(300, 300, 640, 240)
        self.createTable()
        
        self.btn = QPushButton('저장')
        self.btn.clicked.connect(lambda: on_cl(self.size, self.table))  # lambda를 사용하여 필요한 인자를 함께 전달

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
            with open('out_001.txt', 'rb') as fp:
                for r in range(self.size):
                    for c in range(self.size):
                        self.table.setItem(r, c, QTableWidgetItem(str(pickle.load(fp))))
        except Exception as e:
            print(f"Error: {e}")
            for r in range(self.size):
                for c in range(self.size):
                    self.table.setItem(r, c, QTableWidgetItem(''))

def on_cl(size, table):  # size와 table을 인자로 받습니다.
    try:
        with open('out_001.txt', 'wb') as fp:
            for r in range(size):
                for c in range(size):
                    pickle.dump(table.item(r, c).text(), fp)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
