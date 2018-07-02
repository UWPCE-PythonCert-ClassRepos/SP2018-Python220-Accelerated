'''
Insert testing records to db
'''

import sqlite3

try:
    conn = sqlite3.connect('mailroom.db')
    c = conn.cursor()
    c.execute('PRAGMA foreign_keys = ON;')
except Error as e:
    print(e)

donor1 = {"Name": "Jeff Bezos", "Donations": [2000,5000,3000]}
donor2 = {"Name": "Bill Gates", "Donations": [1000,4000]}
donor3 = {"Name": "Donald Trump", "Donations": [3000]}

donors = [donor1, donor2, donor3]

for donor in donors:
    c.execute('INSERT INTO donor VALUES(NULL, ?, NULL)', (donor["Name"], ))
    donor_id = c.lastrowid
    for donation in donor["Donations"]:
        c.execute('INSERT INTO donation VALUES(NULL, ?, ?)', (donation, donor_id))
    conn.commit()

conn.close()