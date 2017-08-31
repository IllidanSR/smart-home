import FaceDetect
import cv2

# capture = cv2.VideoCapture(0)
# ret, frame = capture.read()
# capture.release()

fd = FaceDetect.FaceDetect()
ref = fd.get_descriptor('reference.jpg')

test = fd.get_descriptor('test.jpg')

a = fd.compare(ref, test)

if a > 0.3: print("Чужой")
else:       print("Свой")