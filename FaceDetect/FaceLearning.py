import numpy as np
import cv2
import FaceDetect


class FaceLearning:
    def __init__(self):
        self.fd = FaceDetect.FaceDetect()

    def learn(self):
        cap = cv2.VideoCapture(0)
        while (cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
                cv2.imshow("preview", frame)
                rval, frame = cap.read()
                if cv2.waitKey(20) == 27:
                    return self.fd.get_descriptor(frame)
            else:
                break
        cap.release()
