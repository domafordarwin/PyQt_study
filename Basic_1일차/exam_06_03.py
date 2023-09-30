# 버튼 이벤트 처리하기

# 패키지 불러오기
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton

# 클래스 정의하기
class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton('Button1', self)
        btn1.move(30, 50)

        btn2 = QPushButton('Button2', self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.buttonClicked) # 버튼을 클릭하면 buttonClicked() 메서드가 호출된다.
        btn2.clicked.connect(self.buttonClicked) # 버튼을 클릭하면 buttonClicked() 메서드가 호출된다.

        self.statusBar()

        self.setWindowTitle('Event Sender')
        self.setGeometry(300, 300, 300, 200)
        self.show()

# 함수 정의하기
    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed') # statusBar() 메서드를 이용하여 상태바를 생성한다. 상태바에는 showMessage() 메서드를 이용하여 메시지를 표시한다.

# 메인 함수
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
