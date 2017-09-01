import FaceDetect
import cv2
import json
import Database


db = Database.Database()
# db.create_db()
fd = FaceDetect.FaceDetect()

cap = cv2.VideoCapture(1)
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imwrite('cam.jpg', frame)
        test = fd.get_descriptor('cam.jpg', fd.TYPE_FILE)

        faces = db.get_descr()
        for face in faces:
            curr_face = json.loads(face[0])
            a = fd.compare(curr_face, test)
            if a < 0.5: print('Обнаружен', face[1])
    else:
        break
cap.release()
