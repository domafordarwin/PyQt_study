import sys, pickle
from PyQt5.QtWidgets import (QApplication, QWidget, QTableWidget, QVBoxLayout,
                             QTableWidgetItem, QPushButton)

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.size = 4  # 행과 열의 크기를 정의합니다.
        self.initUI()

    def initUI(self):
        self.setWindowTitle('테이블 위젯에 대해 알아보기')
        self.setGeometry(300, 300, 640, 240)

        # 테이블 위젯 생성
        self.createTable()
        self.btn = QPushButton('저장')
        self.btn.clicked.connect(self.on_cl)  # self.on_cl로 연결합니다.

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
            with open('out_01.txt', 'rb') as fp:
                for r in range(self.size):
                    for c in range(self.size):
                        self.table.setItem(r, c, QTableWidgetItem(str(pickle.load(fp))))
        except Exception as e:
            print(f"Error: {e}")
            for r in range(self.size):
                for c in range(self.size):
                    self.table.setItem(r, c, QTableWidgetItem(''))

    def on_cl(self):  # MyApp 클래스의 메서드로 옮깁니다.
        try:
            with open('out_01.txt', 'wb') as fp:
                for r in range(self.size):
                    for c in range(self.size):
                        item = self.table.item(r, c)
                        text = item.text() if item else ""
                        pickle.dump(text, fp)
            print("Table data has been saved successfully!")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
