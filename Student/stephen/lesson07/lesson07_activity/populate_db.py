"""
Module for populating the personjob database
"""

from personjob_model import *

import logging

def populate_person():
    """
    add person data to database
    """

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('personjob.db')

    logger.info('Working with Person class')
    logger.info('Note how I use constants and a list of tuples as a simple schema')
    logger.info('Normally you probably will have prompted for this from a user')

    PERSON_NAME = 0
    LIVES_IN_TOWN = 1
    NICKNAME = 2

    people = [
        ('Andrew', 'Sumner', 'Andy'), #1
        ('Peter', 'Seattle', None), #2
        ('Susan', 'Boston', 'Beannie'), #3
        ('Pam', 'Coventry', 'PJ'), #4
        ('Steven', 'Colchester', None), #5
        ]

    logger.info('Creating Person records: iterate through the list of tuples')
    logger.info('Prepare to explain any errors with exceptions')
    logger.info('and the transaction tells the database to fail on error')

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        for person in people:
            with database.transaction():
                new_person = Person.create(
                        person_name = person[PERSON_NAME],
                        lives_in_town = person[LIVES_IN_TOWN],
                        nickname = person[NICKNAME])
                new_person.save()
                logger.info('Database add successful')

        logger.info('Print the Person records we saved...')
        for saved_person in Person:
            logger.info(f'{saved_person.person_name} lives in {saved_person.lives_in_town} ' +\
                f'and likes to be known as {saved_person.nickname}')

    except Exception as e:
        logger.info(f'Error creating = {person[PERSON_NAME]}')
        logger.info(e)
        logger.info('See how the database protects our data')

    finally:
        logger.info('database closes')
        database.close()

def populate_department():
    """
    add person data to database
    """

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('personjob.db')

    logger.info('Working with Department class')
    logger.info('Note how I use constants and a list of tuples as a simple schema')
    logger.info('Normally you probably will have prompted for this from a user')

    DEPT_CODE = 0
    DEPT_NAME = 1
    MANAGER = 2

    departments = [
        ('W301', 'Finance', 'Willy Wonka'), #1
        ('R501', 'Human Resources', 'Charlie Bucket' ), #2
        ('L200', 'Logistics', 'Augustus Gloop'), #3
        ('M729', 'Information Technology', 'Veruca Salt'), #4
        ('Y782', 'Business Development', 'Mike Teavee'), #5
        ]

    logger.info('Creating Department records: iterate through the list of tuples')
    logger.info('Prepare to explain any errors with exceptions')
    logger.info('and the transaction tells the database to fail on error')

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        for dept in departments:
            with database.transaction():
                new_dept = Department.create(
                        department_code = dept[DEPT_CODE],
                        department_name = dept[DEPT_NAME],
                        manager = dept[MANAGER])
                new_dept.save()
                logger.info('Database add successful')

        logger.info('Print the Person records we saved...')
        for saved_person in Person:
            logger.info(f'{saved_person.person_name} lives in {saved_person.lives_in_town} ' +\
                f'and likes to be known as {saved_person.nickname}')

    except Exception as e:
        logger.info(f'Error creating = {dept[DEPT_NAME]}')
        logger.info(e)
        logger.info('See how the database protects our data')

    finally:
        logger.info('database closes')
        database.close()

def populate_job():
    """
        add job data to database
    """

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('personjob.db')

    logger.info('Working with Job class')
    logger.info('Creating Job records: just like Person. We use the foreign key')

    JOB_NAME = 0
    START_DATE = 1
    END_DATE = 2
    SALARY = 3
    PERSON_ID = 4
    DEPT_ID = 5


    jobs = [
        ('Analyst', '2001-09-22', '2003-01-30',65500, 1, 3),
        ('Senior analyst', '2003-02-01', '2006-10-22', 70000, 1, 2),
        ('Senior business analyst', '2006-10-23', '2016-12-24', 80000, 1, 1),
        ('Admin supervisor', '2012-10-01', '2014-11-10', 45900, 2, 2),
        ('Admin manager', '2014-11-14', '2018-01-05', 45900, 5, 4)
        ]

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        for job in jobs:
            with database.transaction():
                new_job = Job.create(
                    job_name = job[JOB_NAME],
                    start_date = job[START_DATE],
                    end_date = job[END_DATE],
                    salary = job[SALARY],
                    person_id = job[PERSON_ID],
                    dept_id = job[DEPT_ID])
                new_job.save()

        logger.info('Reading and print all Job rows (note the value of person)...')
        for job in Job:
            logger.info(f'{job.job_name}: {job.start_date} to {job.end_date} for {job.person_id}')

    except Exception as e:
        logger.info(f'Error creating = {job[JOB_NAME]}')
        logger.info(e)

    finally:
        logger.info('database closes')
        database.close()

if __name__ == '__main__':
    populate_person()
    populate_department()
    populate_job()