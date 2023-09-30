# calendar 모듈을 사용하여 2023년 10월의 달력을 출력해보세요.
# Path: Study/exam_08_04.py

import sys

from PyQt5.QtWidgets import (QWidget, QCalendarWidget,
                             QLabel, QApplication, QVBoxLayout)

from PyQt5.QtCore import QDate

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout(self) # 수직 박스 레이아웃 생성

        cal = QCalendarWidget(self) # QCalendarWidget 위젯 생성
        cal.setGridVisible(True) # 그리드 표시 여부 설정
        cal.clicked[QDate].connect(self.showDate) # 날짜를 선택하면 showDate 메서드 호출

        vbox.addWidget(cal) # 수직 박스 레이아웃에 QCalendarWidget 추가

        self.lbl = QLabel(self) # QLabel 위젯 생성
        date = cal.selectedDate() # 선택된 날짜를 반환
        self.lbl.setText(date.toString()) # 날짜를 'yyyy년 MM월 dd일' 형식으로 표시

        vbox.addWidget(self.lbl) # 수직 박스 레이아웃에 QLabel 추가

        self.setLayout(vbox) # 수직 박스 레이아웃을 창의 레이아웃으로 설정

        self.setWindowTitle('QCalendarWidget')
        self.setGeometry(300, 300, 400, 300)
        self.show()

    def showDate(self, date): # showDate 메서드 정의
        self.lbl.setText(date.toString()) # 날짜를 'yyyy년 MM월 dd일' 형식으로 표시

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    