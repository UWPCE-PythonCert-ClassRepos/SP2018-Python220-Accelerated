#!/usr/bin/env python3

"""
simple mailroom program for a non profit
"""
import sys
from peewee import *
from model import Donor, Donation



class Donations():

    def __init__(self, donations=None):

        if donations is None:
            self.donations = {}
        else:
            self.donations = donations

    def __str__(self):
        return str(self.donations)

    def add_donation(self, name, amount):
        
        database = SqliteDatabase('mailroom_database.db')

        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')

        # checking to see if name exists in Donors db.
        # not the best way to check... but it works. 
        try:
            donor = Donor.get(Donor.donor_name == name) 
        except:
            donor = None

        # this instead????
        # donor = Donor.get_or_none(Donor.donor_name == name)

        # if the name that was entered is not already in the database, create a new Donor.
        if donor is None:
            print("{} is a new donor and will be added to the database\n".format(name))
            city = input("Please enter the city this donor is from:\n")
            state = input("Please enter the state or country this donor is from:\n")

            new_donor = Donor.create(
                                    donor_name = name,
                                    donor_city = city,
                                    donor_state = state 
                                    )
            new_donor.save()
            print("{} was added to the database! \n".format(name))
        
        # if the name does exist int he database of donors, confirms that the donor was found.
        else:
            print("{} was found in the database!\n".format(donor))

        # Add the amount of the donation to database.

        new_donation = Donation.create(
            donation_amount = amount,
            donation_donor = name)
        new_donation.save()

        print("{}'s donation amount of ${} was added to the database!".format(name, amount))

        database.close()

        # below was how it was done
        # self.donations.setdefault(name, []).append(amount)
        

    def generate_report(self):
        # generate a report showing all donors, their total donated amount, average 
        # and count of donations

        # Prepping the header and report list. 
        report = []
        report_data = []

        header = ("{:<25s} | {:^15s} | {:^10s} | {:15s}".format(
            "Donor Name", "Total Given", "Num Gifts", "Average Gift"))
        divider = "_" * len(header)

        # Accessing the database
        report.append(header)
        report.append(divider)

        database = SqliteDatabase('mailroom_database.db')

        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')

        # trying to scan through Donor model, which has each person only once.
        # Then trying to find all occurences of this donor in Donation.
        # Get the donation_amount from each donor, put into a list and do the 
        # necessary math to get to the total given, number of donations and 
        # the average of their donations.


        
        report_data.append((donor.donor_name, total_given, donation_count, average_given))

        # Adding the data into report with formatting
        for data in report_data:
            report.append(
                "{:25s}   ${:14.2f}   {:10d}   ${:11.2f}".format(* data))

        printable_report = ("\n").join(report)

        return printable_report

        # ============= Original version below ============= #
        # report = []
        # report_data = []

        # header = ("{:<25s} | {:^15s} | {:^10s} | {:15s}".format(
        #     "Donor Name", "Total Given", "Num Gifts", "Average Gift"))
        # divider = "_" * len(header)

        # report.append(header)
        # report.append(divider)

        # for key_name in self.donations:
        #     name = key_name
        #     total_given = sum(self.donations[key_name])
        #     total_count = len(self.donations[key_name])
        #     avg_given = total_given / total_count
        #     report_data.append((name, total_given, total_count, avg_given))

        # # Sort with respect to "Total Given" value.
        # report_data.sort(key=donations, reverse=True)

        # # Adding the data into report with formatting
        # for data in report_data:
        #     report.append(
        #         "{:25s}   ${:14.2f}   {:10d}   ${:11.2f}".format(* data))

        # printable_report = ("\n").join(report)

        # return printable_report

    def generate_letter(self):

        print("== Send letters to everyone ==")

        for key_name in self.donations:
            file = open("Letter_for_" + key_name + ".txt", "w")

            letter = ("Dear " + key_name + ",\n\n" +
                      "Thank you for your recent donation of $" +
                      "%.2f" % self.donations[key_name][-1] + ".\n\n" +
                      "It will be put to very good use.\n\n" +
                      "Sincerely,\n\n" + "-The Team")

            file.write(letter)

            file.close()

    # @property
    # def donation_count(self, name):
    #     len(self.donations[name])

    # @property
    # def donation_total(self, name):
    #     sum(self.donations[name])

    # @property
    # def donation_average(self, name):
    #     sum(self.donations[name]) / len(self.donations[name])

    @property
    def last_donated(self, name):
        return self.donations[name][-1]

    def names_of_donors(self):

        donors = []

        donors.append("Here is the list of donors:")

        for name in self.donations:
            donors.append(name)

        printable_donors = "\n".join(donors)

        return printable_donors


# -------------------------------------------------------------

def thank_you():
    """
    Get into the thank you note generation portion of the program
    """

    options_dict = {"1": add_donation,
                    "2": display_donors,
                    "3": return_to_menu}

    menu_string = """\n== Send a Thank You ===

    1) Add a new donation (creates new donor profile if a new donor is entered)
    2) Display a list of donors
    3) Back\n"""

    run_loop(options_dict, menu_string)


def input_loop_for_add_donation():

    while True:
        print("Please enter the amount donated:\n")
        input_amount = check_if_number(input(">>"))

        if input_amount:
            return input_amount


def check_if_number(response):

    try:
        donation_amount = float(response)
        return donation_amount
    except ValueError:
        print("invalid input")
        return False


def add_donation():

    print("Please enter the name of the donor:\n")
    donor_name = input(">>")

    donation_amount = input_loop_for_add_donation()

    # while True:
    #     print("Please enter the amount " + donor_name + " donated:\n")
    #     entered_amount = input(">>")
    #     donation_amount = check_if_number(entered_amount)

    donation_db.add_donation(donor_name, donation_amount)


def display_donors():
    """
    Display a list of the donors in the database
    """
    
    database = SqliteDatabase('mailroom_database.db')

    print("The following is a list of all donors:")

    database.connect()
    database.execute_sql('PRAGMA foreign_keys = ON;')

    for donor in Donor:
        print(donor.donor_name)
    
    database.close()

    # print(donation_db.names_of_donors())


def donations(keys):
    return keys[1]


def print_report():

    print(donation_db.generate_report())


def letters():

    donation_db.generate_letter()


def quit_menu():

    options_dict = {"1": quit, "2": return_to_menu}

    menu_string = """Are you sure you want to quit?
    1) Yes, quit
    2) Back?\n"""

    run_loop(options_dict, menu_string)


def quit():

    sys.exit()


def run_loop(arg_dict, menu_string):

    while True:
        print(menu_string)
        user_input = input(">>")

        if user_input:
            result = selection(arg_dict, user_input)

            if result:
                return


def selection(arg_dict, answer):
    try:
        return arg_dict[answer]()
    except (KeyError):
        return False


def return_to_menu():

    return True


def delete_donor(name):
    """
    Haven't really tested this code
    """

    # database.connect()
    # database.execute_sql('PRAGMA foreign_keys = ON;')

    # donor = Donor.get_or_none(Donor.donor_name == name)

    # # if there is a match, delete
    # if donor is not None:
    #     donor.delete_instance()

    # database.close()

    pass

# -------------------------------------------------------------

def mainloop():

    options_dict = {"1": thank_you, "2": print_report,
                    "3": letters, "4": quit_menu}
    menu_string = """Welcome to Mailroom!
Please select one of the following options:
    1) Thank You
    2) Report
    3) Send etters to everyone
    4) Quit\n"""

    run_loop(options_dict, menu_string)


if __name__ == "__main__":

    DONORS = {'Sir Isaac Newton': [100.38, 2, 4, 5000.98],
              'Zach de la Rocha': [1000.76, 5, 235.90, 50.76],
              'Space Ghost': [1, 5, 900000, 76.45]
            }

    donation_db = Donations(DONORS)
    print("...initiating...")
    mainloop()
