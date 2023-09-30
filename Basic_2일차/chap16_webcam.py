# 패키지 불러오기
import sys, cv2, numpy as np, time

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

#Widget 상속
class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        #UI 초기화
        self.setWindowTitle('WebCam Viewer v0.1')
        self.setGeometry(100, 100, 640, 480)

        #UI 구성
        self.initUI()

    def initUI(self):
        self.cpt = cv2.VideoCapture(0)
        self.fps = 24
        self.sens = 300

        _, self.img_o = self.cpt.read()  # 원본 이미지, 이미지를 불러와서 저장하는 코드
        self.img_o = cv2.cvtColor(self.img_o, cv2.COLOR_BGR2RGB) # 이미지를 BGR에서 RGB로 변환하는 코드
        
        cv2.imwrite('img_o.jpg', self.img_o)                     # 이미지를 저장하는 코드

        self.cnt = 0  # 이미지 저장 카운트 변수

        self.frame = QLabel(self)
        self.frame.resize(640, 480)
        self.frame.setScaledContents(True)
        self.frame.move(5, 5)

        self.btn_on = QPushButton('켜기', self)
        self.btn_on.resize(100, 25)
        self.btn_on.move(5, 490)
        self.btn_on.clicked.connect(self.start)

        self.btn_off = QPushButton('끄기', self)
        self.btn_off.resize(100, 30)
        self.btn_off.move(110, 490)
        self.btn_off.clicked.connect(self.stop)

        self.prt = QLabel(self)
        self.prt.resize(200, 25)
        self.prt.move(215, 490)

        self.sldr = QSlider(Qt.Horizontal, self)
        self.sldr.resize(100, 25)
        self.sldr.move(415, 490)
        self.sldr.setMinimum(1)
        self.sldr.setMaximum(30)
        self.sldr.setValue(24)
        self.sldr.valueChanged.connect(self.setFPS)

        self.sldr1 = QSlider(Qt.Horizontal, self)
        self.sldr1.resize(100, 25)
        self.sldr1.move(520, 490)
        self.sldr1.setMinimum(50)
        self.sldr1.setMaximum(500)
        self.sldr1.setValue(300)
        self.sldr1.valueChanged.connect(self.setSens)

    def setFPS(self):
        self.fps = self.sldr.value()
        self.prt.setText('FPS: ' + str(self.fps)+'로 조정되었습니다.')
        self.timer.stop()
        self.timer.start(1000. / self.fps)

    def setSens(self):
        self.sens = self.sldr1.value()
        self.prt.setText('Sensitivity: ' + str(self.sens)+'로 조정되었습니다.')


    def start(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.nextFrameSlot)
        self.timer.start(1000. / self.fps)
    
    def nextFrameSlot(self):
        _, cam = self.cpt.read()
        cam_rgb = cv2.cvtColor(cam, cv2.COLOR_BGR2RGB)
        cam_rgb = cv2.flip(cam_rgb, 1)
        self.img_p = cv2.cvtColor(cam, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('img_p.jpg', self.img_p)

        self.compare(self.img_o, self.img_p)
        self.img_o = self.img_p.copy()
        img = QImage(cam, cam.shape[1], cam.shape[0], QImage.Format_RGB888) # 이미지를 QImage 객체로 변환하는 코드
        pix = QPixmap.fromImage(img)
        self.frame.setPixmap(pix)
        
    def stop(self):
        self.frame.setPixmap(QPixmap.fromImage(QImage()))
        self.timer.stop()


    def compare(self, img_o, img_p):
        err = np.sum((img_o.astype('float') - img_p.astype('float')) ** 2)
        err /= float(img_o.shape[0] * img_p.shape[1])
        if err < self.sens:
            self.cnt += 1
            self.prt.setText('동일한 이미지')
        else:
            t = time.localtime()
            self.prt.setText("{}-{}-{} {}:{}:{}".format(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec))
            self.cnt = 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
            