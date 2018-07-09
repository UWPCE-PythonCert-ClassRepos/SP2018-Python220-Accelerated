# #!/usr/bin/env python3
#
import sys
import math
from textwrap import dedent
import logging
import datetime
import pathlib
import os
from lesson07.relationaldb_mailroom_schema import *


def populate_sql_db():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    db = SqliteDatabase('mailroom.db')

    """
    Add Donor data to the database
    """

    logger.info('Working with the Donor class')

    donors = [('Andrew', 'Picowsky', 'Andy@example.com', '206-559-3249'),
              ('Peter', 'Wolfe', 'Peter@example.com', '450-565-3242'),
              ('Susan', 'Que', 'Susan@example.com', '342-466-0934'),
              ('Pam', 'Potts',  'Pam@example.com', '123-495-9714'),
              ('Steven', 'Colbert',  'Steven@example.com', '325-950-0274')]

    logger.info('Creating Donor records')

    try:
        db.connect()
        db.execute_sql('PRAGMA foreign_keys = ON;')
        for donor in donors:
            with db.transaction():
                new_donor = Donor.create(
                     first_name=donor[0],
                     last_name=donor[1],
                     email=donor[2],
                     phone=donor[3])
                new_donor.save()
                logger.info('Database add successful')

        logger.info('The following donor records have been saved:')

        for saved_donor in Donor:
                logger.info(f'{saved_donor.first_name} {saved_donor.last_name}\'s email and phone are '
                            f'{saved_donor.email} and {saved_donor.phone}.')

    except Exception as y:
        logger.info(f'Error creating = {donor[0, 1]}')
        logger.info(y)

    """
    Add donations to the database
    """

    logger.info("Working with the Donation class")

    donations = [('Andrew', '2018-01-01', 342.32),
                 ('Peter', '2018-02-14', 50.00),
                 ('Susan', '2018-04-01', 100.00),
                 ('Pam', '2018-02-28', 75.00),
                 ('Steven', '2018-03-23', 25.00)]

    try:
        for donation in donations:
            donor_record = Donor.get(Donor.first_name == donation[0])
            new_donation = Donation.create(
                donor_id=donor_record.id,
                date=donation[1],
                donation=donation[2])
            new_donation.save()
            logger.info("Database add successful")

        logger.info('The following donation records have been saved:')
        for saved_donation in Donation:
            logger.info(f'Donor {saved_donation.donor_id} donated {saved_donation.donation} '
                        f'at {saved_donation.date}')

    except Exception as e:
        logger.info(f'Error creating donation records for donor {donations[0]}')
        logger.exception(e)

    finally:
        logger.info("DB closing")
        db.close()


# class Donor:
#     """
#     class to hold the information about a single donor
#     """
#
#     def __init__(self, name, donations=None):
#         """
#         create a new Donor object
#         :param name: name of the donor
#         :param donations=None: iterable of past donations
#         """
#         self.norm_name = self.normalize_name(name)
#         self.name = name.strip()
#         if donations is None:
#             self.donations = []
#         else:
#             self.donations = list(donations)
#
#     @staticmethod
#     def normalize_name(name):
#         """
#         return a normalized version of a name to use as a comparison key
#         simple enough to not be in a method now, but maybe you'd want to make it fancier later.
#         """
#         return name.lower().strip().replace(" ", "")
#
#     @staticmethod
#     def donations_db(name):
#         query = (Donor.select(Donor, Donation).join(Donation)
#                  .where(Donor.donor_name_normalized == name.lower()))
#         donations = list(d.donation.donations for d in query)
#
#         return donations
#
#     @staticmethod
#     def last_donation_db(name):
#         """
#         The most recent donation made
#         """
#         query = (Donor.select(Donor, Donation).join(Donation)
#                  .where(Donor.donor_name_normalized == name.lower()))
#         donations = list(d.donation.donations for d in query)
#         try:
#             return donations[-1]
#         except IndexError:
#             return 0
#
#     @staticmethod
#     def total_donations_db(name):
#         query = (Donor.select(Donor, Donation).join(Donation)
#                  .where(Donor.donor_name_normalized == name.lower()))
#         donations = list(d.donation.donations for d in query)
#         return sum(donations)
#
#     @staticmethod
#     def average_donation_db(name):
#         query = (Donor.select(Donor, Donation).join(Donation)
#                  .where(Donor.donor_name_normalized == name.lower()))
#         donations = list(d.donation.donations for d in query)
#         return sum(donations) / len(donations)
#
#     @staticmethod
#     def add_donation_db(name, amount):
#         """
#         add a new donation
#         """
#         amount = float(amount)
#         if amount <= 0.0:
#             raise ValueError("Donation must be greater than zero")
#         id = Donor.select().where(Donor.donor_name_normalized == name.lower()).get()
#         new_donation = Donation.create(donor=id, donation=amount)
#         new_donation.save()
#
#
# class DonorDB:
#     """
#     encapsulation of the entire database of donors and data associated with them.
#     """
#
#     def __init__(self, donors=None):
#         """
#         Initialize a new donor database
#         :param donors=None: iterable of Donor objects
#         """
#         if donors is None:
#             self.donor_data = {}
#         else:
#             self.donor_data = {d.norm_name: d for d in donors}
#
#     # def save_to_file(self, filename):
#     #     with open(filename, 'w') as outfile:
#     #         self.to_json(outfile)
#
#     # @classmethod
#     # def load_from_file(cls, filename):
#     #     with open(filename, 'r') as infile:
#     #         obj = js.from_json(infile)
#     #     return obj
#
#     @staticmethod
#     def list_donors_db():
#         """
#         creates a list of the donors as a string, so they can be printed
#         Not calling print from here makes it more flexible and easier to
#         test
#         """
#         listing = ["Donor list:"]
#         for donor in Donor:
#             listing.append(donor.first_name)
#         return "\n".join(listing)
#
#     @staticmethod
#     def add_donor_db(name):
#         """
#         Add a new donor to the donor db
#         :param: the name of the donor
#         :returns: the new Donor data structure
#         """
#         query = Donor.select().where(Donor.donor_name_normalized == name.lower())
#         if query.exists():
#             return None
#         # add new donor if doesn't already exist
#         else:
#             try:
#                 new_donor = Donor.create(donor_name=name,
#                                          donor_name_normalized=name.lower())
#                 new_donor.save()
#             except Exception as e:
#                 print(e)
#                 id = Donor.select().where(Donor.donor_name_normalized == name.lower()).get()
#
#         return id
#
#     @staticmethod
#     def gen_letter_db(name):
#         """
#         Generate a thank you letter for the donor
#         :param: donor tuple
#         :returns: string with letter
#         note: This doesn't actually write to a file -- that's a separate
#               function. This makes it more flexible and easier to test.
#         """
#         c = Donor.last_donation_db(name)
#         return dedent(f'''Dear {name},
#                             Thank you for your very kind donation of ${c:.2f}.
#                           It will be put to very good use.
#                              Sincerely,
#                                 -The Team''')
#
#     @staticmethod
#     def sort_key_db(item):
#         return item[1]
#
#     @staticmethod
#     def generate_donor_report_db(name):
#         """
#         Generate the report of the donors and amounts donated.
#         :returns: the donor report as a string.
#         """
#         # First, reduce the raw data into a summary list view
#         report_rows = []
#         for donor in Donor:
#             name = donor.first_name
#             gifts = Donor.donations_db(donor.first_name)
#             total_gifts = Donor.total_donations_db(donor.first_name)
#             num_gifts = len(gifts)
#             avg_gift = Donor.average_donation(donor.first_name)
#             report_rows.append((name, total_gifts, num_gifts, avg_gift))
#
#         # sort the report data
#         report_rows.sort(key=DonorDB.sort_key)
#         report = []
#         report.append("{:25s} | {:11s} | {:9s} | {:12s}".format("Donor Name",
#                                                                 "Total Given",
#                                                                 "Num Gifts",
#                                                                 "Average Gift"))
#         report.append("-" * 66)
#         for row in report_rows:
#             report.append("{:25s}   ${:10.2f}   {:9d}   ${:11.2f}".format(*row))
#         return "\n".join(report)
#
#     @staticmethod
#     def save_letters_to_disk_db():
#         """
#         make a letter for each donor, and save it to disk.
#         """
#         # create 'letters' directory if one does not exist
#         pathlib.Path('letters').mkdir(exist_ok=True)
#         # set the datetime format variable
#         dt_format = '.%m-%d-%Y'
#
#         for donor in Donor:
#             print("Writing a letter to:", donor.first_name)
#             letter = DonorDB.gen_letter_db(donor.first_name)
#             # I don't like spaces in filenames...
#             filename = donor.donor_name.replace(" ", "_")
#             # set the file path using pathlib
#             p = pathlib.Path('letters/' + filename + datetime.datetime.now().strftime(dt_format) + '.txt')
#             open(p, 'w').write(letter)
#
#
# def main_menu_selection():
#     """
#     Print out the main application menu and then read the user input.
#     """
#     action = input(dedent('''
#       Choose an action:
#       1 - Send a Thank You
#       2 - Create a Report
#       3 - Send letters to everyone
#       4 - Quit
#       > '''))
#     return action.strip()
#
#
# def send_thank_you():
#     """
#     Record a donation and generate a thank you message.
#     """
#     # Read a valid donor to send a thank you from, handling special commands to
#     # let the user navigate as defined.
#     os.system("Clear")
#
#     print("Welcome to the Thank You menu. Please select from the following options.\n")
#     response = input("1 - Start working on a donation entry\n"
#                      "2 - Enter 'List' to see a list of existing donors\n"
#                      "3 - Enter 'Quit' to return to the main menu\n"
#                      ">> ")
#     if response == "1":
#         print("\nType the name of an existing or new donor\n"
#               "or type 'Quit' at any time to return to the main menu")
#         name = input(">> ")
#         if name.lower() == "quit":
#                 return
#         amount = input("How much are they donating? \n >> $  ")
#         # normalize the donation amount
#         amount = amount.replace(',', '')
#         try:
#             amount = float(amount)
#         except ValueError:
#             print("\nThat wasn't a valid entry. Please enter a numerical amount for donations.\n")
#             input("Press 'Enter' to return to the Thank You Menu")
#             return
#
#         # If this is a new user, ensure that the database has the necessary
#         # data structure.
#         DonorDB.add_donor_db(name)
#
#         # Record the donation
#         Donor.add_donation_db(name, amount)
#
#         # Print thank you letter to screen
#         print(DonorDB.gen_letter_db(name))
#         input("\n press 'Enter' to return to the Thank You Menu ")
#         os.system("Clear")
#         return
#
#     elif response.lower() == 'list' or response == '2':
#         os.system("Clear")
#         print(DonorDB.list_donors_db())
#     elif response.lower() == 'quit' or response == '3':
#         os.system("Clear")
#         return
#     else:
#         os.system("Clear")
#         print("Not a valid response. Please enter 1, 2, or 3\n")
#
#
# def print_donor_report():
#     print(DonorDB.generate_donor_report_db())
#
#
# def _quit():
#     sys.exit(0)
#
#
# def main():
#     selection_dict = {"1": send_thank_you,
#                       "2": print_donor_report,
#                       "3": DonorDB.save_letters_to_disk_db,
#                       "4": _quit}
#
#     while True:
#         selection = main_menu_selection()
#         try:
#             selection_dict[selection]()
#         except KeyError:
#             print("error: menu selection is invalid!")


if __name__ == "__main__":
    populate_sql_db()
    # main()

"""
This is still broken. populate_sql_db work beautifully and on its own as I expected. I strongly believe that using
a name (first or last), email, phone number, or address (literally everything that i would think to need to collect
about a person for a donation) are not unique. For example, my parents share an email and phone, John Smith is a very
common name. For a large scale and scalable database full of people data, I think that the only sure fire way to
ensure that no data gets duplicated is to use a uniquely generated key.

I got unique keys working (OMG this took me so long) with peewee in my
schema, as demonstrated by only running populate_sql_db(), however i'm really struggling with converting the rest of
the code inherited here to use a unique key instead of "normalized name."

I think that the rest of the code is appropriately converted to utilize the sql database, however i keep getting
PrimaryKey errors and I've dumped upwards of 10 hours into trying to figure out the key error situation- re reading all
the readings and re watching the videos for this lesson, reading most of the current v. peewee documentation ect.
"""
