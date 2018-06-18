#=========================================================================================
#Name: Mailroom with JSON
#Author: Wesley Wang
#Date: 6/17/2018
#=========================================================================================
import sys
from datetime import date
import json_save.json_save_meta as js

class Donor(js.JsonSaveable):

    _name = js.String()
    _donations = js.List()

    def __init__(self, name, donations = None):
        self._name = name
        if donations is None:
            self._donations = []
        else:
            self._donations = donations

    def __str__(self):
        return f"{self._name} donated ${sum(self._donations):,.2f}"

    def __repr__(self):
        return f"{self._name} donated ${sum(self._donations):,.2f}"
        
    @property
    def name(self):
        return self._name
    
    @property
    def donations(self):
        return self._donations

    @property
    def total(self):
        return sum(self._donations)
    
    @property
    def num_donation(self):
        return len(self._donations)

    @property
    def avg_donation(self):
        return sum(self._donations)/len(self._donations)

    def new_donation(self, donation):
        self._donations.append(donation)

    def __eq__(self, other):
        return sum(self._donations) == sum(other._donations)

    def __ne__(self, other):
        return not sum(self._donations) == sum(other._donations)

    def __lt__(self, other):
        return sum(self._donations) < sum(other._donations)

    def __gt__(self, other):
        return not sum(self._donations) < sum(other._donations)

    def __le__(self, other):
        return sum(self._donations) >= sum(other._donations)

    def __ge__(self, other):
        return not sum(self._donations) >= sum(other._donations)

class DonorDB(js.JsonSaveable):

    _donors = js.List()

    def __init__(self, donors=None):
        if donors is None:
            self._donors = []
        else:
            self._donors = donors

    @property
    def donors(self):
        return self._donors
    
    def add_donor(self, donor):
        self._donors.append(donor)

    def load(self):
        with open("C:\_Python220AC\SP2018-Python220-Accelerated\Student\WesWang\Lesson4\Assignment\Donor_DB.json", "r") as db_file:
            self._donors = js.from_json(db_file)._donors

    def save(self):
        with open("C:\_Python220AC\SP2018-Python220-Accelerated\Student\WesWang\Lesson4\Assignment\Donor_DB.json", "w") as db_file:
            db_file.write(self.to_json())

    def generate_donor_list(self):
        output = "-"*20 + "\nList of Donors:\n" + "-"*20
        for donor in sorted(self._donors, key=lambda donor:donor.name):
            output += "\n" + donor.name
        output += "\n" + "-"*20
        return output

    def build_report(self):
        donors = self._donors
        header = ["Donor Name","Total Given", "Num Gifts","Average Gifts"]
        report = ""
        report += "-"*75
        report += f"\n{header[0]:30}| {header[1]:15}| {header[2]:10}| {header[3]:20}\n"
        report += "-"*75
        for donor in sorted(self._donors, key=lambda donor:donor.total, reverse=True):
            report += f"\n{donor.name:30}${donor.total:>15,.2f}{donor.num_donation:>13}{donor.avg_donation:>15,.2f}"
        report += "\n" + "-"*75
        return report

def thank_letter(donor, amount):
    letter = "-"*80 + f"""\nDear {donor},\n\n\tWe have received you donation of ${amount:,.2f}.
        \n\n\tWe greatly appreciate your generous contribution.
        \n\n\tThis donation is meaningful and crucial to our organization's misson.
        \n\nSincerely,\n\nWesley Wang\n""" + "-"*80
    return letter

def thank_you():
    # Ask for user input
    response = input("Please enter donor's full name, or type 'list' to check all donors: ").title()
    if response.lower() == "list":
        print(db.generate_donor_list())
        thank_you()

    while True:
        try:
            amount = float(input("Please enter donation amount for " + response + ":"))
            break
        except:
            print("\nPlease enter a dollar amount!!\n")
            continue

    donors = db.donors
    for donor in donors:
        if response.lower() == donor.name.lower():
            donor.new_donation(amount)
            print(thank_letter(donor.name, amount))
            print("Return to main menu!!")
            mainloop()
    db.add_donor(Donor(response, [amount]))
    print(thank_letter(response, amount))


def report():
    print(db.build_report())


def send_letters():
    file_path = "C:\_Python220AC\SP2018-Python220-Accelerated\Student\WesWang\Lesson4\Assignment\\"
    donors = db.donors
    for donor in donors:
        letters = open(file_path + donor.name.replace(" ", "_") + "_Donation_Letter_" + str(date.today()) + ".txt", "w")
        letters.write(thank_letter(donor.name, donor.donations[-1]))
        letters.close()
    print("\nLetters to all donors' previous donations printed !!\n")

def update():
    db.save()
    print("\nDonor database has been updated!!!\n")

def quit():
    print("You have successfully quit Mailroom")
    sys.exit()

menu = {"1":["Send a Thank you", thank_you]
    , "2":["Create a Report", report]
    , "3":["Send Letters to Everyone", send_letters]
    , "4":["Update Donor Database", update]
    , "5":["Quit", quit]}


def mainloop():
    print("\nWelcome to the Mailroom\n")

    while True:
        for key, value in menu.items():
            print("[" + key + "] "+ value[0])
        response = input("What do you want to do?\t")
        print(response, " was chosen")

        if response not in menu:
            print("Not a Valid Response --- Type 1, 2, 3, 4, or 5")
        else:
            menu[response][1]()


if __name__ == "__main__":
    db = DonorDB()
    db.load()
    mainloop()