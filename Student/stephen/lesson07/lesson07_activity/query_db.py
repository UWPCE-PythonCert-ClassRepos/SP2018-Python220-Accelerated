"""
Module for querying exercise from lesson 7 activity:
We also need to know the duration in days that the job was held.
Produce a list using pretty print that shows all of the departments a person worked in for every job they ever had. 
"""

from personjob_model import *

import logging
import pprint as pp
from datetime import date


def join_classes():
    """
        demonstrate how to join classes together : no matches too
    """

    logging.basicConfig(level=logging.CRITICAL)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('personjob.db')

    logger.info("View records of people's jobs, how many days they had them and the department they were in")

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        logger.info("Querying the database")
        query = (Job
                 .select(Person.person_name.alias('Name'), Job.job_name.alias('Job Title'), Department.department_name.alias('Department'), Job.days_on_job.alias('Days'))
                 .join(Person, JOIN.INNER)
                 .switch(Job)
                 .join(Department, JOIN.INNER)
                 .dicts() # used this feature to setup the output for pretty print
                )
        
        for person in query:
            try:
                pp.pprint(person)

            except Exception as e:
                logger.info(e)

    except Exception as e:
        logger.info(e)

    finally:
        database.close()

if __name__ == '__main__':
    join_classes()
