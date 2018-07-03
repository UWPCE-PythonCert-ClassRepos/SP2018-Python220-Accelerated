"""
    Donor database
    Here we define the schema

"""

from peewee import *

database = SqliteDatabase('mailroom.db')
database.connect()
database.execute_sql('PRAGMA foreign_keys = ON;')



class BaseModel(Model):
    class Meta:
        database = database


class Donor(BaseModel):
    """
        This class defines Person, which maintains details of someone
        for whom we want to research career to date.
    """
    donor_id = IntegerField(primary_key = True)
    donor_name = CharField(max_length = 30)

class Donation(BaseModel):
    """
        This class defines Job, which maintains details of past Jobs
        held by a Person.
    """
    donation_id = IntegerField(primary_key = True)
    donation_amount = DecimalField(max_digits = 9, decimal_places = 2)
    donor_id = ForeignKeyField(Donor, related_name = 'donor_id', null = False)

database.create_tables([Donor, Donation], safe = True)
