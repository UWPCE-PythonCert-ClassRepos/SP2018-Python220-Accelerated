import logging
from peewee import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



database = SqliteDatabase('donor_donation.db')
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
    amount = DecimalField(decimal_places = 2)
    donation_time = DateField(formats = 'YYYY-MM-DD')
    donation_donorid = ForeignKeyField(Donor)
