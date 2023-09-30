# 메뉴바 만들기와 상태 표시줄 만들기

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu

class Myapp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # 윈도우 설정
        self.setWindowTitle('PyQt5 Exam')
        self.resize(400, 300)

        #메뉴바 설정
        # 메뉴바 생성 -> 메뉴 그룹 생성 -> 메뉴에 기능 추가 -> 메뉴바에 메뉴 추가

        menu = self.menuBar() # 메뉴바 생성

        menu_file = menu.addMenu('File') # File 그룹 메뉴 생성
        menu_edit = menu.addMenu('Edit') # Edit 그룹 메뉴 생성


        # file 그룹아래 새로운 하위 메뉴 생성
        file_new = QMenu('New', self) # New 메뉴 객체 생성

        # file_exit = QAction('Exit', self) # Exit 메뉴 객체 생성
        file_exit = QAction('Exit', self) # Exit 메뉴 객체 추가
        file_exit.triggered.connect(QApplication.instance().quit) # Exit 메뉴 객체에 이벤트 추가
        file_exit.setShortcut('Ctrl+Q') # 단축키 설정
        file_exit.setStatusTip('누르면 영원히 빠이빠이') # 상태 표시줄 설정


        #3단계 하위 메뉴 만들기
        new_txt = QAction('텍스트 파일', self) # 텍스트 파일 메뉴 객체 생성
        new_txt.setStatusTip('텍스트 파일을 생성합니다.') # 상태 표시줄 설정

        new_py = QAction('파이썬 파일', self) # 파이썬 파일 메뉴 객체 생성
        new_py.setStatusTip('파이썬 파일을 생성합니다.') # 상태 표시줄 설정


        # 메뉴 등록 관리
        menu_file.addMenu(file_new) # New 메뉴 객체를 생성한 후 이런 방식으로 추가할 수도 있다.
        menu_file.addAction(file_exit) # New 메뉴 객체를 생성한 후 이런 방식으로 추가할 수도 있다.

        # 하위 메뉴 등록 관리
        file_new.addAction(new_txt) # New 메뉴 객체에 텍스트 파일 메뉴 객체를 추가한다.
        file_new.addAction(new_py) # New 메뉴 객체에 파이썬 파일 메뉴 객체를 추가한다.

        # 상태 표시줄 설정
        self.statusBar().showMessage('Ready')

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Myapp()
    sys.exit(app.exec_())

    
