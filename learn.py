import FaceDetect.FaceLearning as fl
import Database
import json

db = Database.Database()
# db.create_db()
facelearn = fl.FaceLearning()

# facelearn.get_move()

name = input('Name ')
db.add(json.dumps(facelearn.learn()), name)
