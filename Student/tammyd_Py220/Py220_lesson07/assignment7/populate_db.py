#populate_db.py

"""
Create, read, and delete data from the database, using the Donors class and Donations class

"""



import logging
from peewee import *
from mailroom_model import *
# can't figure out why Donors class is not being imported. I tried renaming the file, importing classes individually, and importing mailroom on it's own first (followed by "from mailroom_model import Donors").
# Only "from mailroom_model import *" does not give traceback.
# from mailroom_model import Donors, Donations
# Even though it is not importing, the try/except successfully handles the error

def populate_donors_db():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # tell peewee what database we'll use
    database = SqliteDatabase('mailroom.db')

    

    D_ID = 0      # donor_id 
    D_NAME = 1    # donor_name
    D_CITY = 2    # donor_city
    D_PHONE = 3   # donor_phone


    people = [
             ("D001", "Britney Spears", "Los Angeles", "222-222-2222"),
             ("D002", "Mandy Moore", "Portland", "333-333-3333"),
             ("D003", "Christina Aguilera", "Miami", "444-444-4444"),
             ("D004", "Queen Bey", "Houston", "555-555-5555")
             ]

    logger.info('Populating Donor Class')


    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        for person in people:
            with database.transaction():
                new_donor = Donors.create(
                    donor_id = person[D_ID],
                    donor_name = person[D_NAME],
                    donor_city = person[D_CITY],
                    donor_phone = person[D_PHONE]
                    )
                new_donor.save()
                logger.info('Database add successful')

        logger.info('Print the Person records we saved...')
        for saved_person in Donors:
            logger.info(f'{saved_person.donor_name} lives in {saved_person.donor_city}' +\
                f'and has the phone number {saved_person.donor_phone}')

    except Exception as e:
        logger.info(f'Error creating = {person[D_NAME]}')
        logger.info(e)
        logger.info('The database is protecting data')

    finally:
        logger.info('database closes')
        database.close()


def populate_donations_db():

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('mailroom.db')

    donations = [
        (653772.32, '2018-01-01', 'D001'),
        (877.33, '2018-02-02', 'D002'),
        (663.23, '2018-03-03','D003'),
        (1663.23, '2018-04-04', 'D004')
        ]

    logger.info('Donations add successful')

    DONATION_AMOUNT = 0
    DONATION_DATE = 1
    DONATION_DONOR_ID = 2


    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        for donation in donations:
            with database.transaction():
                new_donation = Donations.create(
                    donation_amount = donation[DONATION_AMOUNT],
                    donation_donor_name = donation[DONATION_DATE], 
                    donation_donor_id =[DONATION_DONOR_ID] 
                    )
                new_donation.save()
                logger.info('Database add successful')


    except Exception as e:
        logger.info(f'Error creating = {donation[DONATION_AMOUNT]} at donation date of {donation[DONATION_DATE]}.')
        logger.info(e)
        logger.info('The database is protecting data')

    finally:
        logger.info('database closes')
        database.close()


#if __name__ == "__main__":
#    populate_donors_db()