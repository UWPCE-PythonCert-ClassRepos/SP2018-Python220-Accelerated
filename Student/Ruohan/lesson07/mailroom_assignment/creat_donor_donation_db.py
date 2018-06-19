
from peewee import *
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

database = SqliteDatabase('donordonation.db')
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
    donor = ForeignKeyField(Donor, related_name = 'donor_id')


database.create_tables([
        Donor,
        Donation
    ])

logger.info('Working with Donor class')
DONOR_ID = 0
DONOR_NAME = 1
CITY = 2
PHONE_NUMBER = 3

donors = [
    ('00001', 'William Gates III', 'Seattle', '1234567890'),
    ('00002', 'Cara Delevinge', 'San fransisco', '0983457621'),
    ('00003', 'Ellen Degenerous','LA', None),
    ('00004', 'Kate Upton', 'LA', '9876543201'),
    ('00005', 'Suki Waterhouse', 'London', '654823339'),
    ]

for donor in donors:
    try:
        with database.transaction():
            new_donor = Donor.creat(
                donor_id = donor[DONOR_ID],
                donor_name = donor[DONOR_NAME],
                city = donor[CITY],
                phone_number = donor[PHONE_NUMBER])
            new_donor.save()
    except Exception as e:
        logger.info(f'Error creating = {donor[DONOR_ID]} name is {donor[DONOR_NAME]} with error {e}')


logger.info('Working with Donation class')
DONOR_ID = 0
DONOR_NAME = 1
CITY = 2
PHONE_NUMBER = 3

donors = [
    ('00001', 'William Gates III', 'Seattle', '1234567890'),
    ('00002', 'Cara Delevinge', 'San fransisco', '0983457621'),
    ('00003', 'Ellen Degenerous','LA', None),
    ('00004', 'Kate Upton', 'LA', '9876543201'),
    ('00005', 'Suki Waterhouse', 'London', '654823339'),
    ]

for donor in donors:
    try:
        with database.transaction():
            new_donor = Donor.creat(
                donor_id = donor[DONOR_ID],
                donor_name = donor[DONOR_NAME],
                city = donor[CITY],
                phone_number = donor[PHONE_NUMBER])
            new_donor.save()
    except Exception as e:
        logger.info(f'Error creating = {donor[DONOR_ID]} name is {donor[DONOR_NAME]} with error {e}')



database.close()
