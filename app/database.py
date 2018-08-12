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

    id = AutoField()
    user = ForeignKeyField(User, backref='transactions')
    date_opened = DateTimeField(default=datetime.now)
    date_closed = DateTimeField(null=True)
    amount = DecimalField()
    diff = DecimalField()
    rate_opened = DecimalField()
    rate_closed = DecimalField(null=True)

    @property
    def profit(self):
        if not self.rate_closed:
            return 0
        coeff = self.amount / self.rate_opened
        return coeff*self.rate_closed - self.amount

