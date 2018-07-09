#!/usr/bin/env python3

from peewee import *

database = SqliteDatabase('mailroom.db')
database.connect()
database.execute_sql('PRAGMA foreign_keys = ON;')


class BaseModel(Model):
    class Meta:
        database = database


class Donor(BaseModel):
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=30)
    phone = CharField(max_length=12)
    email = CharField(max_length=30)


class Donation(BaseModel):
    donor_id = ForeignKeyField(Donor, null=False)
    date = DateField(formats='YYYY-MM-DD')
    donation = DecimalField(max_digits=7, decimal_places=2)


database.create_tables([Donor,
                        Donation])
