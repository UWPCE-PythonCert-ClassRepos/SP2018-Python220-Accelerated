#!/usr/bin/env python
"""
This is an object oriented version
"""
import os
import pprint as p
import logging
# import peewee
import sys
import math
from textwrap import dedent
import datetime
import sqlite3
from donordb_model import *

"""

Declaring donordb

"""

donorsql = os.path.abspath('donor.db')
# donordb = peewee.SqliteDatabase(donorsql)
donordb = sqlite3.connect(donorsql)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



class Donor():
    """
    class to hold the information about a single donor
    """

    def __init__(self, name, donor_id, donations=None):
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
            self.city = city
            self.phone_number = phone_number



    @staticmethod
    def normalize_name(name):
        """
        return a normalized version of a name to use as a comparison key
        simple enough to not be in a method now, but maybe you'd want to make it fancier later.
        """
        return name.lower().strip().replace(" ", "")




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


##############################################################################
#                                                                            #
#   ****** Build Notes *******                                               #
#                                                                            #
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

    def add_donor():
        """
        Add a new donor to the donor db
        :param: the name of the donor
        :returns: the new Donor data structure
        """

        donor_id = '00006'
        donor_name = 'Weezy'
        city = 'Miami'
        phone_number = '5555555555'

        try:
            with donordb:
                # conn = donordb.connect()
                cur = donordb.cursor()

            cur.execute(
                        '''INSERT INTO donor (donor_id, donor_name, city, phone_number)
                           Values (?, ?, ?, ?)
                        ''', (donor_id, donor_name, city, phone_number)
                       )

        except Exception as e:
            logger.info(e)

        finally:
            donordb.commit()


##############################################################################
#                                                                            #
#   ****** Build Notes *******                                               #
#                                                                            #
#                                                                            #
#   ****** Data Base Donor Class ******                                      #
#                                                                            #
#               amount = donation[AMOUNT],                                   #
#               donation_date = donation[DONATION_DATE],                     #
#               donor_id = donation[DONOR_ID])                               #
#                                                                            #
#                                                                            #
##############################################################################


    def add_donation():
  
        """
        Adds a new donation record into the donation table 
        """

        amount = '150000'
        donation_date = str(datetime.datetime.now().strftime('%Y-%m-%d'))
        donor_id = '00006'

        try:
            with donordb:
                # conn = donordb.connect()
                cur = donordb.cursor()

            cur.execute(
                        '''INSERT INTO donation(
                                                amount,
                                                donation_date,
                                                donor_id
                                               )
                               Values (?, ?, ?)
                        ''', (amount, donation_date, donor_id)
                       )

        except Exception as e:
            logger.info(e)

        finally:
            donordb.commit()

    """
    updates the donor table
    """

    def update_donor_info():

        donor_id = '00006'
        city = 'Riverside'

        try:
            with donordb:
                # conn = donordb.connect()
                cur = donordb.cursor()

            cur.execute(
                        '''Update donor
                           Set city = (?)
                           Where donor_id = (?)
                        ''', (city, donor_id)
                       )

            updates = '''{donor_id} has been updated
            with a new city: {city}'''.format(donor_id=donor_id, city=city)

            print(updates)

        except Exception as e:
            logger.info(e)

        finally:
            donordb.commit()
        """
        Deletes a record from the donor table 
        """

    def delete_a_donor():

        donor_id = '00006'

        try:
            with donordb:

                cur = donordb.cursor()

            cur.execute(
                        '''Delete 
                           from donor
                           Where donor_id = (?)
                        ''', (donor_id,)
                       )

            deletesuser = '''{donor_id} has been removed from the database
            the database'''.format(donor_id=donor_id)

            print(deletesuser)

        except Exception as e:
            logger.info(e)

        finally:
            donordb.commit()

    """
    Generates the last donations used for sending out letters to the
    donors

    """

    def last_donation():

        try:
            with donordb:
                cur = donordb.cursor()

                cur.execute(
                             '''
                             SELECT
                                   d.donor_id
                                  ,d.donor_name
                                  ,max(dn.donation_date) as last_donation
                             FROM donor d
                             LEFT OUTER JOIN donation dn
                             on d.donor_id = dn.donor_id
                             Group by d.donor_id, d.donor_name
                             Order by d.donor_id asc
                             '''
                            )

                col_name_list = [tuple for tuple in (('DonorID'),
                                                     ('DonorName'),
                                                     ('DonorDate'))]

                rows = cur.fetchall()
                p.pprint(col_name_list)
                for row in rows:
                    p.pprint(row)

        except Exception as e:
            logger.info(e)

    """
    Creates a donor list using SQL lite

    """

    def list_donors():

        try:
            with donordb:
                cur = donordb.cursor()

                cur.execute(
                            '''SELECT donor_id, donor_name
                               FROM donor'''
                           )

                col_name_list = [tuple[0] for tuple in cur.description]

                rows = cur.fetchall()
                p.pprint(col_name_list)

                for row in rows:
                    p.pprint(row)

        except Exception as e:
            logger.info(e)


##############################################################################
#                                                                            #
# Awesome tutorial on passing strings into a SQL query                       #
# https://www.youtube.com/watch?v=qfGu0fBfNBs                                #
#                                                                            #
##############################################################################

    def find_donorid():
        """
        Uses a sql query to return the donors name and donor_id 
        """

        finddonor = ('00002')

        try:
            with donordb:
                cur = donordb.cursor()

                cur.execute(
                            '''SELECT donor_id, donor_name
                               FROM donor
                               WHERE  donor_id = (?)
                            ''', (finddonor,)
                            )

                col_name_list = [tuple[0] for tuple in cur.description]

                rows = cur.fetchall()
                p.pprint(col_name_list)

                for row in rows:
                    p.pprint(row)

        except Exception as e:
            logger.info(e)

    """
    Generates the donors report using SQL

    """

    def generate_donor_report():

        try:
            with donordb:
                cur = donordb.cursor()

                cur.execute(
                        '''
                        SELECT 
                              Rep.donor_id as DonorID
                             ,Rep.donor_name as DonorName
                             ,Rep.donor_amount as DonorAmount
                             ,Rep.donor_number as NumberofDonations
                             ,Rep.donor_amount/Rep.donor_number as AverageGift
                        FROM
                            (
                             SELECT 
                                   d.donor_id
                                  ,d.donor_name
                                  ,sum(dn.amount) as donor_amount
                                  ,count(dn.amount) as donor_number
                                  ,null as average
                             FROM donor d
                             LEFT OUTER JOIN donation dn 
                             on d.donor_id = dn.donor_id
                             Group by d.donor_id 
                             Order by d.donor_id asc
                             )Rep
                        '''
                        )

                col_name_list = [tuple for tuple in (('DonorID'),
                                                     ('DonorName'),
                                                     ('DonorAmount'),
                                                     ('DonorNumber'),
                                                     ('AverageGift'))]

                rows = cur.fetchall()
                p.pprint(col_name_list)
                for row in rows:
                    p.pprint(row)

        except Exception as e:
            logger.info(e)


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


def user_id_input():

    userid = input("Enter donor id or 'menu' for main menu:")
    if userid.lower() -- 'menu':
        return
    else:
        return user_id

def main_menu_selection():
    """
    Print out the main application menu and then read the user input.
    """
    action = input(dedent('''
      Choose an action:
      1 - Send a Thank You
      2 - Create a Report
      3 - Send letters to everyone
      4 - Create a new donor
      5 - Add a donation
      6 - Update donor information
      7 - List all donors
      8 - Delete a donor
      9 - Quit
      > '''))
    return action.strip()


def send_thank_you():
    """
    Record a donation and generate a thank you message.
    """
    # Read a valid donor to send a thank you from, handling special commands to
    # let the user navigate as defined.
    while True:
        user_id = input("Enter a donor'id to see a desired donor"
                       "(or 'list' to see all donors or 'menu' to exit)> ").strip()
        if user_id == "list":
            print(DonorDB.list_donors())
        elif user_id == "menu":
            return
        else:
            break

    # Now prompt the user for a donation amount to apply. Since this is
    # also an exit point to the main menu, we want to make sure this is
    # # done before mutating the db.
    # while True:
    #     amount_str = input("Enter a donation amount (or 'menu' to exit)> ").strip()
    #     if amount_str == "menu":
    #         return
    #     # Make sure amount is a valid amount before leaving the input loop
    #     try:
    #         amount = float(amount_str)
    #         # extra check here -- unlikely that someone will type "NaN", but
    #         # it IS possible, and it is a valid floating point number:
    #         # http://en.wikipedia.org/wiki/NaN
    #         if math.isnan(amount) or math.isinf(amount) or round(amount, 2) == 0.00:
    #             raise ValueError
    #     # in this case, the ValueError could be raised by the float() call, or by the NaN-check
    #     except ValueError:
    #         print("error: donation amount is invalid\n")
    #     else:
    #         break

    # If this is a new user, ensure that the database has the necessary
    # data structure.
    donor = DonorDB.find_donorid(user_id)
    if donor is None:
        donor = print('Add a New User') ##DonorDB.add_donor(user_id)

    # Record the donation
    # donor.add_donation(amount)
    # print(db.gen_letter(donor))


# def print_donor_report():
#     print(db.generate_donor_report())


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
                      "2": DonorDB.generate_donor_report,
                      # "3": save_letters_to_disk,
                      "4": DonorDB.add_donor,
                      "5": DonorDB.add_donation,
                      "6": DonorDB.update_donor_info,
                      "7": DonorDB.list_donors,
                      "8": DonorDB.delete_a_donor,
                      "9": quit}

    while True:
        selection = main_menu_selection()
        try:
            selection_dict[selection]()
        except KeyError:
            print("error: menu selection is invalid!")

if __name__ == "__main__":

    main()