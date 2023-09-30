# 프로그래스 바 만들기

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar
from PyQt5.QtCore import QBasicTimer

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25) # 위치와 크기 설정

        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction) # 버튼을 클릭하면 doAction 메서드 호출

        self.timer = QBasicTimer() # 타이머 생성
        self.step = 0

        self.setWindowTitle('QProgressBar')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def timerEvent(self, e): # 타이머 이벤트가 발생할 때마다 호출되는 이벤트 핸들러
        if self.step >= 100: # 100이 되면 타이머를 중지하고 버튼의 텍스트를 'Finished'로 변경
            self.timer.stop()
            self.btn.setText('Finished')
            return
        
        self.step = self.step + 1 # 1씩 증가시키면서 프로그래스 바의 값을 변경
        self.pbar.setValue(self.step)

    def doAction(self): # 버튼을 클릭하면 호출되는 메서드
        if self.timer.isActive(): # 타이머가 이미 실행중이면 중지
            self.timer.stop()
            self.btn.setText('Start')
        else: # 타이머가 중지되어 있으면 시작
            self.timer.start(100, self) # 100ms 간격으로 타이머를 실행
            self.btn.setText('Stop')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    