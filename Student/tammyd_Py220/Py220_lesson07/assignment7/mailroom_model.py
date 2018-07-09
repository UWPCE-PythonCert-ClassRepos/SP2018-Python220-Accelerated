"""

Simple database example with Peewee ORM, sqlite and Python
Here we define the schema
Use logging for messages so they can be turned off

"""


import logging
from peewee import *


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("One off program to build the classes from the model in the database")

logger.info("Here we define our data (the schema)")
logger.info("First name and connect to a database (sqlite here)")

logger.info("The next 3 lines of code are the only database specific code")

database = SqliteDatabase("mailroom.db")
database.connect()
database.execute_sql("PRAGMA foregn_keys = ON") # needed for sqlite only

logger.info("Connected to database")

class BaseModel(Model):
    class Meta:
        database = database

class Donors(BaseModel):
    """
    this class defines Donor, which maintains details of someone who has made a donation
    """
    logger.info("Donors class model created")
    donor_id = CharField(primary_key = True, max_length = 10)  #primary_key = True means every person has to have a unique name
    donor_name = CharField(max_length = 40)
    donor_city = CharField(max_length = 40, null = True)  #donor may have no city
    donor_phone = CharField(max_length= 13, null = True) #donor may not have/give contact info
    logger.info("Successfully logged Donors")

class Donations(BaseModel):
    """
    this class defines Donations, which maintains details of someone's donation
    """
    logger.info("Donations class model created")
    donation_amount = DecimalField(decimal_places = 2)
    donation_date = DateField(formats = "YYYY-MM-DD")
    donation__donor_id = ForeignKeyField(Donor)
    logger.info("Successfully logged Donations")

database.create_tables([
        Donors,
        Donations,
    ])

database.close()