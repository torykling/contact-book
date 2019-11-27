from peewee import *
from datetime import date

# create db object with configuration for database
db = PostgresqlDatabase('people', user='postgres',
                        password='', host='localhost', port='5432')

# connect to db
db.connect()

# a meta class is a class defined in a class that we use for configuration to the database
class BaseModel(Model):
    class Meta:
        database = db

# subclass of the base model to create a person model
class Person(BaseModel):
    name = CharField()
    birthday = DateField()

class Pet(BaseModel):
  name = CharField()
  animal_type = CharField()
# create tables in database for models
db.create_tables([Person, Pet])


tory = Person(name='Tory', birthday=date(1988, 8, 3))
tory.save()
greta = Pet(name='Greta', animal_type='dog')
greta.save()

# two ways to read -- .get() returns only the first record
Pet.get(Pet.name == 'Greta')
Pet.get(Pet.animal_type == 'dog')

# .select() - gets multiple records
# this gets them all
Person.select()
# this gets by condition
Person.select().where(Person.birthday < date(1990, 1, 1))

# update (if we didn't already have this variable defines)
tory = Person.get(Person.name == 'Tory')
tory.birthday = date(1988, 8, 4)
tory.save()

# delete
tory.delete_instance()
