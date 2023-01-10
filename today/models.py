from peewee import *

database = PostgresqlDatabase()

class BaseModel(Model):
    class Meta:
        database = database

class ConfModel(BaseModel):
    id = AutoField()
    name = CharField(max_length=100)
    link = CharField(max_length=100)
    abbreviation = CharField(max_length=23)
    shortname = CharField(max_length=4)
    active = CharField(max_length=1)

    class Meta:
        table_name = "conferences"