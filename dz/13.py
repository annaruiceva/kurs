import peewee
from peewee import *

db = MySQLDatabase(database="test", user="root", password="root", host="127.0.0.1", port=3306)


class BaseModel(Model):
    class Meta:
        database = db


class Class(BaseModel):
    id = PrimaryKeyField()
    name = CharField(max_length=50, default="Без названия")


class Student(BaseModel):
    id = PrimaryKeyField()
    first_name = CharField(max_length=15)
    last_name = CharField(max_length=15)
    age = IntegerField(constraints=[Check('age>0 and age < 120')])
    class_id = ForeignKeyField(Class, on_delete="set null", null=True)
    email = CharField(max_length=20, unique=True)
    phone = CharField(max_length=20, unique=True)


Class.create_table()
Student.create_table()

data_class = [
    {"name": "Математика"},
    {"name": "Русский"},
    {"name": "История"},
    {"name": "что-то новое"},

]

with db.manual_commit():
    db.begin()
    try:
        Class.insert_many(data_class, fields=[Class.name]).execute()
    except:
        db.rollback()
        print("откат записи аудиторий")
    else:
        try:
            db.commit()
        except:
            db.rollback()
            print("откат записи аудиторий")

data = [
    {"first_name": 'Кошкина', "last_name": 'Машка', "age": '17', "class_id": '1', "email": 'alo@kot.ru',
     "phone": '375889562325'},
    {"first_name": 'Коrа', "last_name": 'Ni', "age": '21',
     "class_id": '3', "email": 'alopoka@tut.ru', "phone": '322889562325'}
]

with db.manual_commit():
    db.begin()
    try:
        for u in data:
            Student.create(**u)
    except:
        db.rollback()
        print("откат записи студентов")
    else:
        try:
            db.commit()
        except:
            db.rollback()
            print("откат записи студентов")
