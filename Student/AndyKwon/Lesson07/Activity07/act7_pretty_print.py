# Pretty print the database 
# currently unable to populate the db but this is how I think I would pprint

from peewee import *
from act7_personjob_model import Person, Job, Department
from pprint import pprint


def pretty_print():
    # acccess the data base

    database = SqliteDatabase('act7_personjob.db')
    database.connect()
    database.execute_sql('PRAGMA foreign_keys = ON;')

    # create query 
    query = (Person.select(Person, Job, Department).join(Job, JOIN.INNER).join(Department, JOIN.INNER))

    # loop through the query and pprint 
    for line in query:
        pprint(f'{item.person} had this job {line.job.job_name} in {line.job.department.department_name} department.')

    # close the database
    database.close()

pretty_print()