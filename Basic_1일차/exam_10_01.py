import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit 

class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)

        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/plain'):    # 텍스트 형태의 MIME 데이터가 있는지 확인
            e.accept()  
        else:
            e.ignore()
            
    def dropEvent(self,e):                        # 드롭 이벤트가 발생하면, MIME 데이터를 텍스트로 변환한 후 버튼에 표시
        self.setText(e.mimeData().text())   

class Myapp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        edit = QLineEdit('', self)
        edit.setDragEnabled(True)
        edit.move(30, 65)

        button = Button('Button', self)
        button.move(190, 65)

        self.setWindowTitle('Simple Drag & Drop')
        self.setGeometry(300, 300, 300, 150)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Myapp()
    ex.show()
    app.exec_()


