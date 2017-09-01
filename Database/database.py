from peewee import *


db = SqliteDatabase('database.db')

class Faces(Model):
    id = PrimaryKeyField()
    descriptor = TextField(unique=True)
    name = TextField(unique=True)

    class Meta:
        database = db

class Database:

    def __init__(self):
        db.connect()

    def create_db(self):
        db.create_table(Faces)

    def add(self, descriptor, name):
        Faces.create(descriptor = descriptor, name = name)

    def get_descr(self):
        people = []
        for face in Faces.select():
            people.append([face.descriptor, face.name])
        return people

    def __del__(self):
        db.close()