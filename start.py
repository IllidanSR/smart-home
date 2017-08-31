import FaceDetect
import cv2
import sqlite3
import json

# capture = cv2.VideoCapture(0)
# ret, frame = capture.read()
# capture.release()

fd = FaceDetect.FaceDetect()
ref = fd.get_descriptor('reference.jpg')

print(json.dumps(ref))

test = fd.get_descriptor('test1.jpg')

a = fd.compare(ref, test)

if a > 0.3: print("Чужой")
else:       print("Свой")