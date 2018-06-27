#!/usr/bin/env python

"""
    creat donor and donation dabatbas contains only two table: donor and donation
    (And some sample information has been input)
"""

from donor_donation_model import *
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

database.create_tables([
        Donor,
        Donation
    ])

logger.info('Working with Donor class')

def get_donor_sample_data():
    donors = [
        ('00001', 'William Gates III', 'Seattle', '1234567890'),
        ('00002', 'Cara Delevinge', 'San fransisco', '0983457621'),
        ('00003', 'Ellen Degenerous','LA', None),
        ('00004', 'Kate Upton', 'LA', '9876543201'),
        ('00005', 'Suki Waterhouse', 'London', '654823339'),
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
        (100000, '2018-03-01', '00001'),
        (30000, '2017-11-21', '00002'),
        (15000, '2017-04-27','00003'),
        (20000, '2018-01-01', '00004'),
        (200000, '2017-08-09', '00001')
        ]
    return donations

AMOUNT = 0
DONATION_TIME = 1
DONATION_DONORID = 2

donations = get_donation_sample_data()

for donation in donations:
    try:
        with database.transaction():
            new_donation = Donation.create(
                amount = donation[AMOUNT],
                donation_time = donation[DONATION_TIME],
                donation_donorid = donation[DONATION_DONORID])
            new_donation.save()
    except Exception as er:
        logger.info(f'Error creating = {donation[AMOUNT]} donation time is {donation[DONATION_TIME]} with error {er}')


database.close()
