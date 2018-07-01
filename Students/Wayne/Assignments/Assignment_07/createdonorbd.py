from donordb_model import *
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

database.create_tables([
        Donor,
        Donation
    ])

logger.info('Building Donor Class DB')

def get_donor_sample_data():
    donors = [
        ('00001', 'Rivers Cuomo', 'Los Angeles', '14258675309'),
        ('00002', 'Dave Grohl', 'Springfield', '12068675309'),
        ('00003', 'Billy Joe Armstrong','Oakland', None),
        ('00004', 'Blake Schwarzenbach', 'Berkeley', '12538675309'),
        ('00005', 'Jenny Fromde Block', 'London', '13608675309'),
        ]
    return donors

DONOR_ID = 0
DONOR_NAME = 1
CITY = 2
PHONE_NUMBER = 3


donors = get_donor_sample_data()

for donor in donors:
    try:
        with database.transaction():
            new_donor = Donor.create(
                donor_id = donor[DONOR_ID],
                donor_name = donor[DONOR_NAME],
                city = donor[CITY],
                phone_number = donor[PHONE_NUMBER])
            new_donor.save()
    except Exception as e:
        logger.info(f'Error creating = {donor[DONOR_ID]} name is {donor[DONOR_NAME]} with error {e}')


logger.info('Working with Donation class')

def get_donation_sample_data():
    donations = [
        (150000, '2018-03-06', '00001'),
        (50000, '2017-02-28', '00002'),
        (125000, '2018-04-20','00003'),
        (210000, '2018-01-21', '00004'),
        (150000, '2018-01-11', '00001'),
        (9, '2018-01-15', '00005')
        ]
    return donations

AMOUNT = 0
DONATION_DATE = 1
DONOR_ID = 2

donations = get_donation_sample_data()

for donation in donations:
    try:
        with database.transaction():
            new_donation = Donation.create(
                amount = donation[AMOUNT],
                donation_date = donation[DONATION_DATE],
                donor_id = donation[DONOR_ID])
            new_donation.save()
    except Exception as er:
        logger.info(f'Error creating = {donation[AMOUNT]} donation time is {donation[DONATION_DATE]} with error {er}')


database.close()