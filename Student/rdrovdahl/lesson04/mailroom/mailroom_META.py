#! /usr/local/bin/python3
'''
this code shows how to use metapgramming with a decorator
the json_save module will allow saving an object to a JSON file and the reading
of a JSON file to create an object

this is a snippet of the code used in the mailroom program developed in the
first class series
'''

import sys
sys.path.insert(0, './json_save')
import json_save.json_save_dec as js


donors_db_dict = {'Iron Man': ('Iron Man', ([100000, 50000, 1000], 'Hero', 'USA')),
                  'Thor': ('Thor', ([50, 25, 100], 'Hero', 'Earth')),
                  'Hulk': ('Hulk', ([500], 'Unaffiliated', 'Unknown')),
                  'Winter Soldier': ('Winter Soldier', ([360, 480], 'Villian', 'USSR')),
                  'Captain America': ('Captain America', ([30, 40], 'Hero', 'USA')),
                  'Nick Fury': ('Nick Fury', ([100000, 545, 1000], 'Retired', 'Unknown')),
                  'Hawkeye': ('Hawkeye', ([75, 50, 20], 'Hero', 'USA')),
                  'Ultron': ('Ultron', ([50000, 40000, 50000], 'Villian', 'DarkWeb')),
                  'Black Panther': ('Black Panther', ([100, 900, 50], 'Unaffiliated', 'Africa')),
                  'War Machine': ('War Machine', ([10, 10], 'Unaffiliated', 'USA')),
                  'Red Skull': ('Red Skull', ([1000, 2000, 3000], 'Villian', 'Europe'))
                  }


@js.json_save
class DonorDB():
    name = js.String()
    donations = js.List()
    status = js.String()
    location = js.String()

    def __init__(self, name=None, donations=None, status=None, location=None):
        self.name = name
        self.donations = [] if donations is None else donations
        self.status = status
        self.location = location


def write_object_to_file(my_object):
    with open("mail_db.json", 'w') as tempfile:  # Can change 'w' to 'a' but the from_json doesn't like the formatting
        tempfile.write(my_object.to_json())

def read_object_from_file(my_file):
    with open(my_file) as tempfile:
        reconstructed_donor = js.from_json(tempfile)
        assert reconstructed_donor.name == 'Red Skull'

if __name__ == '__main__':
    dd = {}
    for x in donors_db_dict.items():
        name = (x[1][0])
        # instantiate an object for every donor in the dictionary
        dd[name] = DonorDB(name, x[1][1][0], x[1][1][1], x[1][1][2])
        # now write the objects to a JSON file
        # found that the JSON file is readable by the from_json method with
        # only a single object entry in it
        # as a result, the file will be rewritten with every pass through this
        # loop and only contain the last entry
        write_object_to_file(dd[name])
    # show the dictionary of instances
    for k, v in dd.items():
        print(k, v)
    # now we can get specific instance details as follows:
    #    print(dd['Thor'].donations)
    #    print(dd['Thor'].status)
    # example of how to set attribute values
    #    dd['Black Panther'].donations = [100, 200, 100]
    # example of how to append donation values to existing list
    #    dd['Black Panther'].donations.append(555)

    # the following is a call to read a JSON file which has a single object
    # for a donor named 'Red Skull'
    read_object_from_file('mail_db2.json')
