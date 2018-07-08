'''
Wesley Wang
Activity 7
Insert data into personjob database
'''

import sqlite3
import logging
import logging.handlers

try:
    conn = sqlite3.connect('personjob.db')
    c = conn.cursor()
    c.execute('PRAGMA foreign_keys = ON;')
except Error as e:
    print(e)

format = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"
formatter = logging.Formatter(format)
console_handler = logging.StreamHandler()        
console_handler.setLevel(logging.DEBUG)          
console_handler.setFormatter(formatter)  
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)                   
logger.addHandler(console_handler) 


def add_dpt():
    c.execute('INSERT INTO department VALUES ("F001", "Finance", "Finance Manager")')
    c.execute('INSERT INTO department VALUES ("M001", "Marketing","Marketing Manager")')
    c.execute('INSERT INTO department VALUES ("R001", "Research", "Research Manager")')
    conn.commit()
    logging.info("New departments created!")

def add_ppl():
    c.execute('INSERT INTO person VALUES (1, "Alpha Male", "Seattle", NULL)')
    c.execute('INSERT INTO person VALUES (2, "Beta Male", "Seattle", NULL)')
    c.execute('INSERT INTO person VALUES (3, "Omega Male", "Bothell", NULL)')
    conn.commit()
    logging.info("New people added!")

def add_job():
    c.execute('INSERT INTO job VALUES (NULL, "Data Analyst", "2016-05-01", "2018-05-25", 50000.00, 1,"F001")')
    c.execute('INSERT INTO job VALUES (NULL, "Manager", "2010-02-01", "2018-07-05", 75000.00, 2, "M001")')
    c.execute('INSERT INTO job VALUES (NULL, "Data Analyst", "2016-05-01", "2017-08-31", 45000.00, 3, "R001")')
    conn.commit()
    logging.info("New Jobs added!")

if __name__ == "__main__":
    add_dpt()
    add_ppl()
    add_job()
    conn.close()