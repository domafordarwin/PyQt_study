# 참고 자료 https://www.youtube.com/watch?v=OtqWefBqbxA&list=PL1eLKSeW1Baj72go6l3gg4C8TXRNUBdMo

import sys, os  # 시스템 정보를 얻기 위해 sys 모듈을, 환경 변수를 얻기 위해 os 모듈을 가져온다.


from PyQt5.QtWidgets import QApplication, QWidget # PyQt5.QtWidgets 모듈에서 QApplication, QWidget 클래스를 가져온다. 가장 기본적인 UI 클래스이다.

from PyQt5.QtWidgets import QPushButton # PyQt5.QtWidgets 모듈에서 QPushButton 클래스를 가져온다. 버튼을 만들기 위해 필요하다.

class MyApp(QWidget): # MyApp 클래스를 정의한다. QWidget 클래스를 상속받는다.
    def __init__(self): # MyApp 클래스의 생성자를 정의한다.
        super().__init__() # 부모 클래스의 생성자를 호출한다.
        self.initUI() # initUI() 메서드를 호출한다.

    # 2단계 : UI 구성하기
    def initUI(self): # initUI() 메서드를 정의한다.

        #윈도우 설정 옵션
        self.setWindowTitle('My First Application') # 윈도우 타이틀을 설정한다.
        self.move(200, 200) # 윈도우를 화면의 (200, 200) 위치로 이동시킨다.

        # 창크기 조절하기
        self.setGeometry(600, 300, 400, 600) # 윈도우의 위치와 크기를 설정한다. (x, y, width, height)
        #self.resize(400, 200) # 윈도우의 크기를 (400, 200)으로 설정한다.


        # 버튼 추가하기
        # 버튼을 만들고 버튼의 위치와 크기를 설정한다.
        btn = QPushButton('Quit', self) # 버튼의 텍스트를 'Quit'으로 설정하고, 부모 위젯을 self로 설정한다.
        btn.move(50, 50) # 버튼을 화면의 (50, 50) 위치로 이동시킨다.
        btn.resize(btn.sizeHint()) # 버튼의 크기를 적절히 조절한다.
        btn.clicked.connect(QApplication.instance().quit) # 버튼이 클릭되면 어플리케이션을 종료한다.
        btn.setToolTip('Click to quit') # 버튼에 마우스를 올리면 툴팁이 나타난다


        self.show() # 윈도우를 화면에 보여준다.

# 메인 코드 작성하기
if __name__ == '__main__': # 이 코드가 메인 코드일 때만 아래 코드를 실행한다.
    app = QApplication(sys.argv) # QApplication 객체를 생성한다.
    ex = MyApp() # MyApp 객체를 생성한다.
    sys.exit(app.exec_()) # app.exec_() 메서드를 호출하여 이벤트 루프를 실행한다.