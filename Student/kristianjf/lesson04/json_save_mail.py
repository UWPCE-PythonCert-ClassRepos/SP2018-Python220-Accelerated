#!/usr/bin/env python3

'''Using metaclass json.save decorator to add ability to save and load json with ease'''
import json
import json_save.json_save.json_save.json_save_dec as js
from mailroom_6 import *

@js.json_save
class JsonDh:
    '''Create class that uses js.json_save metaclass decorator'''
    Donors = js.List()
    def __init__(self, dh):

        self.Donors = [{'name': donor_object.name, 'donations': donor_object.donations} \
        for donor_object in dh.donors.values()]
    def save(self):
        '''Use js method to export attributes to json'''
        with open('json_out.json', 'w') as c_outfile:
            self.to_json(fp=c_outfile)
    @classmethod
    def load(cls, file='json_in.json'):
        '''Use js method to initialize class using json file import'''
        with open(file, 'r') as c_infile:
            return js.from_json(c_infile)

if __name__ == '__main__':
    # Create instance of json donor handler with populated data structure.
    TEST_JSON_DH = JsonDh(dh=PopulateDB())
    # Save JSON export to a file
    TEST_JSON_DH.save()
    with open('json_out.json') as outfile:
        print(f'\nFile Saved\nResults: {json.load(outfile)}\n')
    # Create a new file named json_in.json and add a new donor.
    with open('json_out.json', 'r') as infile:
        PYTHON_IN = json.load(infile)
        PYTHON_IN['Donors'].append({'name':'Kristian Francisco', 'donations': [20000]})
        with open('json_in.json', 'w') as outfile:
            outfile.write(json.dumps(PYTHON_IN, indent=4, separators=(',', ': ')))
        print(f'Added Donor: {PYTHON_IN["Donors"][-1]}\nResults: {PYTHON_IN}\n')
    # Load the new json_in.json file using classmethod load
    TEST_LOAD_JSON_DH = JsonDh.load(file='json_in.json')
    print(f'File Loaded\nResults: {vars(TEST_LOAD_JSON_DH)}\n')
