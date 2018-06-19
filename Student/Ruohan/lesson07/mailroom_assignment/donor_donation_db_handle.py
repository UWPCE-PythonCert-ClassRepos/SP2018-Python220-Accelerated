
from creat_donor_donation_db import *
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


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
    try 
