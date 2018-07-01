"""
    Simple database examle with Peewee ORM, sqlite and Python
    Here we define the schema

"""

import logging
from datetime import date
from peewee import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

database = SqliteDatabase('personjob.db')
database.connect()
database.execute_sql('PRAGMA foreign_keys = ON;')

class BaseModel(Model):
    class Meta:
        database = database

class Person(BaseModel):
    """
        This class defines Person, which maintains details of someone
        for whom we want to research career to date.
    """
    person_name = CharField(primary_key=True, max_length=30)
    lives_in_town = CharField(max_length=40)
    nickname = CharField(max_length=20, null=True)

class Job(BaseModel):
    """
        This class defines Job, which maintains details of past Jobs
        held by a Person.
    """
    job_name = CharField(primary_key=True, max_length=30)
    start_date = DateField(formats='YYYY-MM-DD')
    end_date = DateField(formats='YYYY-MM-DD')
    salary = DecimalField(max_digits=7, decimal_places=2)
    person_employed = ForeignKeyField(Person, related_name='was_filled_by', null=False)

# class PersonNumKey(BaseModel):
#     """
#         This class defines Person, which maintains details of someone
#         for whom we want to research career to date.
#
#         *** I am implemented with a numeric PK that is generated by the system ***
#     """
#     person_name = CharField(max_length = 30)
#     lives_in_town = CharField(max_length = 40)
#     nickname = CharField(max_length = 20, null = True)

class Department(BaseModel):
    """
        This class defines Department, which maintains details of which Departments
        held by a Person.
    """
    dept_name = CharField(primary_key=True, max_length=4)
    dept_manager = ForeignKeyField(Person, related_name='mgr_was_filled_by', null=False)
    person_employed = ForeignKeyField(Person, related_name='prs_was_filled_by', null=False)
    job_held = ForeignKeyField(Job, related_name='job_filled', null=False)
    duration = IntegerField()

logger.info('Creating tables')
database.create_tables([
        Job,
        Person,
        Department
    ])
logger.info(f'Tables Created: {database.get_tables()}')

logger.info('Creating person')

def populate_person_db():
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
        ('Andrew', 'Sumner', 'Andy'),
        ('Peter', 'Seattle', None),
        ('Susan', 'Boston', 'Beannie'),
        ('Pam', 'Coventry', 'PJ'),
        ('Steven', 'Colchester', None),
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

def populate_job_db():
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
    PERSON_EMPLOYED = 4

    jobs = [
        ('Analyst', '2001-09-22', '2003-01-30',65500, 'Andrew'),
        ('Senior analyst', '2003-02-01', '2006-10-22', 70000, 'Andrew'),
        ('Senior business analyst', '2006-10-23', '2016-12-24', 80000, 'Andrew'),
        ('Admin supervisor', '2012-10-01', '2014-11,10', 45900, 'Peter'),
        ('Admin manager', '2014-11-14', '2018-01,05', 45900, 'Peter')
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
                    person_employed = job[PERSON_EMPLOYED])
                new_job.save()

        logger.info('Reading and print all Job rows (note the value of person)...')
        for job in Job:
            logger.info(f'{job.job_name} : {job.start_date} to {job.end_date} for {job.person_employed}')

    except Exception as e:
        logger.info(f'Error creating = {job[JOB_NAME]}')
        logger.info(e)

    finally:
        logger.info('database closes')
        database.close()

def populate_dept_db():
    """
        add dept data to database
    """

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('personjob.db')

    logger.info('Working with Department class')
    logger.info('Creating Department records: just like Person. We use the foreign key')

    DEPT_NAME = 0
    DEPT_MANAGER = 1
    PERSON_EMPLOYED = 2
    JOB_HELD = 3

    departments = [
        ('AAAA', 'Peter', 'Andrew', 'Analyst'),
        ('BBBB', 'Peter', 'Andrew', 'Senior analyst'),
        ('CCCC', 'Peter', 'Andrew', 'Senior business analyst')
        ]

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        for department in departments:
            query = Job.select().where(
                Job.person_employed == department[PERSON_EMPLOYED] and
                Job.job_name == department[JOB_HELD])
            start_date = [(x.start_date.split('-')) for x in query][0]
            end_date = [x.end_date.split('-') for x in query][0]
            start_date_obj = date(int(start_date[0]), int(start_date[1]), int(start_date[2]))
            end_date_obj = date(int(end_date[0]), int(end_date[1]), int(end_date[2]))

            with database.transaction():
                new_department = Department.create(
                    dept_name=department[DEPT_NAME],
                    dept_manager=department[DEPT_MANAGER],
                    person_employed=department[PERSON_EMPLOYED],
                    job_held=department[JOB_HELD],
                    duration=(end_date_obj - start_date_obj).days)
                new_department.save()

        logger.info('Reading and print all Department rows (note the value of person)...')
        for department in Department:
            logger.info(f'Department {department.dept_name} : Department Manager {department.dept_manager} manage {department.person_employed} in position {department.job_held} for {department.duration} days')

    except Exception as e:
        logger.info(f'Error creating = {department[DEPT_NAME]}')
        logger.info(e)

    finally:
        logger.info('database closes')
        database.close()

def drop_persondb_tables():
    database.drop_tables(Department)
    database.drop_tables(Job)
    database.drop_tables(Person)

if __name__ == '__main__':
    populate_person_db()
    populate_job_db()
    populate_dept_db()
