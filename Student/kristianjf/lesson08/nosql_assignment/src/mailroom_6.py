#!/usr/bin/env python3
import sys
import logging
import login_database
from datetime import datetime
from functools import reduce
'''
Goal:
You work in the mail room at a local charity. Part of your job is to write \
incredibly boring, repetitive emails thanking your donors for their generous \
gifts. You are tired of doing this over and over again, so you’ve decided to \
let Python help you out of a jam and do your work for you.
'''
'''
It should have a data structure that holds a list of your donors and a history of \
the amounts they have donated. This structure should be populated at first with at \
least five donors, with between 1 and 3 donations each.
'''

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info('Connecting to MongoDB')
database = login_database.login_mongodb_cloud()['dev_assignment']
logger.info(f'''Connected to {database.client} and
                created database {database.__dict__.get('_Database__name')}''')

class Donor():
    database = login_database.login_mongodb_cloud()['dev_assignment']
    donor_collection = database['donors']
    r_cache = login_database.login_redis_cloud()
    neo4j_driver = login_database.login_neo4j_cloud()
    def __init__(self, name, donations):
        self._name = name.title()
        self._donations = donations if isinstance(donations, list) else [donations]
        '''Add Donor Record to Table'''
        try:
            self.donor_collection.insert_one({'name': self._name, 'donations':self._donations})
            with self.neo4j_driver.session() as session:
                cyph = "CREATE (n:Donor {donor:'%s'})" % (
                    self._name)
                session.run(cyph)
                cyph = "CREATE (n:Donation {donation:'%s'})" % (
                    self._donations)
                session.run(cyph)
                cypher = """
                MATCH (n1:Donor {donor:'%s'})
                CREATE (n1)-[donations:DONATIONS]->(n2:Donation {donations:'%s'})
                """ % (self._name, self._donations)
                session.run(cypher)

        except Exception as e:
            logger.info(f'Error creating = {name, donations}')
            logger.info(e)
        else:
            donations = self.donations
            for donation in donations:
                self.r_cache.rpush(self._name, donation)
        finally:
            logger.info('database closes')
            database.client.close()

    def __lt__(self, other):
        return sum(self.donations) < sum(other.donations)
    @property
    def name(self):
        return self._name
    @property
    def donations(self):
        if self.r_cache.lindex(self.name, 0):
            return [int(donation) for donation in self.r_cache.lrange(self.name, 0, -1)]
        else:
            for donations in self.donor_collection.find({'name': self.name}):
                return donations['donations']
    @property
    def normalized_name(self):
        return self._name
    def donate(self, new_donation):
        try:
            donations = self.donations
            donations = self.donations.append(new_donation)
            self.donor_collection.update_one({'name': self.name},
                                             {'$set': {'donations': donations}})
        except Exception as e:
            logger.info(f'Error adding donation = {self.name, new_donation}')
            logger.info(e)
        else:
            self.r_cache.rpush(self._name, new_donation)

    def metrics(self):
        num_d = len(self.donations)
        total_d = sum(self.donations)
        avg_d = total_d / num_d
        return num_d, total_d, avg_d

    def send_letter(self):
        '''
        Try to use a dict and the .format() method to do the letter as one big \
        template rather than building up a big string in parts.
        In this version, add a function (and a menu item to invoke it), that goes \
        through all the donors in your donor data structure, generates a thank you \
        letter, and writes it to disk as a text file.
        '''
        filename = '_'.join(self.name.split())+'.txt'
        with open(filename, 'w') as outfile:
            outfile.write(self.output_string().format(name=self.name, donation=self.donations))
            print(f'Writing: {filename}')

    def output_string(self):
        'Output string for letters'
        format_string = 'Dear {name},\n\nThank you for your generous donation of ' \
                        '${donation}. Please send us more money at your earliest ' \
                        'convenience.'
        return format_string

class DonorHandler:
    def __init__(self):
        self.donors = {}
    def add_donor(self, donor_object):
        self.donors[donor_object.normalized_name] = donor_object
    def dnr_challenge(self, factor=1, **kwargs):
        new_dh = DonorHandler()
        for donor, donor_object in self.donors.items():
            '''Add a new feature to Mailroom using filter so that donations either above
            or below a specified dollar amount are included in the map operations of #1 above.
            You can do this by adding min_donation and max_donation optional keyword parameters
            to your challenge function. You’ll want to filter the donations before
            passing them to map.'''
            filter_donations = self.dnr_filter(\
            donor_object.donations, kwargs['min_donation'], kwargs['max_donation'])

            '''Add a new feature to Mailroom using map so that each donation on record can be
            doubled, tripled or indeed multiplied by any arbitrary factor based on the whims
            of philanthropists who would like to support our cause.
            This will require a new function (or method in your donor database class) called
            challenge(factor) that takes a multiplier (factor), and multiplies all the
            donations of all the donors by the factor. The function returns a NEW donor database,
            with the new data.'''
            map_donations_f = list(map(lambda x, y: x*y, filter_donations,\
            len(filter_donations)*[factor]))

            new_d = Donor(donor+' Projection', map_donations_f)
            new_dh.add_donor(new_d)
        return new_dh
    def dnr_filter(self, lst, min_donation=0, max_donation=10000000):
        lst = list(filter(lambda x: (x > min_donation) and (x < max_donation), lst))
        return lst

    def dnr_projections(self, donor, **kwargs):
        '''
        For instance, based on donations in the current database, show them (a) what their total
        contribution would come to in dollars if they were to double contributions under $100.
        And then (b) show them what their total contribution would come to if they were to
        triple contributions over $50.
        '''
        dnr_proj = self.dnr_challenge(**kwargs)
        return reduce(lambda x, y: x+y, dnr_proj.donors[donor].donations)

    def thank_you(self, full_name='', donation_amount=int(), **kwargs):
        '''
        If the user (you) selects ‘Send a Thank You’, prompt for a Full Name.
            If the user types a name not in the list, add that name to the data structure and use it.
            If the user types a name in the list, use it.
        Once a name has been selected, prompt for a donation amount.
            Turn the amount into a number – it is OK at this point for the program to crash if \
            someone types a bogus amount.
        Once an amount has been given, add that amount to the donation history of the selected user.
        Finally, use string formatting to compose an email thanking the donor for their generous \
        donation. Print the email to the terminal and return to the original prompt.
        '''
        '''
        Collect, Format and Validate Full name
        '''
        while not full_name:
            full_name_input = input('Please enter full name of the recipient: ').split()
            full_name = self.name_response_valid(full_name_input)
        '''
        Process Full Name
        '''
        ds_names = [name for name in self.donors]

        if full_name in ds_names:
            print(f'Found {full_name} in data_structure')
            while not donation_amount:
                donation_amount = int(input('Please enter a donation amount: '))
            self.donors[full_name].donate(donation_amount)
            print(self.donors[full_name].output_string().format(name=full_name, \
            donation=donation_amount))
        else:
            while not donation_amount:
                donation_amount = int(input('Please enter a donation amount: '))
            self.add_donor(Donor(full_name, donation_amount))
            print(self.donors[full_name].output_string().format(name=full_name, \
            donation=donation_amount))
        return self.donors[full_name].output_string().format(name=full_name, \
        donation=donation_amount)

    def list_donors(self, **kwargs):
        '''
        If the user types ‘list’, show them a list of the donor names and re-prompt
        '''
        for name in self.donors:
            print(name)
        return [name for name in self.donors]

    def create_a_report(self, **kwargs):
        '''
        Creating a Report
        If the user (you) selected “Create a Report”, print a list of your donors, \
        sorted by total historical donation amount.
        '''
        print('Menu: Create a Report')
        top_row = ('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')
        format_header = '{:<30} | {:<15} | {:<10} | {:<15}\n'
        format_data = '{:<30} $ {:<15.2f}   {:<10} $ {:<15.2f}\n'
        format_string = format_header.format(*top_row)
        for donor in sorted(self.donors.values(), reverse=True):
            name = donor.name
            num_gifts, total_given, avg_gift = donor.metrics()
            format_string += format_data.format(name, total_given, num_gifts, avg_gift)
        print(format_string)
        return format_string

    def send_letters(self, **kwargs):
        '''
        Try to use a dict and the .format() method to do the letter as one big \
        template rather than building up a big string in parts.
        In this version, add a function (and a menu item to invoke it), that goes \
        through all the donors in your donor data structure, generates a thank you \
        letter, and writes it to disk as a text file.
        '''
        for donor in self.donors.values():
            donor.send_letter()

    def run_projection(self, full_name='', max_donation_amount=int(), factor=int(), **kwargs):
        'Select from list of Donors to Run Projections'
        # donor_list_dict = {full_name: self.dnr_projections for donor in self.donors}
        donor_list_dict = {donor: kwargs.update({'full_name': donor}) for donor in self.donors}
        menu(donor_list_dict)
        'Collect Donor Name, Max Donation Amount, Factor'
        while not max_donation_amount:
            max_donation_amount = int(input('Please enter a max donation amount: '))
        while not factor:
            factor = int(input('Please enter a factor: '))
        donation_amount = self.dnr_projections(donor=full_name, min_donation=1, \
        max_donation=max_donation_amount, factor=factor, **kwargs)
        print(self.donors[full_name].output_string().format(name=full_name, \
        donation=donation_amount))
        return self.donors[full_name].output_string().format(name=full_name, \
        donation=donation_amount)

    #Name Validation
    def name_response_valid(self, full_name):
        'Validate and Return Name Input'
        full_name_cap = ''
        try:
            for name in full_name:
                assert name.isalpha()
                full_name_cap += f'{name.capitalize()} '
            full_name = full_name_cap.strip()
        except AssertionError:
            print('Invalid Name. Found non-alphabetic characters')
        else:
            return full_name

#Function to Process Menu Options
def menu(options_dict, **kwargs):
    '''
    The script should prompt the user (you) to choose from a menu of 3 actions: \
    “Send a Thank You”, “Create a Report” or “quit”)
    '''
    options = [option[0:2] for option in enumerate(options_dict.keys(), 1)]
    while True:
        print('Please select a number from the list of the following options: \n')
        for option in options:
            print(option)
        response = menu_response_valid(options)
        response_selection = options[response-1][1]
        options_dict[response_selection](**kwargs)

#Main Menu
def main_menu(**kwargs):
    'Create Main Menu'
    program_options_dict = {'Send a Thank You': thank_you_menu, \
                            'Create a Report': kwargs['donor_handler'].create_a_report, \
                            'Send Letters to Everyone': kwargs['donor_handler'].send_letters, \
                            'Run Donor Projections': kwargs['donor_handler'].run_projection, \
                            'quit': quit_menu}
    menu(program_options_dict, **kwargs)

#Thank You Menu
def thank_you_menu(**kwargs):
    '''
    Sending a Thank You
    If the user (you) selects ‘Send a Thank You’, prompt for a Full Name.
    If the user types ‘list’, show them a list of the donor names and re-prompt
    '''
    program_options_ty = {'Send a Thank You': kwargs['donor_handler'].thank_you, \
                        'Action: List': kwargs['donor_handler'].list_donors, \
                        'quit': main_menu}
    menu(program_options_ty, **kwargs)

def quit_menu(**kwargs):
    sys.exit()

#Menu Option Validation
def menu_response_valid(options):
    'Validate Menu Options'
    try:
        response = int(input())
        assert response in [option[0] for option in options]
    except ValueError:
        print('Non-integer value entered. Please try again.')
    except AssertionError:
        print('This number does not exist in the list of options. Please try again.')
    else:
        return response
    #Name Validation

def PopulateDB():
    'Create Donors'
    jb = Donor('Jeff Bezos', [1, 5, 10])
    bg = Donor('Bill Gates', [10000])
    sj = Donor('Steve Jobs', [20, 50, 100])
    'Create Donors Handle'
    dh = DonorHandler()
    dh.add_donor(jb)
    dh.add_donor(bg)
    dh.add_donor(sj)
    return dh

def main():
    dh = PopulateDB()
    'Call Main Menu'
    main_menu(donor_handler=dh)

if __name__ == '__main__':
    main()
