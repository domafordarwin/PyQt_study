import sys

from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication

                                    # QHBoxLayout, QVBoxLayout 클래스를 가져온다.
                                    # QHBoxLayout 클래스는 수평 박스 레이아웃을 만든다.
                                    # QVBoxLayout 클래스는 수직 박스 레이아웃을 만든다.

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 버튼 만들기
        okbutton = QPushButton('OK')
        cancelbutton = QPushButton('Cancel')
        
        # box layout 만들기
        hbox = QHBoxLayout()
        hbox.addStretch(1) # 늘어나는 공간을 만든다.
        hbox.addWidget(okbutton)
        hbox.addWidget(cancelbutton)

        vbox = QVBoxLayout()
        vbox.addStretch(1) # 늘어나는 공간을 만든다.
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setWindowTitle('Absolute Positioning')
        self.setGeometry(300, 300, 400, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    

    