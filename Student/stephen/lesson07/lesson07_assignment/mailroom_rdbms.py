#!/usr/bin/env python

"""
Simple Mailroom Program for a nonprofit
Using RDBMS model to persist data
"""

# The script should prompt the user (you) to choose from a menu of 3 actions:
# “Send a Thank You”, “Create a Report” or “quit”)

import os, sys
import json
from donor_model import *
from donor_report import create_report

database = SqliteDatabase('donor_db.db')
database.connect()
database.execute_sql('PRAGMA foreign_keys = ON;')

class aDonor:
    """
    Handles the donor
    """
    def __init__(self, donor_id):
        self._donor_id = donor_id
        self._donor_info = Donor.get(Donor.id == self._donor_id)
        self._name = self._donor_info.first_name + ' ' + self._donor_info.last_name
        self._donation_info = (
            Donation.select(
                Donation.donor_id,
                fn.SUM(Donation.amount).alias('total_given'),
                fn.COUNT(Donation.id).alias('num_gifts'),
                fn.AVG(Donation.amount).alias('average_gift'),
                fn.MAX(Donation.donation_dt).alias('last_gift_dt')
            )
            .join(Donor, JOIN.INNER)
            .where(Donation.donor_id == self._donor_id)
            .group_by(Donation.donor_id)
            .order_by(fn.SUM(Donation.amount).desc())
            .limit(1)
            .get()
        )

    @property
    def name(self):
        return self._name

    @property
    def donations(self):
        query = (Donation.select(Donation.donation_dt, Donation.amount)
            .where(Donation.donor_id == self._donor_id)
            .order_by(Donation.donation_dt.desc()))
        donations_list = []
        for row in query:
            donations_list.append((row.donation_dt.strftime("%m-%d-%Y"), '${:,.2f}'.format(row.amount)))
        self._donations = donations_list
        return self._donations

    def add_donation(self, donation, dt=datetime.now()):
        self._donation = donation
        try:
            with database.transaction():
                new_donation = Donation.create(
                        donor_id = self._donor_id,
                        amount = self._donation,
                        donation_dt = dt
                )
                new_donation.save()
        except Exception as e:
            """
            If I had more time I would figure out how to make the
            program recover more gracefully from exceptions
            """
            raise(e)

    @property
    def total_donations(self):
        return self._donation_info.total_given
        # return reduce(lambda a, x: a+x, self._donations, 0)
        # s = 0
        # for d in donations:
        #     s += d
        # return s

    @property
    def count_donations(self):
        return self._donation_info.num_gifts

    @property
    def average_donation(self):
        return self._donation_info.average_gift

    @property
    def letter(self):
        """
        Takes the donor and returns a string that is a formatted thank you note
        with the donor's name and last donation amount.
        """
        last_donation = (Donation.select(Donation.amount)
            .where(Donation.donor_id == self._donor_id)
            .order_by(Donation.id.desc())
            .limit(1)
            .get()
        )
        return "Dear {:s},\n\nWe greatly appreciate your generous donation of ${:,.2f}.\n\nThank you,\nThe Team".format(self._name, last_donation.amount)

    @property
    def filename(self):
        'Return a txt file name based on the donor name and using underscores instead of spaces'
        return self._name.replace(' ', '_') + '.txt'

    # allow other items to call the class
    def __repr__(self):
        return "{}: {}".format(self._name, self._donations)  

class Menu:
    response = None

    def __init__(self, title, menu):
        self._title = title
        self._menu = menu
        error_msg = 'Not a valid response. Enter '
        for key in self._menu:
            error_msg += key + ', '
        self._error = error_msg[:-3] + 'or ' +  error_msg[-3] + '.\n'

    def menu(self):
        m = [str(k) + ') ' + str(v[0]) + '\n' for k, v in self._menu.items()]
        return ''.join(m)

    def get_response(self):
        print(self._title)
        print(self.menu())
        response = input('>> ')
        while response not in self._menu:
            print(self._error)
            response = input('>> ')
        self.response = response

    @property
    def switch(self):
        return {k:v[1] for k, v in self._menu.items()}
    
def print_report():
    print(create_report())

def return_to_main():
    return

def write_letters_to_disk():
    """
    Generate one letter for each donor and write to disk
    """
    query = (
        Donor.select(Donor.id)
        .join(Donation, JOIN.INNER)
        .group_by(Donor.id)
    )
    for row in query:
        donor = aDonor(row.id)
        print('Generating letter to {:s}'.format(donor.name))
        with open(donor.filename, 'w') as outfile:
            outfile.write(donor.letter)
    print()
    return

def enter_donor_info():
    print('\nEnter the first name of the donor')
    e_first_name = input('>> ')
    print('Optional: Enter the middle name of the donor')
    e_middle_name = input('>> ')
    print('Enter the last name of the donor')
    e_last_name = input('>> ')
    print('Optional: Enter the preferred name of the donor')
    e_preferred_name = input('>> ')
    print('Optional: Enter the street address of the donor')
    e_address = input('>> ')
    print('Optional: Enter the donor city')
    e_city = input('>> ')
    print('Optional: Enter the donor state')
    e_state = input('>> ')
    print('Optional: Enter the donor zip code')
    e_zip_code = input('>> ')
    print('Enter the donor email address')
    e_email = input('>> ')
    print('Enter the donor phone number')
    e_phone = input('>> ')
    print('Enter the donation amount')
    e_amount = input('>> ')
    print()
    try:
        with database.transaction():
            new_donor = Donor.create(
                first_name = e_first_name,
                middle_name = e_middle_name,
                last_name = e_last_name,
                preferred_name = e_preferred_name,
                address = e_address,
                city = e_city,
                state = e_state,
                zip_code = e_zip_code,
                email = e_email,
                phone = e_phone
            )
            new_donor.save()

            new_donation = Donation.create(
                donor_id = new_donor.id,
                amount = e_amount,
                donation_dt = datetime.now()
            )
            new_donation.save()

            print(aDonor(new_donor.id).letter)
            print()
 
    except Exception as e:
        """
        If I had more time I would figure out how to make the
        program recover more gracefully from exceptions
        """
        raise(e)

    return

def enter_donation():
    """
    If i had more time I would try to handle cases
    where two donors exist with the same first
    and last names
    """
    print('\nEnter the first name of the donor')
    e_first_name = input('>> ')
    print('Enter the last name of the donor')
    e_last_name = input('>> ')
    try:
        donor = Donor.get(Donor.first_name == e_first_name and Donor.last_name == e_last_name)
    except DoesNotExist:
        print('The donor could not be found')
        print()
        return
    print('Enter the donation amount')
    e_amount = input('>> ')
    print('Enter the date of the donation (using mm/dd/yyyy fromat, ex: 06/30/2018)')
    e_donation_date = input('>> ')
    current_donor = aDonor(donor.id)
    current_donor.add_donation(e_amount, dt=e_donation_date)
    print()
    print(current_donor.letter)
    print()
    return

def print_donor_list():
    print('\nDonors:')
    query = Donor.select(Donor.id)
    for row in query:
        donor = aDonor(row.id)
        print(donor.name)
    print()
    pass

def thank_you():
    ty = Menu('Thank You Menu:', thank_you_menu)
    ty.get_response()
    ty.switch.get(ty.response)()
    return

def quit_program():
    """
    Close database connection
    """
    database.close()
    sys.exit()

main_menu = {
    '1': ['Send a Thank You', thank_you]
    , '2': ['Create a Report', print_report]
    , '3': ['Send letters to everyone', write_letters_to_disk]
    , '4': ['Quit', quit_program]
    }

thank_you_menu = {
    '1': ['Add a new donor', enter_donor_info]
    , '2': ['Enter a donation for an existing donor', enter_donation]
    , '3': ['See a list of donor names', print_donor_list]
    , '4': ['Return to the Main Menu', return_to_main]
    }

def mainloop():
    print('Welcome to Mailroom\n')
    main = Menu('Main Menu:', main_menu)
    while True:
        main.get_response()
        main.switch.get(main.response)()

if __name__ == '__main__':
    mainloop()
