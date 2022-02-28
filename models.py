import os
import datetime 

from peewee import *

from playhouse.db_url import connect

DATABASE = SqliteDatabase('wordle.sqlite', pragmas={'foreign_keys': 1})

class User(Model):
	username = CharField(unique=True)
	level = CharField()

	class Meta:
		database = DATABASE

class Word(Model):
	word = CharField(unique=True)
	length = IntegerField()

	class Meta:
		database = DATABASE



class Times(Model):
	times = DateTimeField()
	owner = ForeignKeyField(User, backref='Times', on_delete = "CASCADE")

	class Meta:
		database = DATABASE


def initialize():
	DATABASE.connect()

	DATABASE.create_tables([User, Word, Times], safe = True)

	DATABASE.close()