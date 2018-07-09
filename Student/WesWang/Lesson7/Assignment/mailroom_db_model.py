'''
Mailroom Database Model
Wesley Wang
'''

from peewee import *

database = SqliteDatabase('mailroom.db')
database.connect()
database.execute_sql('PRAGMA foreign_keys = ON;')

class BaseModel(Model):
    class Meta:
        database = database


''' Ideal model
class Donor(BaseModel):
    donor_id = PrimaryKeyField()
    first_name = CharField(max_length = 35)
    middle_name = CharField(max_length = 35, null = True)
    last_name = CharField(max_length = 35)
    nickname = CharField(max_length = 20, null = True)
'''


class Donor(BaseModel):
    donor_id = PrimaryKeyField()
    name = CharField(max_length = 70)
    nickname = CharField(max_length = 20, null = True)


class Address(BaseModel):
    address_id = PrimaryKeyField()
    donor = ForeignKeyField(Donor, related_name = 'donated by', null = False)
    address_line1 = CharField(max_length = 90)
    address_line2 = CharField(max_length = 90, null = True)
    city = CharField(max_length = 35)
    state = CharField(max_length = 35)
    zipcode = CharField(max_length = 10)


class Donation(BaseModel):
    donation_id = PrimaryKeyField()
    amount = DecimalField(max_digits = 7, decimal_places = 2)
    donor = ForeignKeyField(Donor, related_name = 'donated by', null = False)


database.create_tables([Donor, Address, Donation])
