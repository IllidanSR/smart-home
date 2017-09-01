import numpy as np
import cv2
import FaceDetect


class FaceLearning:
    def __init__(self):
        self.fd = FaceDetect.FaceDetect()

    def learn(self):
        cap = cv2.VideoCapture(1)
        while (cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
                cv2.imshow("preview", frame)
                rval, frame = cap.read()
                if cv2.waitKey(20) == 27:  # exit on ESC
                    cv2.imwrite('cam.jpg', frame)
                    return self.fd.get_descriptor('cam.jpg', self.fd.TYPE_FILE)
            else:
                break
        cap.release()
