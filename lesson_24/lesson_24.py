from pony.orm import *
from pony.orm.core import sql_logger

db = Database()

sqlite = dict(
            provider='sqlite',
            filename='person.db',
            create_db=True
            )

mysql = dict(
            provider='mysql',
            host="127.0.0.1",
            user="student",
            passwd="welcome2qauto",
            db="person"
            )


class Person(db.Entity):
    name = Required(str)
    age = Optional(int)
    cars = Set('Car')


class Car(db.Entity):
    maker = Required(str)
    model = Optional(str)
    owner = Required(Person)

db.bind(sqlite)
# db.bind(mysql)
db.generate_mapping(create_tables=True)
set_sql_debug(True)

@db_session
def add_person(name: str = "Isaak"):
    p1 = Person(name=name, age=21)
    c1 = Car(maker="Audi", model="AAs", owner=p1)
    db.commit()

#add_person("Matfheere")

@db_session
def output():
    print(Car.select().show())
    print(Person.select().show())
    result = select(p for p in Person if p.age > 20)
    print(result.show())
output()

@db_session
def change_name():
    pass

@db_session
def show():
    Person.select(lambda e: e.age >= 20).show()

show()