"""
Simple mailroom program for a non profit
"""

# Start with interactive loop

import sys
import math

from textwrap import dedent


"""
The following section of code pertain to the building and manipulation of the
donors database.
"""

# ----------------------------------------------------------------------------
#
# Built a sample database and put it into a dict format
#
# ----------------------------------------------------------------------------


def find_donor_db():
    return{'dave grohl': ("Dave Grohl", [999999.99, 45.63]),
           'billy joe armstrong': ("Billy Joe Armstrong", [15000, 2222]),
           'rivers cuomo': ("Rivers Cuomo", [1994.96, 2100000]),
           }

# ----------------------------------------------------------------------------
#
# Building donor class that handles all items pertaining to storing a donor
#
# ----------------------------------------------------------------------------


class Donor():
    def __init__(self, name, donations=None):
        self.uni_name = self.universal_name(name)
        self.name = name.strip()
        self.donations = [] if donations is None else list(donations)

# Used to return a key

    @staticmethod
    def universal_name(name):
        return name.lower().strip().replace(" ", "")

    # @property
    # def donations(self):
    #     return self._donations

    def add_donation(self, amount):
        amount = float(amount)
        if amount <= 0.0:
            raise ValueError("Donation must be greater than zero")
        self.donations.append(amount)

    @property
    def total_donations(self):
        return sum(self.donations)

    @property
    def average_donation(self):
        return self.total_donations / len(self.donations)

    @property
    def last_donation(self):
        return self.donations[-1]

# ----------------------------------------------------------------------------
#
# Building db class that handles all items pertaining to adding and storing
# donor information
#
# ----------------------------------------------------------------------------


class DonorData():
    def __init__(self, donors=None):
        if donors is None:
            self.donor_data = {}
        else:
            self.donor_data = {Donor.universal_name: d for d in donors}

    @property
    def donors(self):
        return self.donor_data.values()

    def add_donor(self, name):
        donor = Donor(name)
        self.donor_data[Donor.universal_name] = donor
        return donor

    # def get_total_from_donor(self, donor_name):
    #     return self.donors[donor_name.lower()].total_donations

    def list_donors(self):
        listing = ["Donors:"]
        for donor in self.donors:
            listing.append(donor.name)
        return "\n".join(listing)

    def search_donor_db(self, name):
        return self.donor_data.get(Donor.universal_name(name))
    #     # return donor_db.get(key)

    @staticmethod
    def sort_key(item):
        return item[1]

    # @property
    # def num_donors(self):
    #     return len(donors)

    # ----------------------------------------------------------------------------
#
# Builds the donor report and displays the name, total given, number of gifts
# and the average gift donated by the donor.
#
# ----------------------------------------------------------------------------

    def donor_report(self):

        report_rows = []
        for donor in self.donor_data.values():
            name = donor.name
            donations = donor.donations
            total_donations = donor.total_donations
            num_donations = len(donations)
            avg_donation = donor.average_donation
            report_rows.append((name, total_donations, num_donations, avg_donation))

        report_rows.sort(key=self.sort_key)
        report = []
        report.append("{:25s} | {:11s} | {:9s} | {:12s}".format("Donor Name",
                                                                "Total Donated",
                                                                "Num gifts",
                                                                "Average Donation"))
        report.append("_" * 66)
        for row in report_rows:
            report.append("{:25s}   ${:10.2f}   ${:9d}   ${:11.2f}".format(*row))
        return "\n".join(report)

# ----------------------------------------------------------------------------
#
# Makes a standardized letter template that passes through the donor name and
# and the amount donated
#
# ----------------------------------------------------------------------------

    def write_letter(self, donor):

        return dedent('''Dear {0:s},

            Thank you for your kind doation of ${1:.2f}.
            We will make sure that it is put to very good use.

                                    Sincerely,
                                        - The American Cancer Society)
        '''.format(donor.name, donor.last_donation)
                     )

# ----------------------------------------------------------------------------
#
# Save letters to disk
#
# ----------------------------------------------------------------------------

    def save_letters_to_disk(self):
        for donor in self.donor_data.values():
            print("creating letter to:", donor.name)
            letter = self.write_letter(donor)
            filename = donor.name.replace(" ", "_") + ".txt"
            open(filename, 'w').write(letter)



# def object_oriented_db():
#     db = DonorData()
#     raw_data = find_donor_db()

#     for k, v in raw_data.items():
#         print(k,v)
#         donor = Donor(k)
#         for donation in v[1]:
#             donor.add_donation(donation)
#     return db


"""
The following section of the code pertaions to the operational side of the
"""

# ----------------------------------------------------------------------------
#
# Mainloop
#
# ----------------------------------------------------------------------------

testdb = DonorData(find_donor_db())


def mainloop():

    mainmenuinput = input(dedent("""
        What would you like to do?

        (1) - Send a Thank You Letter
        (2) - Build a Report
        (3) - Send letters to all donors
        (4) - Quit

        > """))
    return mainmenuinput.strip()


# def accept_donation(self, name):
#     while True:
#         donation_msg = input("Enter your desired donation amount"
#                              " or 'menu' to exit)>").strip()
#         if donation_msg == "menu":
#             return
#         else:
#             donation_amt = float(donation_msg)
#             break

#     donor = self.search_donor_db(name)
#     if donor is None:
#         donor = testdb.add_new_donor(name)

#         donor[1].append(donation_amt)

#         print(thank_you_message())


def thank_you_message():
    while True:
        name = input("Enter the donor's name or a list of donor's"
                     "names to see all donors (or type 'menu'"
                     "to exit)>").strip()
        if name == 'list':
            print(testdb.list_donors())
        elif name == 'menu':
            return
        else:
            break

# creates loop for donation amount input

    while True:
        donationinput = input("Enter the amount donated "
                              "(or 'menu' to exit)>").strip()
        if donationinput == 'menu':
            return

        try:
            amount = float(donationinput)
            if math.isnan(amount):
                raise ValueError
        except ValueError:
            print("please enter a valide donation amount")
        else:
            break

    donor = testdb.search_donor_db(name)
    if donor is None:
        donor = testdb.add_donor(name)

        donor.add_donation(amount)

        print(testdb.write_letter(donor))
# ----------------------------------------------------------------------------
#
# Prints the donor report
#
# ----------------------------------------------------------------------------


def print_donor_report():
    print(testdb.donor_report())


# ----------------------------------------------------------------------------
#
# quits the program when prompted in the menu
#
# ----------------------------------------------------------------------------


def quit():
    sys.exit()

# ----------------------------------------------------------------------------
#
# Creates the main function for the Mailroom2.py exercise
#
# ----------------------------------------------------------------------------


def runmain():
    mainlist_dict = {"1": thank_you_message,
                     "2": print_donor_report,
                     "3": testdb.save_letters_to_disk,
                     "4": quit}

    while True:
        action = mainloop()
        try:
            mainlist_dict[action]()
        except KeyError:
            print("error: menu selection is invalid!")


if __name__ == "__main__":
    runmain()
