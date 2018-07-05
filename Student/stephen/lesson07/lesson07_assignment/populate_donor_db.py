"""
    This module creates and does an initial population
    of the donor database.
"""

from donor_model import *

def populate_donor():
    """
    Add initial donors to the database
    """

    database = SqliteDatabase('donor_db.db')

    FIRST_NAME = 0
    MIDDLE_NAME = 1
    LAST_NAME = 2
    PREFERRED_NAME = 3
    ADDRESS = 4
    CITY = 5
    STATE = 6
    ZIP_CODE = 7
    EMAIL = 8
    PHONE = 9

    donors = [
        ('Jeff', None, 'Bezos', None, '345 15th Ave', 'Medina', 'WA', '98045', 'jeff@amazon.com', '206-555-9898'), #1
        ('Paul', 'C', 'Allen', None, '9753 Main St', 'Bellevue', 'WA', '98025', 'pallen@email.com', '425-989-5555'), #2
        ('Oprah', None, 'Winfrey', None, '178 Robin Lane', 'Orcas Island', 'WA', '98478', 'oprah@ownetwork.com', '800-678-3333'), #3
        ('Elon', None, 'Musk', None, '900 Rialto St', 'San Francisco', 'CA', '94129', 'elon@tesla.com', '615-309-5928'), #4
        ('Richard', 'Charles', 'Branson', 'Rich', '516 Abbey Rd', 'New York City', 'NY', '10007', 'richard@virgin.com', '888-907-1859'), #5
        ]

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        for donor in donors:
            with database.transaction():
                new_donor = Donor.create(
                        first_name = donor[FIRST_NAME],
                        middle_name = donor[MIDDLE_NAME],
                        last_name = donor[LAST_NAME],
                        preferred_name = donor[PREFERRED_NAME],
                        address = donor[ADDRESS],
                        city = donor[CITY],
                        state = donor[STATE],
                        zip_code = donor[ZIP_CODE],
                        email = donor[EMAIL],
                        phone = donor[PHONE]
                )
                new_donor.save()

        # print out donors that have been saved
        for saved_donor in Donor:
            print(f'{saved_donor.first_name} {saved_donor.last_name} lives in {saved_donor.city}, {saved_donor.state}')

    except Exception as e:
        print(f'Error creating = {donor[FIRST_NAME]} {donor[LAST_NAME]}')
        raise(e)

    finally:
        database.close()

def populate_donation():
    """
    Add initial donations to the database
    """

    database = SqliteDatabase('donor_db.db')

    DONOR_ID = 0
    AMOUNT = 1
    DONATION_DT = 2

    donations = [
        (1, 100.00, '2018-01-02'), #1
        (1, 75.00, '2018-02-20'), #2
        (2, 500.00, '2018-04-15'), #3
        (2, 75, '2018-05-01'), #4
        (3, 200, '2018-05-01'), #5
        (4, 150.00, '2018-05-02'), #6
        (5, 600.00, '2018-05-13'), #7
        (5, 90.00, '2018-06-01'), #8
        (1, 100.00, datetime.now()), #9
        ]

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        for donation in donations:
            with database.transaction():
                new_donation = Donation.create(
                        donor_id = donation[DONOR_ID],
                        amount = donation[AMOUNT],
                        donation_dt = donation[DONATION_DT]
                )
                new_donation.save()

        # print out donor donations
        donor_donations = (
            Donation.select(Donor.first_name, Donor.last_name, Donation.amount, Donation.donation_dt)
            .join(Donor, JOIN.INNER)
        )

        for donor_donation in donor_donations:
            donation_date = donor_donation.donation_dt.strftime("%B %d, %Y")
            print(f'{donor_donation.donor_id.first_name} {donor_donation.donor_id.last_name}',
                f'donated ${donor_donation.amount} on {donation_date}.')

    except Exception as e:
        print(f'Error creating = {donation[DONOR_ID]} {donation[AMOUNT]} {donation[DONATION_DT]}')
        raise(e)

    finally:
        database.close()

if __name__ == '__main__':
    populate_donor()
    populate_donation()