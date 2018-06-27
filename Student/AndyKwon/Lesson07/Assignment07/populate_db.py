# Populating database for mailroom

import peewee
import logging
from create_db import Donor, Donation

database = peewee.SqliteDatabase('mailroom_database.db')

def populate_donors():
    """
    populate database of donors and their donations
    """

    donors = [('Sir Isaac Newton', 'Woolsthorpe', 'England'), 
              ('Zach de la Rocha', 'Long Beach', 'California'),
              ('Space Ghost', 'Ghost Planet', 'Space')
             ]

    database.connect()
    database.execute_sql('PRAGMA foreign_keys = ON;')

    for donor in donors:
        with database.transaction():
            new_donor = Donor.create(donor_name=donor[0],
                                     donor_city=donor[1],
                                     donor_state=donor[2]
                                    )
            new_donor.save()
        
    for donor in Donor:
        print(donor)

    database.close()

def populate_donations():
    
    donations = [
                (100.38, 'Sir Isaac Newton'),
                (900000.00, 'Space Ghost'),
                (235.46, 'Zach de la Rocha'),
                (80.00, 'Space Ghost'),
                (44.33, 'Zach de la Rocha'),
                (122.22, 'Sir Isaac Newton'),
                (1.00, 'Space Ghost'),
                (1.23, 'Sir Isaac Newton'),
                (12.00, 'Space Ghost'),
                (3456.88, 'Zach de la Rocha')
                ]

    database.connect()
    database.execute_sql('PRAGMA foreign_keys = ON;')
    for donation in donations:
        with database.transaction():
            new_donation = Donation.create(donation_amount = donation[0],
                                           donation_donor = donation[1]
                                          )
            new_donation.save()

    # i = 0
    # for i in ranging(len(Donation)-1):
    #     print(Donation[i])

if __name__ == "__main__":
    populate_donors()
    populate_donations()

