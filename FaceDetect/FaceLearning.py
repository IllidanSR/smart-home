import numpy as np
import cv2
import FaceDetect


class FaceLearning:
    def __init__(self):
        self.fd = FaceDetect.FaceDetect()

    def get_move(self):
        cap = cv2.VideoCapture(0)
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

        while (cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
                frame = cv2.flip(frame, 90)
                out.write(frame)
                cv2.imshow('frame', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break

        cap.release()
        out.release()
        cv2.destroyAllWindows()

    def learn(self, video):
        cap = cv2.VideoCapture(video)
        while (cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
                frame = cv2.flip(frame, 90)
                self.fd.get_descriptor(frame)
                descr = cv2.imshow('frame', frame)
                print(descr)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break
        cap.release()
        cv2.destroyAllWindows()