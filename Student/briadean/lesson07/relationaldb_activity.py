#!/usr/bin/env python3
"""
Learning persistence with Peewee and sqlite
"""

import logging
import pprint
from lesson07.personjob_model_modified import *
from datetime import datetime


def populate_db():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    db = SqliteDatabase('personjob.db')

    """
    Add person data to the database
    """

    logger.info('Working with the Person class')

    PERSON_NAME = 0
    LIVES_IN_TOWN = 1
    NICKNAME = 2

    people = [('Andrew', 'Sumner', 'Andy'),
              ('Peter', 'Seattle', None),
              ('Susan', 'Boston', 'Beannie'),
              ('Pam', 'Coventry', 'PJ'),
              ('Steven', 'Colchester', None)]

    logger.info('Creating Person records')

    try:
        db.connect()
        db.execute_sql('PRAGMA foreign_keys = ON;')
        for person in people:
            with db.transaction():
                new_person = Person.create(
                     person_name=person[PERSON_NAME],
                     lives_in_town=person[LIVES_IN_TOWN],
                     nickname=person[NICKNAME])
                new_person.save()
                logger.info('Database add successful')

        logger.info('The following person records have been saved:')
        for saved_person in Person:
                logger.info(f'{saved_person.person_name} lives in {saved_person.lives_in_town} '
                            f'and likes to be known as {saved_person.nickname}')

    except Exception as y:
        logger.info(f'Error creating = {person[PERSON_NAME]}')
        logger.info(y)

    """
    Add department data to the database
    """

    logger.info('Working with the Department class')

    DEPARTMENT_ID = 0
    DEPARTMENT_NAME = 1
    DEPARTMENT_MANAGER = 2

    departments = [('G435', 'Engineering', 'Mr Boops'),
                   ('B429', 'Business Administration', 'Mr Bits'),
                   ('H443', 'Human Resources', 'Mrs Bobs')]

    logger.info('Creating Department records')

    try:
        for department in departments:
            with db.transaction():
                new_department = Department.create(dept_id=department[DEPARTMENT_ID],
                                                   dept_name=department[DEPARTMENT_NAME],
                                                   dept_manager=department[DEPARTMENT_MANAGER])
                new_department.save()
                logger.info('Database add successful')

        logger.info('The following department records have been saved:')
        for saved_department in Department:
            logger.info(f'{saved_department.dept_id} or the {saved_department.dept_name} department '
                        f'is managed by {saved_department.dept_manager}')

    except Exception as y:
        logger.info(f'Error creating = {department[DEPARTMENT_NAME]}')
        logger.info(y)

    """
    Add job data to the database
    """

    logger.info('Working with the Job class')
    logger.info('Creating Job records')

    JOB_NAME = 0
    START_DATE = 1
    END_DATE = 2
    SALARY = 3
    PERSON_EMPLOYED = 4
    DEPT_ID = 5

    jobs = [('Analyst', '2001-09-22', '2003-01-30', 65500, 'Andrew', 'G435'),
            ('Senior analyst', '2003-02-01', '2006-10-22', 70000, 'Andrew', 'G435'),
            ('Senior business analyst', '2006-10-23', '2016-12-24', 80000, 'Andrew', 'B429'),
            ('Admin supervisor', '2012-10-01', '2014-11-10', 45900, 'Peter', 'H443'),
            ('Admin manager', '2014-11-14', '2018-01-05', 45900, 'Peter', 'H443')]

    try:
        for job in jobs:
            # compute jobs duration as days
            date_format = '%Y%m%d'
            x = job[START_DATE].replace('-', '')
            y = job[END_DATE].replace('-', '')
            start = datetime.strptime(x, date_format)
            end = datetime.strptime(y, date_format)
            duration = (end - start).days

            with db.transaction():
                new_job = Job.create(
                     job_name=job[JOB_NAME],
                     start_date=job[START_DATE],
                     end_date=job[END_DATE],
                     salary=job[SALARY],
                     person_employed=job[PERSON_EMPLOYED],
                     dept_id=job[DEPT_ID],
                     job_duration=duration)
                new_job.save()

        logger.info('The following job records have been saved:')

        for saved_job in Job:
            logger.info(f'{saved_job.person_employed} held a {saved_job.job_name} position from {saved_job.start_date} '
                        f'to {saved_job.end_date} which was {saved_job.job_duration} total days.')

    except Exception as y:
        logger.info(f'Error creating = {job[JOB_NAME]}')
        logger.info(y)

    finally:
        logger.info('db closes')
        db.close()


def display_departments_per_job():
    query = (Person.select(Person, Job).join(Job, JOIN.INNER))
    # todo: figure out how to make this work with pretty print


if __name__ == '__main__':
    populate_db()
    display_departments_per_job()
