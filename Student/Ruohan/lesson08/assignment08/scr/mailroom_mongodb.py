#!/usr/bin/env python

"""
    mailroom script for mongodb
"""

import sys
import math
from textwrap import dedent
import pprint
import login_database
import utilities
from initial_data import get_donor_donation

log = utilities.configure_logger('default', '../logs/mongodb_script.log')

class Donor():

    def __init__(self, name, lst = []):
        self.name = name.capitalize()
        self.donation = lst
        def add_donations(self, amount):
            self.donation.append(amount)

    @property
    def total(self):
        return sum(self.donation)


    @property
    def times(self):
        return len(self.donation)

    @property
    def ave(self):
        return self.total/self.times

    @property
    def last(self):
        if len(self.donation) > 0:
            return self.donation[-1]
        else:
            return 0

    def __str__(self):
        return f'{self.name}:{self.donation}'

class DonorMongodb():

    def __init__(self, donor_donation=None):
        with login_database.login_mongodb_cloud() as client:
            log.info('Step 1: We are going to use a database called dev')
            self.db = client['dev']

            log.info('And in that database use a collection called donor')
            self.donor_data = self.db['donor']

            log.info('Step 2: Now we add data from arguments')
            self.donor_data.insert_many(donor_donation)

    @property
    def donors(self):
        return self.db.donor_data.find()

    def list_donors(self):
        """
            creates a list of the donors as a string, so they can be printed
        """
        listing = ["Donor list:"]
        for donor in self.donors:
            listing.append(donor.name)
        return "\n".join(listing)

    def find_donor(self, name):
        """
            find a donor in the donor db
        """
        name_query = {'name': name}
        return self.donor_data.find_one(name_query)

    def add_donor(self, name):
        """
            Add a new donor to the donor db
        """
        donor = Donor(name)
        with login_database.login_mongodb_cloud() as client:
            self.db = client['dev']
            self.donor_data = self.db['donor']
            self.donor_data.insert(donor)
        return donor

    def gen_letter(self, donor):
        """
        Generate a thank you letter for the donor
        """
        with login_database.login_mongodb_cloud() as client:
            self.db = client['dev']
            self.donor_data = self.db['donor']
            name_query = {'name': donor.name}
            donor = self.donor_data.find(name_query)
            return dedent('''Dear {0:s},
                  Thank you for your very kind donation of ${1:.2f}.
                  It will be put to very good use.
                                 Sincerely,
                                    -The Team
                  '''.format(donor['name'], donor['donation'][-1])
                          )

    @staticmethod
    def sort_key(item):
        return item[1]

    def generate_donor_report(self):
        """
        Generate the report of the donors and amounts donated.
        :returns: the donor report as a string.
        """
        report_rows = []
        with login_database.login_mongodb_cloud() as client:
            self.db = client['dev']
            self.donor_data = self.db['donor']
            for donor in self.donor_data.find():
                name = donor['name']
                gifts = donor['donation']
                total_gifts = sum(donor['donation'])
                num_gifts = len(gifts)
                avg_gift = total_gifts / num_gifts
            report_rows.append((name, total_gifts, num_gifts, avg_gift))

        # sort the report data
        report_rows.sort(key=self.sort_key)
        report = []
        report.append("{:25s} | {:11s} | {:9s} | {:12s}".format("Donor Name",
                                                                "Total Given",
                                                                "Num Gifts",
                                                                "Average Gift"))
        report.append("-" * 66)
        for row in report_rows:
            report.append("{:25s}   ${:10.2f}   {:9d}   ${:11.2f}".format(*row))
        return "\n".join(report)

    def save_letters_to_disk(self):
        """
        make a letter for each donor, and save it to disk.
        """
        with login_database.login_mongodb_cloud() as client:
            self.db = client['dev']
            self.donor_data = self.db['donor']
            for donor in self.donor_data.find():
                print("Writing a letter to:", donor['name'])
                letter = self.gen_letter(donor)
                filename = donor['name'].replace(" ", "_") + ".txt"
                open(filename, 'w').write(letter)


donor_donation = get_donor_donation()
db = DonorMongodb(donor_donation)


def main_menu_selection():
    """
    Print out the main application menu and then read the user input.
    """
    action = input(dedent('''
      Choose an action:
      1 - Send a Thank You
      2 - Create a Report
      3 - Send letters to everyone
      4 - Quit
      > '''))
    return action.strip()


def send_thank_you():
    """
    Record a donation and generate a thank you message.
    """
    # Read a valid donor to send a thank you from, handling special commands to
    # let the user navigate as defined.
    while True:
        name = input("Enter a donor's name"
                     "(or 'list' to see all donors or 'menu' to exit)> ").strip()
        if name == "list":
            print(db.list_donors())
        elif name == "menu":
            return
        else:
            break

    while True:
        amount_str = input("Enter a donation amount (or 'menu' to exit)> ").strip()
        if amount_str == "menu":
            return
        try:
            amount = float(amount_str)
            if math.isnan(amount) or math.isinf(amount) or round(amount, 2) == 0.00:
                raise ValueError
        except ValueError:
            print("error: donation amount is invalid\n")
        else:
            break

    donor = db.find_donor(name)
    if donor is None:
        donor = db.add_donor(name)

    donor.add_donation(amount)
    print(db.gen_letter(donor))


def print_donor_report():
    print(db.generate_donor_report())


def quit():
    sys.exit(0)


def main():
    selection_dict = {"1": send_thank_you,
                      "2": print_donor_report,
                      "3": db.save_letters_to_disk,
                      "4": quit}

    while True:
        selection = main_menu_selection()
        try:
            selection_dict[selection]()
        except KeyError:
            print("error: menu selection is invalid!")

if __name__ == "__main__":

    main()
