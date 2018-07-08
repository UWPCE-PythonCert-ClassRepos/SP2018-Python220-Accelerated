"""
    Mailroom database with Peewee ORM, sqlite and Python
    Here we define the schema and create the database tables
"""

from peewee import *
# import logging
# import os

database = SqliteDatabase('mailroom_database.db')
database.connect()
database.execute_sql('PRAGMA foreign_keys = ON;')   


class BaseModel(Model):
    class Meta:
        database = database


class Donor(BaseModel):
    """
    Donor class for donor details 
    """
    donor_name = CharField(max_length=30, primary_key=True)
    donor_city = CharField(max_length=40, null=True)
    donor_state = CharField(max_length=40, null=True)
    # donor_company
    # donor_occupation
    # donor_age


class Donation(BaseModel):
    """
    This class contains the list of donations for each Donor
    """
    donation_amount = DecimalField(max_digits=10, decimal_places=2)
    donation_donor = ForeignKeyField(Donor)
    # donation_donor = ForeignKeyField(Donor, backref='donated_by')
    # donation_date = peewee.DateField(formats='MM-DD-YYYY')


database.create_tables([Donor, Donation])

database.close()



# if __name__ == "__main__":

    

#     database.connect()
#     database.execute_sql('PRAGMA foreign_keys = ON;')   

#     database.create_tables([Donor, Donation])

#     database.close()

