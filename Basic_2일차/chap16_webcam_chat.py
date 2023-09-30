import sys
import cv2
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QSlider, QVBoxLayout, QWidget

class VideoCamera(object):
    def __init__(self):
        self.cpt = cv2.VideoCapture(0)
        self.sens = 300
        self.img_o = None
        self.cnt = 0

    def get_frame(self):
        _, img = self.cpt.read()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        if self.img_o is None:
            self.img_o = img
        diff = cv2.absdiff(self.img_o, img)
        _, diff = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
        cnt = cv2.countNonZero(diff)
        if cnt > self.sens:
            cv2.imwrite('img_' + str(self.cnt) + '.jpg', img)
            self.cnt += 1
        return diff


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.cam = VideoCamera()
        self.timer = QTimer()
        self.timer.timeout.connect(self.nextFrameSlot)

        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        self.label = QLabel(self)
        layout.addWidget(self.label)

        self.fps_slider = QSlider(Qt.Horizontal, self)
        self.fps_slider.setMinimum(1)
        self.fps_slider.setMaximum(30)
        self.fps_slider.setValue(24)
        self.fps_slider.valueChanged.connect(self.adjustFPS)
        layout.addWidget(self.fps_slider)

        self.sens_slider = QSlider(Qt.Horizontal, self)
        self.sens_slider.setMinimum(0)
        self.sens_slider.setMaximum(1000)
        self.sens_slider.setValue(300)
        self.sens_slider.valueChanged.connect(self.adjustSensitivity)
        layout.addWidget(self.sens_slider)

        self.setCentralWidget(central_widget)

        self.adjustFPS()
        self.show()

    def adjustFPS(self):
        fps = self.fps_slider.value()
        self.timer.start(1000 // fps)

    def adjustSensitivity(self):
        self.cam.sens = self.sens_slider.value()

    def nextFrameSlot(self):
        frame = self.cam.get_frame()
        height, width = frame.shape
        bytes_per_line = width
        q_img = QImage(frame.data, width, height, bytes_per_line, QImage.Format_Grayscale8)
        pixmap = QPixmap.fromImage(q_img)
        self.label.setPixmap(pixmap)


def main():
    app = QApplication(sys.argv)
    main_win = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
