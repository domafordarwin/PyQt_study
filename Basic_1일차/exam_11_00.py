# 제11강 페인터와 페인트 이벤트 처리
import sys, random

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush, QFont
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.a = "지난하고 지루하지만 기본기를 \n 익히는 것은 매우 중요하다."

        self.setWindowTitle('Draw Points')
        self.setGeometry(300, 300, 300, 300)
        self.show()

    def paintEvent(self, e):                                    # paintEvent 메서드를 재구현하여 화면을 그리는 코드를 작성
        qp = QPainter()                                         # QPainter 클래스의 인스턴스 생성
        qp.begin(self)                                          # QPainter 클래스의 begin() 메서드를 호출하여 화면에 그리기 시작
        self.drawText(e, qp)                                    # draw_Text() 메서드를 호출하여 텍스트를 처리
        # self.drawPoints(qp)                                   # drawPoints() 메서드를 호출하여 점을 처리
        # self.drawRectangles(qp)                               # drawRectangles() 메서드를 호출하여 사각형을 처리
        # self.drawLines(qp)                                    # drawLines() 메서드를 호출하여 선을 처리
        # self.drawBrushes(qp)                                  # drawBrushes() 메서드를 호출하여 브러시를 처리
        # self.drawPolygon(qp)                                  # drawPolygon() 메서드를 호출하여 다각형을 처리
        # self.drawEllipse(qp)                                  # drawEllipse() 메서드를 호출하여 타원을 처리
        # self.drawPath(qp)                                     # drawPath() 메서드를 호출하여 경로를 처리
        # self.drawText(qp)                                     # drawText() 메서드를 호출하여 텍스트를 처리
        # self.drawImage(qp)                                    # drawImage() 메서드를 호출하여 이미지를 처리

        qp.end()                                                # QPainter 클래스의 end() 메서드를 호출하여 그리기를 끝냄

    def drawText(self, e, qp):
        qp.setPen(QColor(168, 34, 3))                           # 펜의 색상을 설정
        qp.setFont(QFont('Decorative', 10))                     # 폰트를 설정
        qp.drawText(e.rect(), Qt.AlignHCenter, self.a)           # 화면의 중앙에 텍스트를 그림

    def drawImage(self, qp):
        qp.drawImage(0, 0, self.image)                          # 이미지를 그림

    def drawPoints(self, qp):
        qp.setPen(Qt.red)                                       # 펜의 색상을 설정
        size = self.size()                                      # 현재 위젯의 크기를 구함
        for i in range(1000):                                   # 1000개의 점을 그림
            x = random.randint(1, size.width()-1)               # 점의 x 좌표를 랜덤하게 구함
            y = random.randint(1, size.height()-1)              # 점의 y 좌표를 랜덤하게 구함
            qp.drawPoint(x, y)                                  # 점을 그림

    def drawRectangles(self, qp):
        qp.setPen(Qt.red)                                       # 펜의 색상을 설정
        qp.setBrush(QColor(200, 0, 0))                          # 브러시의 색상을 설정
        qp.drawRect(10, 15, 90, 60)                             # 사각형을 그림
        qp.setBrush(QColor(255, 80, 0, 160))                    # 브러시의 색상을 설정
        qp.drawRect(130, 15, 90, 60)                            # 사각형을 그림

    def drawLines(self, qp):
        qp.setPen(Qt.blue)                                      # 펜의 색상을 설정
        qp.drawLine(20, 40, 250, 40)                            # 선을 그림
        qp.setPen(Qt.red)                                       # 펜의 색상을 설정
        qp.setBrush(Qt.yellow)                                  # 브러시의 색상을 설정
        qp.drawRect(20, 80, 50, 50)                             # 사각형을 그림
        qp.drawLine(20, 40, 20, 80)                             # 선을 그림
        qp.drawLine(70, 40, 70, 80)                             # 선을 그림
        qp.drawLine(20, 80, 70, 80)                             # 선을 그림


    def drawBrushes(self, qp):
        qp.setBrush(Qt.SolidPattern)                            # 브러시의 패턴을 설정
        qp.drawRect(10, 15, 90, 60)                             # 사각형을 그림
        qp.setBrush(Qt.Dense1Pattern)                           # 브러시의 패턴을 설정
        qp.drawRect(130, 15, 90, 60)                            # 사각형을 그림
        qp.setBrush(Qt.Dense2Pattern)                           # 브러시의 패턴을 설정
        qp.drawRect(250, 15, 90, 60)                            # 사각형을 그림
        qp.setBrush(Qt.Dense3Pattern)                           # 브러시의 패턴을 설정
        qp.drawRect(10, 105, 90, 60)                            # 사각형을 그림
        qp.setBrush(Qt.DiagCrossPattern)                        # 브러시의 패턴을 설정
        qp.drawRect(10, 105, 90, 60)                            # 사각형을 그림
        qp.setBrush(Qt.Dense5Pattern)                           # 브러시의 패턴을 설정
        qp.drawRect(130, 105, 90, 60)                           # 사각형을 그림

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())



