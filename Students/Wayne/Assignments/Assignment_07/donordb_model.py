"""
    Simple database example with Peewee ORM, sqlite and Python
    Here we define the schema
    Use logging for messages so they can be turned off

"""
import logging
from peewee import *


database = SqliteDatabase('donor.db')
database.connect()
database.execute_sql('PRAGMA foreign_keys = ON;')



class BaseModel(Model):
    class Meta:
        database = database


class Donor(BaseModel):
    donor_id = CharField(primary_key = True, max_length = 12)
    donor_name = CharField(max_length = 30)
    city = CharField(max_length = 30, null = True)
    phone_number = CharField(max_length = 30, null = True)


class Donation(BaseModel):
    amount = DecimalField(max_digits = 28, decimal_places = 2)
    donation_date = DateField(formats = 'YYYY-MM-DD')
    donor_id = ForeignKeyField(Donor)
