"""
    Mailroom database with Peewee ORM, sqlite and Python
    Here we define the schema and create the database tables
"""

from peewee import *

database = SqliteDatabase('mailroom.db')
database.connect()
database.execute_sql('PRAGMA foreign_keys = ON;')

class BaseModel(Model):
    class Meta:
        database = database


class Donors(BaseModel):
    """
        This class defines Donor, which maintains details of someone
        for who has donated to the Avengers Fund A Kitten initiative
    """
    id = PrimaryKeyField()
    donor_name = CharField(max_length=30)
    donor_name_normalized = CharField(max_length=30)
    affiliation = CharField(max_length=30, null=True)
    location = CharField(max_length=40, null=True)


class Donations(BaseModel):
    """
        This class contains the list of donations for each Donor
    """
    id = PrimaryKeyField()
    donor = ForeignKeyField(Donors, backref='donations')
    donation = IntegerField()
    donation_date = DateField(formats='MM-DD-YYYY', null=True)

database.create_tables([
        Donors,
        Donations,
    ], safe=True)
