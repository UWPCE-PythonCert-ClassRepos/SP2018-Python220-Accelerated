
from mailroom_oo import *
import json_save.json_save.json_save.json_save_dec as js
import os


##############################################################################
#                                                                            #
#  https://docs.python.org/3/library/json.html:                              #
#  ________________________________________________________________________  #
#                                                                            #
#  json.load(,fp, *, cls=None, object_hook=None, parse_float=None,           #
#  parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)        #
#                                                                            #
#  serialize obj as a JSON formatted stream to fp (a .write()-supporting     #
#  file-like object) using this conversion table. The json module always     #
#  produces str objects, not bytes objects. Therefore, fp.write() must       #
#  support str input.                                                        #
#                                                                            #
#
#  ________________________________________________________________________  #
#                                                                            #
#  writing file from json out:                                               #
#  ________________________________________________________________________  #
#                                                                            #
#  https://stackoverflow.com/questions/12309269/                             #
#  how-do-i-write-json-data-to-a-file                                        #
#                                                                            #
#   with open('data.txt', 'w') as outfile:                                   #
#   json.dump(jsonData, outfile, sort_keys = True, indent = 4,               #
#              ensure_ascii = False)                                         #
#                                                                            #
##############################################################################


@js.json_save
class save_donor_db:
    Donors = js.List()  # uses list function from json_save_dec

    def __init__(self, donordb):
        self.Donors = [{'name': donor.name, 'donations': donor.donations}
                       for donor in donors.values()]  # packs db into a list

    def save(self):  # Should save as an outfile
        with open('json._mr.txt', 'w') as outfile:
            self.dump(self.donors, fp=outfile)

    @classmethod  # Should load in file
    def load(cls, file='json_in.json'):
        with open(file, 'r') as infile:
            return js.from_json(infile)
