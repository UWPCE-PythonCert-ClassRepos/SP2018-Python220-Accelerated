#!/usr/bin/env python3

"""
simple mailroom program for a non profit
"""

# Currently does not succesfully load the JSON file, defaults to
# a "None" database. 

import sys

import json_save.json_save.json_save_dec as js


@js.json_save
class Donations():

    # new addition
    #string --> Donor name
    # donor_name = js.String()

    #list --> Donations made by donor
    donations = js.Dict()


    def __init__(self, donations = None):

        if donations is None:
            self.donations = {}
        else:
            self.donations = donations

    def __str__(self):
        return str(self.donations)

    def add_donation(self, name, amount):
        self.donations.setdefault(name, []).append(amount)

    def generate_report(self):
        report = []
        report_data = []

        header = ("{:<25s} | {:^15s} | {:^10s} | {:15s}".format(
            "Donor Name", "Total Given", "Num Gifts", "Average Gift"))
        divider = "_" * len(header)

        report.append(header)
        report.append(divider)

        for key_name in self.donations:
            name = key_name
            total_given = sum(self.donations[key_name])
            total_count = len(self.donations[key_name])
            avg_given = total_given / total_count
            report_data.append((name, total_given, total_count, avg_given))

        # Sort with respect to "Total Given" value.
        report_data.sort(key=donations, reverse=True)

        # Adding the data into report with formatting
        for data in report_data:
            report.append(
                "{:25s}   ${:14.2f}   {:10d}   ${:11.2f}".format(* data))

        printable_report = ("\n").join(report)

        return printable_report

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
    # This section is the new portions for the JSON stuffs

    def save_donor_database(self, filename = "donor_database.json"):
        with open(filename, 'w') as out_file:
            self.to_json(out_file)
    
    @classmethod
    def load_donor_database(self, filename = "donor_database.json"):
        with open(filename, 'r') as in_file:
            return js.from_json(in_file)


    # -------------------------------------------------------------

def thank_you():
    """
    Get into the thank you note generation portion of the program
    """

    options_dict = {"1": add_donation,
                    "2": display_donors,
                    "3": return_to_menu}

    menu_string = """== Send a Thank You ===

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

    print(donation_db.names_of_donors())


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

    donation_db = Donations()
    print("...initiating...")

    print(donation_db)
    mainloop()
