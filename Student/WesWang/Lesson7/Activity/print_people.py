'''
Wesley Wang
Activity 7
Print all employees
'''

import sqlite3

try:
    conn = sqlite3.connect('personjob.db')
    c = conn.cursor()
    c.execute('PRAGMA foreign_keys = ON;')
except Error as e:
    print(e)

def print_people():
    query = c.execute('SELECT p.person_name, j.job_name, d.dpt_name \
                        FROM person AS p \
                            INNER JOIN job AS j \
                                ON p.person_id = j.person_employed_id \
                            INNER JOIN department AS d \
                                ON j.dpt_number_id = d.dpt_number')
    for person in query:
        print(person[0] + " was a " + person[1] + " at " + person[2] + " department.")

if __name__ == "__main__":
    print_people()
    conn.close()