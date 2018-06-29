
from personjob_modeli import *
import logging
from datetime import datetime


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info('Working with People class')
PERSON_NAME = 0
LIVES_IN_TOWN = 1
NICKNAME = 2

people = [
    ('Andrew', 'Sumner', 'Andy'),
    ('Peter', 'Seattle', None),
    ('Susan', 'Boston', 'Beannie'),
    ('Pam', 'Coventry', 'PJ'),
    ('Steven', 'Colchester', None),
    ]

logger.info('Creating Person records: iterate through the list of tuples')
logger.info('Prepare to explain any errors with exceptions')
logger.info('and the transaction tells the database to rollback on error')

for person in people:
    try:
        with database.transaction():
            new_person = Person.create(
                    person_name = person[PERSON_NAME],
                    lives_in_town = person[LIVES_IN_TOWN],
                    nickname = person[NICKNAME])
            new_person.save()
            logger.info('Database add successful')

    except Exception as e:
        logger.info(f'Error creating = {person[PERSON_NAME]}')
        logger.info(e)


logger.info('Read and print all Person records we created...')

for person in Person:
    logger.info(f'{person.person_name} lives in {person.lives_in_town} ' +\
        f'and likes to be known as {person.nickname}')


logger.info('Working with Job class')

logger.info('Creating Job records: just like Person. We use the foreign key')

JOB_NAME = 0
START_DATE = 1
END_DATE = 2
SALARY = 3
PERSON_EMPLOYED = 4

jobs = [
    ('Analyst', '2001-09-22', '2003-01-30',65500, 'Andrew'),
    ('Senior analyst', '2003-02-01', '2006-10-22', 70000, 'Andrew'),
    ('Senior business analyst', '2006-10-23', '2016-12-24', 80000, 'Andrew'),
    ('Admin supervisor', '2012-10-01', '2014-11-10', 45900, 'Peter'),
    ('Admin manager', '2014-11-14', '2018-01-05', 45900, 'Peter')
    ]


for job in jobs:
    try:
        # compute the job duration in number of days
        date_format = '%Y%m%d'
        a = job[START_DATE].replace('-', '')
        b = job[END_DATE].replace('-', '')
        d0 = datetime.strptime(a, date_format)
        d1 = datetime.strptime(b, date_format)
        JD = (d1 - d0).days
        logger.info(JD)
        #save data to Job Table
        with database.transaction():
            new_job = Job.create(
                job_name = job[JOB_NAME],
                start_date = job[START_DATE],
                end_date = job[END_DATE],
                salary = job[SALARY],
                job_duration = JD,
                person_employed = job[PERSON_EMPLOYED])
            new_job.save()

    except Exception as e:
        logger.info(f'Error creating = {job[JOB_NAME]}')
        logger.info(e)

logger.info('Reading and print all Job rows (note the value of person)...')

for job in Job:
    logger.info(f'{job.job_name} : {job.start_date} to {job.end_date} for {job.job_duration} days for {job.person_employed}')

logger.info('Working with Department class')

logger.info('Creating Department records: just like Job. We use the foreign key')

DEPARTMENT_NUMBER = 0
DEPARTMENT_NAME = 1
MANAGER = 2
JOB_INCLUDED = 3

departments = [
    ('RD01', 'Research', 'Peter', 'Analyst'),
    ('RD02', 'Research', 'Bill', 'Senior analyst'),
    ('RD03', 'Research', 'Anna', 'Senior business analyst'),
    ('HR01', 'Human Resource Management', 'Sam', 'Admin supervisor'),
    ('HR02', 'Human Resource Management', 'Jessica', 'Admin manager')
    ]

for department in departments:
    try:
        with database.transaction():
            new_department = Department.create(
                department_number = department[DEPARTMENT_NUMBER],
                department_name = department[DEPARTMENT_NAME],
                manager = department[MANAGER],
                job_included = department[JOB_INCLUDED])
            new_department.save()

    except Exception as e:
        logger.info(f'Error creating = {department[DEPARTMENT_NAME]}')
        logger.info(e)

logger.info('Reading and print all Department rows')

for department in Department:
    logger.info(f'{department.department_number} : '
     f'{department.department_name} manager is {department.manager} has '
     f'{department.job_included}')

query = (Person
         .select(Person, Job)
         .join(Job)
         .order_by(Person)
         .prefetch(Job, Department)
        )


for person in query:
    logger.info(f'Person {person.person_name} had job {person.job.job_name} for {person.job.job_duration} days')
    for department in person.job.was_in:
        logger.info(f"  in {department.department_number}")

database.close()
