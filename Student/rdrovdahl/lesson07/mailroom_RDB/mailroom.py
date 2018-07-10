#! /usr/local/bin/python3
"""
This is an object oriented version of the mailroom program which uses peewee
as an ORM with a sqlite database
"""

import os
import sys
import math
# handy utility to make pretty printing easier
from textwrap import dedent
import datetime
import pathlib
# database schema
from mailroom_db_model import *


def populate_sql_db():
    """
    seed the sqlite database
    """
    response = input('Would you like to perform the initial population of the sqlite database? y/n >')
    if response.lower() == 'n':
        return
    donor_list = [('Iron Man', [100000, 50000, 1000], 'Hero', 'USA'),
                  ('Thor', [50, 25, 100], 'Hero', 'Earth'),
                  ('Winter Soldier', [360, 480], 'Villian', 'USSR'),
                  ('Captain America', [30, 40], 'Hero', 'USA'),
                  ('Nick Fury', [100000, 545, 1000], 'Retired', 'Unknown'),
                  ('Hawkeye', [75, 50, 20], 'Hero', 'USA'),
                  ('Ultron', [50000, 40000, 50000], 'Villian', 'DarkWeb'),
                  ('Black Panther', [100, 900, 50], 'Unaffiliated', 'Africa'),
                  ('War Machine', [10, 10], 'Unaffiliated', 'USA'),
                  ('Red Skull', [1000, 2000, 3000], 'Villian', 'Europe'),
                  ]
    database = SqliteDatabase('mailroom.db')
    # populate Donor table
    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        for donor in donor_list:
            with database.transaction():
                new_donor = Donors.create(
                    donor_name=donor[0],
                    donor_name_normalized=donor[0].lower(),
                    affiliation=donor[2],
                    location=donor[3])
                new_donor.save()
    except Exception as e:
        print(e)
    # populate Donations table
    try:
        for donor in donor_list:
            id = Donors.select().where(Donors.donor_name == donor[0]).get()
            for i in range(len(donor[1])):
                with database.transaction():
                    new_donation = Donations.create(
                        donor=id,
                        donation=donor[1][i])
                    new_donation.save()
    except Exception as e:
        print(e)
    finally:
        database.close()



# Utility so we have data to test with, etc.
# def get_sample_data():
#     """
#     returns a list of donor objects to use as sample data
#     """
#     return [Donor('Iron Man', [100000, 50000, 1000], 'Hero', 'USA'),
#             Donor('Thor', [50, 25, 100], 'Hero', 'Earth'),
#             Donor('Winter Soldier', [360, 480], 'Villian', 'USSR'),
#             Donor('Captain America', [30, 40], 'Hero', 'USA'),
#             Donor('Nick Fury', [100000, 545, 1000], 'Retired', 'Unknown'),
#             Donor('Hawkeye', [75, 50, 20], 'Hero', 'USA'),
#             Donor('Ultron', [50000, 40000, 50000], 'Villian', 'DarkWeb'),
#             Donor('Black Panther', [100, 900, 50], 'Unaffiliated', 'Africa'),
#             Donor('War Machine', [10, 10], 'Unaffiliated', 'USA'),
#             Donor('Red Skull', [1000, 2000, 3000], 'Villian', 'Europe'),
#             ]


class Donor():
    """
    class to hold the information about a single donor
    """

    def __init__(self, name, donations=None, affiliation='unknown', location='unknown'):
        """
        create a new Donor object
        :param name: the full name of the donor
        :param donations=None: iterable of past donations
        """

        self.norm_name = self.normalize_name(name)
        self.name = name.strip()
        if donations is None:
            self.donations = []
        else:
            self.donations = list(donations)
        self.affiliation = affiliation
        self.location = location

    @staticmethod
    def donations_rdb(name):
        query = (Donors.select(Donors, Donations).join(Donations)
                 .where(Donors.donor_name_normalized == name.lower()))
        donations = list(d.donations.donation for d in query)
        return donations


    @staticmethod
    def normalize_name(name):
        """
        return a normalized version of a name to use as a comparison key
        simple enough to not be in a method now, but maybe you'd want to make it fancier later.
        """
        return name.lower().strip().replace(" ", "")

    # @property
    # def last_donation(self):
    #     """
    #     The most recent donation made
    #     """
    #     try:
    #         return self.donations[-1]
    #     except IndexError:
    #         return None

    @staticmethod
    def last_donation_rdb(name):
        """
        The most recent donation made
        """
        query = (Donors.select(Donors, Donations).join(Donations)
                 .where(Donors.donor_name_normalized == name.lower()))
        donations = list(d.donations.donation for d in query)
        try:
            return donations[-1]
        except IndexError:
            return 0

    # @property
    # def total_donations(self):
    #     return sum(self.donations)

    @staticmethod
    def total_donations_rdb(name):
        query = (Donors.select(Donors, Donations).join(Donations)
                 .where(Donors.donor_name_normalized == name.lower()))
        donations = list(d.donations.donation for d in query)
        return sum(donations)

    # @property
    # def average_donation(self):
    #     try:
    #         return self.total_donations / len(self.donations)
    #     except ZeroDivisionError:
    #         return 0

    @staticmethod
    def average_donation_rdb(name):
        query = (Donors.select(Donors, Donations).join(Donations)
                 .where(Donors.donor_name_normalized == name.lower()))
        donations = list(d.donations.donation for d in query)
        try:
            return sum(donations) / len(query)
        except ZeroDivisionError:
            return 0

    # def add_donation(self, amount):
    #     """
    #     add a new donation
    #     """
    #     amount = float(amount)
    #     if amount <= 0.0:
    #         raise ValueError("Donation must be greater than zero")
    #     self.donations.append(amount)

    @staticmethod
    def add_donation_rdb(name, amount):
        """
        add a new donation
        """
        amount = float(amount)
        if amount <= 0.0:
            raise ValueError("Donation must be greater than zero")
        id = Donors.select().where(Donors.donor_name_normalized == name.lower()).get()
        new_donation = Donations.create(
            donor=id,
            donation=amount)
        new_donation.save()


class DonorDB():
    """
    encapsulation of the entire database of donors and associated data
    """

    def __init__(self, donors=None):
        """
        Initialize a new donor database
        :param donors=None: iterable of Donor objects
        """
        if donors is None:
            self.donor_data = {}
        else:
            self.donor_data = {d.norm_name: d for d in donors}

    # def save_to_file(self, filename):
    #     with open(filename, 'w') as outfile:
    #         self.to_json(outfile)

    # @classmethod
    # def load_from_file(cls, filename):
    #     with open(filename, 'r') as infile:
    #         obj = js.from_json(infile)
    #     return obj

    # @property
    # def donors(self):
    #     """
    #     an iterable of all the donors
    #     """
    #     return self.donor_data.values()

    # def list_donors(self):
    #     """
    #     creates a list of the donors as a string, so they can be printed
    #     Not calling print from here makes it more flexible and easier to
    #     test
    #     """
    #     listing = ["Donor list:"]
    #     for donor in self.donors:
    #         listing.append(donor.name)
    #     return "\n".join(listing)

    @staticmethod
    def list_donors_rdb():
        """
        creates a list of the donors as a string, so they can be printed
        Not calling print from here makes it more flexible and easier to
        test
        """
        listing = ["Donor list:"]
        for donor in Donors:
            listing.append(donor.donor_name)
        return "\n".join(listing)

    # def find_donor(self, name):
    #     """
    #     find a donor in the donor db
    #     :param: the name of the donor
    #     :returns: The donor data structure -- None if not in the self.donor_data
    #     """
    #     return self.donor_data.get(Donor.normalize_name(name))

    # def add_donor(self, name):
    #     """
    #     Add a new donor to the donor db
    #     :param: the name of the donor
    #     :returns: the new Donor data structure
    #     """
    #     donor = Donor(name)
    #     self.donor_data[donor.norm_name] = donor
    #     return donor

    @staticmethod
    def add_donor_rdb(name, affiliation=None, location=None):
        """
        Add a new donor to the donor db
        :param: the name of the donor
        :returns: the new donor id
        """
        # check to see if donor already exists
        query = Donors.select().where(Donors.donor_name_normalized==name.lower())
        if query.exists():
            return None
        # add new donor if doesn't already exist
        else:
            try:
                new_donor = Donors.create(
                    donor_name=name,
                    donor_name_normalized=name.lower(),
                    affiliation=affiliation,
                    location=location)
                new_donor.save()
            except Exception as e:
                print(e)
        id = Donors.select().where(Donors.donor_name_normalized == name.lower()).get()
        return id


    # def gen_letter(self, donor):
    #     """
    #     Generate a thank you letter for the donor
    #     :param: donor tuple
    #     :returns: string with letter
    #     note: This doesn't actually write to a file -- that's a separate
    #           function. This makes it more flexible and easier to test.
    #     """
    #     k = (donor.last_donation/5 * 2)
    #     letter = (f'''Dear {donor.name},
    #         We at the Avengers Fund-a-Kitten Initiative would like to thank you for
    #     your generous donation of ${donor.last_donation:,.2f}.\n
    #     Taking advantage of our kitten matching partner, with these added funds we
    #     will be able to provide {k:,.2f} kitten(s) to well deserving little girls
    #     all over the world including hard to reach places like Antarctica and
    #     Tacoma, WA!\n\n
    #         Sincerely,
    #         Your Friends at AFAK\n''')
    #     return letter

    @staticmethod
    def gen_letter_rdb(name):
        """
        Generate a thank you letter for the donor
        :param: donor tuple
        :returns: string with letter
        note: This doesn't actually write to a file -- that's a separate
              function. This makes it more flexible and easier to test.
        """
        k = (Donor.last_donation_rdb(name)/5 * 2)
        letter = (f'''Dear {name},
            We at the Avengers Fund-a-Kitten Initiative would like to thank you for
        your generous donation of ${Donor.last_donation_rdb(name):,.2f}.\n
        Taking advantage of our kitten matching partner, with these added funds we
        will be able to provide {k:,.2f} kitten(s) to well deserving little girls
        all over the world including hard to reach places like Antarctica and
        Tacoma, WA!\n\n
            Sincerely,
            Your Friends at AFAK\n''')
        return letter

    # def save_letters_to_disk(self):
    #     """
    #     make a letter for each donor, and save it to disk.
    #     """
    #     # create 'letters' directory if one does not exist
    #     pathlib.Path('letters').mkdir(exist_ok=True)
    #     # set the datetime format variable
    #     dt_format = '.%m-%d-%Y'
    #     for donor in self.donor_data.values():
    #         print("Writing a letter to:", donor.name)
    #         letter = self.gen_letter(donor)
    #         # I don't like spaces in filenames...
    #         filename = donor.name.replace(" ", "_")
    #         # set the file path using pathlib
    #         p = pathlib.Path('letters/' + filename +
    #                          datetime.datetime.now().strftime(dt_format) + '.txt')
    #         open(p, 'w').write(letter)

    def save_letters_to_disk_rdb():
        """
        make a letter for each donor, and save it to disk.
        """
        # create 'letters' directory if one does not exist
        pathlib.Path('letters').mkdir(exist_ok=True)
        # set the datetime format variable
        dt_format = '.%m-%d-%Y'
        for donor in Donors:
            print("Writing a letter to:", donor.donor_name)
            letter = DonorDB.gen_letter_rdb(donor.donor_name)
            # I don't like spaces in filenames...
            filename = donor.donor_name.replace(" ", "_")
            # set the file path using pathlib
            p = pathlib.Path('letters/' + filename +
                             datetime.datetime.now().strftime(dt_format) + '.txt')
            open(p, 'w').write(letter)

    # @staticmethod
    # def sort_key(item):
    #     # used to sort on name in self.donor_data
    #     return item[1]

    # def generate_donor_report(self):
    #     """
    #     Generate the report of the donors and amounts donated.
    #     :returns: the donor report as a string.
    #     """
    #     # First, reduce the raw data into a summary list view
    #     report_rows = []
    #     for donor in self.donor_data.values():
    #         name = donor.name
    #         gifts = donor.donations
    #         total_gifts = donor.total_donations
    #         num_gifts = len(gifts)
    #         avg_gift = donor.average_donation
    #         report_rows.append((name, total_gifts, num_gifts, avg_gift))
    #
    #     # sort the report data
    #     report_rows.sort(key=self.sort_key, reverse=True)
    #     report = []
    #     report.append("{:25s} | {:11s} | {:9s} | {:12s}".format("Donor Name",
    #                                                             "Total Given",
    #                                                             "Num Gifts",
    #                                                             "Average Gift"))
    #     report.append("-" * 66)
    #     for row in report_rows:
    #         report.append("{:25s}   ${:10.2f}   {:9d}   ${:11.2f}".format(*row))
    #     return "\n".join(report)

    @staticmethod
    def sort_key_rdb(item):
        return item[1]

    @staticmethod
    def generate_donor_report_rdb():
        """
        Generate the report of the donors and amounts donated.
        :returns: the donor report as a string.
        """
        # First, reduce the raw data into a summary list view
        report_rows = []
        for donor in Donors:
            name = donor.donor_name
            gifts = Donor.donations_rdb(donor.donor_name)
            total_gifts = Donor.total_donations_rdb(donor.donor_name)
            num_gifts = len(gifts)
            avg_gift = Donor.average_donation_rdb(donor.donor_name)
            report_rows.append((name, total_gifts, num_gifts, avg_gift))

        # sort the report data
        report_rows.sort(key=DonorDB.sort_key_rdb, reverse=True)
        report = []
        report.append("{:25s} | {:11s} | {:9s} | {:12s}".format("Donor Name",
                                                                "Total Given",
                                                                "Num Gifts",
                                                                "Average Gift"))
        report.append("-" * 66)
        for row in report_rows:
            report.append("{:25s}   ${:10.2f}   {:9d}   ${:11.2f}".format(*row))
        return "\n".join(report)

# User-interaction code
# Above this is all the logic code
#  The stuff you'd need if you had a totally different UI.different
#  below is code only for the command line interface.


# db = DonorDB(get_sample_data())


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
    os.system('clear')
    print('''THANK YOU Menu

Let's record that new donation and draft a THANK YOU message.\n\n''')
    while True:
        print('\nChoose an action:\n')
        print('1 - Start working on a donor entry\n'
              '2 - Enter "list" to see a list of existing donors\n'
              '3 - Enter "quit" to return to the main menu\n')
        response = input(' >> ')
        if response == '1':
            print('\nType the name of an existing or new donor.\n'
                  '(type "quit" at any time to return to the main menu)')
            name = input(' >> ')
            if name.lower() == 'quit':
                return
            amount = input('What is the donation amount? \n >> ')
            # normallize the donation amount
            amount = amount.replace('$', '').replace(',', '')
            try:
                amount = float(amount)
            except ValueError:
                print('\nNot a valid entry.  Need to enter a numerical value for the '
                      'donation amount\n')
                input('  press "Enter" to return to the THANK YOU Menu ')
                return

            # If this is a new user, ensure that the database has the necessary
            # data structure.
            # donor = db.find_donor(name)
            # if donor is None:
            #     donor = db.add_donor(name)
            DonorDB.add_donor_rdb(name)

            # Record the donation
            # donor.add_donation(amount)
            Donor.add_donation_rdb(name, amount)

            # Print thank you letter to screen
            # print(db.gen_letter(donor))
            print(DonorDB.gen_letter_rdb(name))
            input('\n  press "Enter" to return to the THANK YOU Menu ')
            os.system('clear')
            return

        elif response == 'list' or response == '2':
            os.system('clear')
            print(db.list_donors())
        elif response == 'quit' or response == '3':
            os.system('clear')
            return
        else:
            os.system('clear')
            print('not a valid response, try again\n')


def print_donor_report():
    os.system('clear')
    # print(db.generate_donor_report())
    print(DonorDB.generate_donor_report_rdb())

def quit():
    sys.exit(0)


def main():
    '''main menu function'''
    os.system('clear')
    print('''Avengers: Fund-a-Kitten Initiative

  Because every little girl
  Everywhere in the world
  ...deserves a kitten


Welcome to Mailroom\n\n''')

    selection_dict = {"1": send_thank_you,
                      "2": print_donor_report,
                      "3": DonorDB.save_letters_to_disk_rdb,
                      "4": quit}

    while True:
        selection = main_menu_selection()
        try:
            selection_dict[selection]()
        except KeyError:
            print("error: menu selection is invalid!")

if __name__ == "__main__":
    populate_sql_db()
    main()
