from personjob_model import *

import logging

def populate_db():

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('mailroom.db')

    '''
    creating donor stuff
    '''

    logger.info('Creating donor records')

    DONOR_ID = 0
    DONOR_NAME = 1

    donors = [
        (1, 'Walter White'),
        (2, 'Jesse Pinkman'),
        (3, 'Gustavo Fring')
        ]

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        for donor in donors:
            with database.transaction():
                new_donor = Donor.create(
                    donor_id = donors[DONOR_ID],
                    donor_name = donors[DONOR_NAME])
                new_donor.save()

    except Exception as e:
        logger.info(f'Error creating = {donors[DONOR_NAME]}')
        logger.info(e)

    finally:
        logger.info('database closes')
        database.close()

    '''
    creating donation stuff
    '''

    logger.info('Creating donation records')

    DONATION_ID = 0
    DONATION_AMOUNT = 1
    DONOR_ID = 2

    donations = [
        (1, 5000.00, 1),
        (2, 6000.00, 1),
        (3, 4000.00, 2),
        (4, 4500.00, 3)
        ]

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        for donation in donations:
            with database.transaction():
                new_donation = Donation.create(
                    donation_id = donations[DONATION_ID],
                    donation_amount = donations[DONATION_AMOUNT],
                    donor_id = donations[DONOR_ID])
                new_donation.save()

    except Exception as e:
        logger.info(f'Error creating = {donations[DONATION_ID]}')
        logger.info(e)

    finally:
        logger.info('database closes')
        database.close()

if __name__ == '__main__':
    populate_db()
