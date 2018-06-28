#!/usr/bin/env python
"""
This is an object oriented version
"""
import os
import logging
import peewee
import sys
import math
from textwrap import dedent
import datetime
from donordb_model import *

"""

Declaring donordb

"""

donorsql = os.path('donor.db')
donordb = peewee.SqliteDatabase(donorsql)


class Donor():
    """
    class to hold the information about a single donor
    """

    def __init__(self, name, donations=None):
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
            self.donor_id = donor_id
            self.city
            self.phone_number

    @staticmethod
    def donations_rdb(name):
        query = (Donors.select(Donors, Donation).join(Donation)
                 .where(Donors.donor_name_normalized == name.lower()))
        donations = list(d.donation.donation for d in query)
        return donations


    @staticmethod
    def normalize_name(name):
        """
        return a normalized version of a name to use as a comparison key
        simple enough to not be in a method now, but maybe you'd want to make it fancier later.
        """
        return name.lower().strip().replace(" ", "")

    @property
    def last_donation(self):
        """
        The most recent donation made
        """
       query = (Donors.select(Donors, Donation).join(Donation)
                 .where(Donors.donor_name_normalized == name.lower()))
        donations = list(d.donations.donation for d in query)
        try:
            return donations[-1]
        except IndexError:
            return 0

    @property
    def total_donations(self):
        query = (Donors.select(Donors, Donations).join(Donations)
                 .where(Donors.donor_name_normalized == name.lower()))
        donations = list(d.donations.donation for d in query)
        return sum(donations)

    @property
    def average_donation(name):
        query = (Donors.select(Donors, Donations).join(Donations)
                 .where(Donors.donor_name_normalized == name.lower()))
        donations = list(d.donations.donation for d in query)
        try:
            return sum(donations) / len(query)
        except ZeroDivisionError:
            return 0

    def add_donation(name, amount):
        """
        add a new donation
        """
        amount = float(amount)
        if amount <= 0.0:
            raise ValueError("Invalid Donation Amount")
        id = Donors.select().where(Donors.donor_name_normalized == name.lower()).get()
        new_donation = Donations.create(
            donor=id,
            donation=amount)
        new_donation.save()

class DonorDB():
    """
    encapsulation of the entire database of donors and data associated with them.
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

    @property
    def donors(self):
        """
        an iterable of all the donors
        """
        return self.donor_data.values()

    def list_donors(self):  #<---- select * from donors 
        """
        creates a list of the donors as a string, so they can be printed
        Not calling print from here makes it more flexible and easier to
        test
        """
        listing = ["Donor list:"]
        for donor in self.donors:
            listing.append(donor.name)
        return "\n".join(listing)

    def find_donor(self, name):
        """
        find a donor in the donor db
        :param: the name of the donor
        :returns: The donor data structure -- None if not in the self.donor_data
        """
        return self.donor_data.get(Donor.normalize_name(name))


##############################################################################
#                                                                            #
#   ****** Build Notes *******                                               #
#                                                                            #
#   Taken from personjob_learning_v3_p1.py                                   #
#                                                                            #
#    try:                                                                    #
#       database.connect()                                                   #
#       database.execute_sql('PRAGMA foreign_keys = ON;')                    #
#       for person in people:                                                #
#           with database.transaction():                                     #
#               new_person = Person.create(                                  #
#                       person_name = person[PERSON_NAME],                   #
#                       lives_in_town = person[LIVES_IN_TOWN],               #
#                       nickname = person[NICKNAME])                         #
#               new_person.save()                                            #
#        except Exception as e:                                              #
#                                                                            #
#           finally:                                                         #
#       logger.info('database closes')                                       #
#       database.close()                                                     #
#                                                                            #
#   ****** Data Base Donor Class ******                                      #
#                                                                            #
#       donor_id = donor[DONOR_ID],                                          #
#               donor_name = donor[DONOR_NAME],                              #
#               city = donor[CITY],                                          #
#               phone_number = donor[PHONE_NUMBER])                          #
#                                                                            #
#                                                                            #
##############################################################################


   def add_donor(self, name):
        """
        Add a new donor to the donor db
        :param: the name of the donor
        :returns: the new Donor data structure
        """

        try:
        donordb.connect()
        donordb.execute_sql('PRAGMA foreign_keys = ON;')

        for donor in donors:
            with database.transaction():   
                new_donor = Donor.create(
                    donor_id=donorid,
                    donor_name=donor_name,
                    donor_city=donor_city,
                    phone_number=phone_number)
                new_donor.save()
        logger.info('new donor has been added and saved')
                logger.info('display new donor')
        newdonor = Donor.get(donor_name=donor_name)

        logger.info(f'{newdonor.donor_name} was recently created')

            except Exception as e:
        logger.info(e)

    finally:
        donordb.close()


##############################################################################
#                                                                            #
#   ****** Build Notes *******                                               #
#                                                                            #
#   Taken from personjob_learning_v3_p1.py                                   #
#                                                                            #
#   ****** Data Base Donor Class ******                                      #
#                                                                            #
#               amount = donation[AMOUNT],                                   #
#               donation_date = donation[DONATION_DATE],                     #
#               donor_id = donation[DONOR_ID])                               #
#                                                                            #
#                                                                            #
##############################################################################


    def add_donation(donor_id, amount)
    try:
        donordb.connect()
        donordb.execute_sql('PRAGMA foreign_keys = ON;')

        donation_date = date.today()

            with database.transaction():   
                new_donation = Donation.create(
                    amount=amount,
                    donation_date=donation_date,
                    donor_id=donor_id)
                new_donation.save()
        logger.info('a new donation has been added and saved')
                logger.info('display recently added donation')
        newdonation = Donation.get(donor_name=donor_name)

        logger.info(f'{newdonor.donor_name} was recently created')

            except Exception as e:
        logger.info(e)

    finally:
        donordb.close()



##############################################################################
#                                                                            #
#   ****** Build Notes *******                                               #
#                                                                            #
#   Taken from personjob_learning_v3_p3.py                                   #
#                                                                            #
#    try:                                                                    #
#       database.connect()                                                   #
#       database.execute_sql('PRAGMA foreign_keys = ON;')                    #
#                                                                            #
#           with database.transaction():                                     #
#                aperson = Person.get(Person.person_name == 'Andrew')        #
#                logger.info(f'Trying to delete {aperson.person_name}        #
#                              who lives in {aperson.lives_in_town}')        #
#                aperson.delete_instance()                                   #
#                                                                            #
#        except Exception as e:                                              #
#                                                                            #
#        finally:                                                            #
#            database.close()                                                #
#                                                                            #
#                                                                            #
#                                                                            #
#                                                                            #
##############################################################################


    def delete_donor_record(donor_id):

        try:
            database.connect()
            database.execute_sql('PRAGMA foreign_keys = ON;')

        for donor in donors:
            with database.transaction():
                adonor = Donor.get(Donor.donor_id == '00006')
                logger.info(f'''Deleting record of {adonor.donor_name} with
                                Donor id # {adonor.donor_id}''')
                aperson.delete_instance()

            logger.info('Showing remaining donors')
            for donor in donors:
            logger.info(f"{donor.donor_id} | {donor.donor_name} | {donor.donor_city} | {donor.phone_number}")

        except Exception as e:
            logger.info(e)

        finally:
            database.close()



    def gen_letter(self, donor):
        """
        Generate a thank you letter for the donor
        :param: donor tuple
        :returns: string with letter
        note: This doesn't actually write to a file -- that's a separate
              function. This makes it more flexible and easier to test.
        """
        return dedent('''Dear {0:s},
              Thank you for your very kind donation of ${1:.2f}.
              It will be put to very good use.
                             Sincerely,
                                -The Team
              '''.format(donor.name, donor.last_donation)
                      )

    @staticmethod
    def sort_key(item):
        # used to sort on name in self.donor_data
        return item[1]

    def generate_donor_report(self):
        """
        Generate the report of the donors and amounts donated.
        :returns: the donor report as a string.
        """
        # First, reduce the raw data into a summary list view
        report_rows = []
        for donor in self.donor_data.values():
            name = donor.name
            gifts = donor.donations
            total_gifts = donor.total_donations
            num_gifts = len(gifts)
            avg_gift = donor.average_donation
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
        for donor in self.donor_data.values():
            print("Writing a letter to:", donor.name)
            letter = self.gen_letter(donor)
            # I don't like spaces in filenames...
            filename = donor.name.replace(" ", "_") + ".txt"
            open(filename, 'w').write(letter)


# User-interaction code
# Above this is all the logic code
#  The stuff you'd need if you had a totally different UI.different
#  below is code only for the command line interface.


# import sys
# import math

# # handy utility to make pretty printing easier
# from textwrap import dedent

# from mailroom import model

# create a DB with the sample data
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
    while True:
        name = input("Enter a donor's name"
                     "(or 'list' to see all donors or 'menu' to exit)> ").strip()
        if name == "list":
            print(db.list_donors())
        elif name == "menu":
            return
        else:
            break

    # Now prompt the user for a donation amount to apply. Since this is
    # also an exit point to the main menu, we want to make sure this is
    # done before mutating the db.
    while True:
        amount_str = input("Enter a donation amount (or 'menu' to exit)> ").strip()
        if amount_str == "menu":
            return
        # Make sure amount is a valid amount before leaving the input loop
        try:
            amount = float(amount_str)
            # extra check here -- unlikely that someone will type "NaN", but
            # it IS possible, and it is a valid floating point number:
            # http://en.wikipedia.org/wiki/NaN
            if math.isnan(amount) or math.isinf(amount) or round(amount, 2) == 0.00:
                raise ValueError
        # in this case, the ValueError could be raised by the float() call, or by the NaN-check
        except ValueError:
            print("error: donation amount is invalid\n")
        else:
            break

    # If this is a new user, ensure that the database has the necessary
    # data structure.
    donor = db.find_donor(name)
    if donor is None:
        donor = db.add_donor(name)

    # Record the donation
    donor.add_donation(amount)
    print(db.gen_letter(donor))


def print_donor_report():
    print(db.generate_donor_report())


def quit():
    sys.exit(0)

"""

Updated Main menu to reflect the new functionality from mailroom. The following
features need to be added for easier usability: 

    * create donor
    * add a donation 
    * update donor record 
    * list all donors
    * delete a donor 

"""

def main():
    selection_dict = {"1": send_thank_you,
                      "2": print_donor_report,
                      "3": db.save_letters_to_disk,
                      "4": 
                      "5":
                      "6":
                      "7":
                      "8":
                      "9": quit}

    while True:
        selection = main_menu_selection()
        try:
            selection_dict[selection]()
        except KeyError:
            print("error: menu selection is invalid!")

if __name__ == "__main__":

    main()