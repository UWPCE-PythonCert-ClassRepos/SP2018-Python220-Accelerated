"""
    This is a simple database model to house data
    for the Mailroom Application. The model
    just has two tables: Donor and Donation related
    by a donor_id field in Donation that references
    Donor
"""

from peewee import Model, CharField, DateTimeField, JOIN, fn, DoesNotExist
from peewee import DecimalField, ForeignKeyField, SqliteDatabase
from datetime import date, datetime, time
# need this library for hybrid properties
from playhouse.hybrid import hybrid_method, hybrid_property

database = SqliteDatabase('donor_db.db')
database.connect()

database.execute_sql('PRAGMA foreign_keys = ON;')

class BaseModel(Model):
    class Meta:
        database = database

class Donor(BaseModel):
    """
        This class defines the Donor, which maintains details of someone
        who has made a donation to the organization. We'll be using the auto
        generated primary keys since we may have people with the same name
        who donate
    """
    first_name = CharField(max_length=50)
    middle_name = CharField(max_length=50, null=True)
    last_name = CharField(max_length=50)
    preferred_name = CharField(max_length=100, null=True)
    address = CharField(max_length=100, null=True)
    city = CharField(max_length=50, null=True)
    state = CharField(max_length=50, null=True) # in case of out of country
    zip_code = CharField(max_length=20, null=True)
    email = CharField(max_length=100)
    phone = CharField(max_length=25)

class Donation(BaseModel):
    """
        This class defines Donations, which maintains details about how
        much donors contribute to the organization
    """
    donor_id = ForeignKeyField(Donor, null=False)
    amount = DecimalField(max_digits=11, decimal_places=2)
    donation_dt = DateTimeField()
    # Note to self: by default datetimefield formatted as YYYY-MM-DD HH:MM:SS

if __name__ == '__main__':
    # Drop tables to start with a clean slate
    database.execute_sql('DROP TABLE IF EXISTS Donation;')
    database.execute_sql('DROP TABLE IF EXISTS Donor;')

    # Create tables
    database.create_tables([
        Donor,
        Donation
    ])

    database.close()