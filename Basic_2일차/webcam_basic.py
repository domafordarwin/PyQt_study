import cv2
from PyQt5.QtCore import QTimer  # QTimer를 올바르게 임포트합니다.

class VideoCamera(object):
    def __init__(self):
        self.cpt = cv2.VideoCapture(0)
        self.fps = 24
        self.sens = 300
        self.timer = None
        self.img_o = None
        self.cnt = 0

    def __del__(self):
        self.cpt.release()

    def get_frame(self):
        _, img = self.cpt.read()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        if self.img_o is None:
            self.img_o = img
        diff = cv2.absdiff(self.img_o, img)
        _, diff = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
        cnt = cv2.countNonZero(diff)
        if cnt > self.sens:
            cv2.imwrite('img_'+str(self.cnt)+'.jpg', img)
            self.cnt += 1
        return diff  # 이미지 배열을 반환합니다.

    def start(self):
        self.timer = QTimer()  # QTimer 인스턴스를 생성합니다.
        self.timer.timeout.connect(self.nextFrameSlot)
        self.timer.start(int(1000. / self.fps))  # 인자를 정수로 변환합니다.

    def stop(self):
        self.timer.stop()

    def nextFrameSlot(self):
        _, img = self.cpt.read()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        if self.img_o is None:
            self.img_o = img
        diff = cv2.absdiff(self.img_o, img)
        _, diff = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
        cnt = cv2.countNonZero(diff)
        if cnt > self.sens:
            cv2.imwrite('img_'+str(self.cnt)+'.jpg', img)
            self.cnt += 1
        return diff  # 이미지 배열을 반환합니다.

if __name__ == '__main__':
    cam = VideoCamera()
    cam.start()
    while True:
        frame = cam.nextFrameSlot()
        cv2.imshow('frame', frame)  # 이미지 배열을 사용합니다.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cam.stop()
    cv2.destroyAllWindows()
