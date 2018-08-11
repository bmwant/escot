from datetime import datetime

from peewee import SqliteDatabase
from peewee import (
    Model,
    CharField,
    DateTimeField,
    DateField,
    AutoField,
    ForeignKeyField,
    DecimalField,
    BooleanField,
)

import config


db = SqliteDatabase(config.DB_PATH, pragmas={'foreign_keys': 1})


class User(Model):
    class Meta:
        database = db

    id = AutoField()
    name = CharField()
    email = CharField()
    telegram_handle = CharField()
    wallet = CharField()


class Transaction(Model):
    class Meta:
        database = db

    date = DateTimeField(default=datetime.now)
    user = ForeignKeyField(User, backref='transactions')
    amount = DecimalField()
    rate = DecimalField()
    closed = BooleanField(default=False)
