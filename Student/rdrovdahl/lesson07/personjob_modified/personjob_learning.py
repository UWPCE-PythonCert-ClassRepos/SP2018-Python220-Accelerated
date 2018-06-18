"""
    Learning persistence with Peewee and sqlite
    delete the database to start over
        (but running this program does not require it)
"""
import logging
from personjob_model import *
from datetime import datetime


def populate_db():
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
                        person_name=person[PERSON_NAME],
                        lives_in_town=person[LIVES_IN_TOWN],
                        nickname=person[NICKNAME])
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

    """
    add department data to database
    """

    logger.info('Working with Department class')

    DEPARTMENT_ID = 0
    DEPARTMENT_NAME = 1
    DEPARTMENT_MANAGER = 2

    departments = [
        ('E101', 'Engineering', 'Mr Sprocket'),
        ('T201', 'Information Technology', 'Mr Bits'),
        ('B402', 'Business Administration', 'Mrs Pots'),
        ('H504', 'Human Resources', 'Mrs Fields'),
        ]

    logger.info('Creating Department records: iterate through the list of tuples')
    logger.info('Prepare to explain any errors with exceptions')
    logger.info('and the transaction tells the database to fail on error')

    try:
        for department in departments:
            with database.transaction():
                new_department = Department.create(
                        dept_id=department[DEPARTMENT_ID],
                        dept_name=department[DEPARTMENT_NAME],
                        dept_manager=department[DEPARTMENT_MANAGER])
                new_department.save()
                logger.info('Database add successful')

        logger.info('Print the Department records we saved...')
        for saved_department in Department:
            logger.info(f'{saved_department.dept_id} is the ID for the {saved_department.dept_name} department ' +\
                f'and the department manager is {saved_department.dept_manager}')

    except Exception as e:
        logger.info(f'Error creating = {department[DEPARTMENT_NAME]}')
        logger.info(e)
        logger.info('See how the database protects our data')

    """
    add job data to database
    """

    logger.info('Working with Job class')
    logger.info('Creating Job records: just like Person. We use the foreign key')

    JOB_NAME = 0
    START_DATE = 1
    END_DATE = 2
    SALARY = 3
    PERSON_EMPLOYED = 4
    DEPT_ID = 5

    jobs = [
        ('Analyst', '2001-09-22', '2003-01-30', 65500, 'Andrew', 'T201'),
        ('Senior analyst', '2003-02-01', '2006-10-22', 70000, 'Andrew', 'B402'),
        ('Senior business analyst', '2006-10-23', '2016-12-24', 80000, 'Andrew', 'B402'),
        ('Admin supervisor', '2012-10-01', '2014-11-10', 45900, 'Peter', 'H504'),
        ('Admin manager', '2014-11-14', '2018-01-05', 45900, 'Peter', 'H504')
        ]

    try:
        for job in jobs:
            # compute the job duration in number of days
            date_format = '%Y%m%d'
            a = job[START_DATE].replace('-', '')
            b = job[END_DATE].replace('-', '')
            d0 = datetime.strptime(a, date_format)
            d1 = datetime.strptime(b, date_format)
            JD = (d1 - d0).days

            with database.transaction():
                new_job = Job.create(
                    job_name=job[JOB_NAME],
                    start_date=job[START_DATE],
                    end_date=job[END_DATE],
                    salary=job[SALARY],
                    person_employed=job[PERSON_EMPLOYED],
                    dept_id=job[DEPT_ID],
                    job_duration=JD)
                new_job.save()

        logger.info('Reading and print all Job rows (note the value of person)...')
        for job in Job:
            logger.info(f'{job.job_name} : {job.start_date} to {job.end_date} ({job.job_duration} days) for {job.person_employed}')

    except Exception as e:
        logger.info(f'Error creating = {job[JOB_NAME]}')
        logger.info(e)

    finally:
        logger.info('database closes')
        database.close()


def print_departments():
    '''
        print out a list of departments a person worked for considering every
        job they ever held
    '''
    logger = logging.getLogger(__name__)
    mydict = {}
    # query for all persons who have held jobs
    query = (Person
             .select(Person, Job)
             .join(Job, JOIN.INNER)
             )
    for person in query:
        logger.info(f'Person {person.person_name} had job {person.job.job_name} with department ID {person.job.dept_id}')
        dept = Department.get(Department.dept_id == person.job.dept_id)
        logger.info(f'   department name is {dept.dept_name}')
        try:
            mydict[person.person_name].insert(0, dept.dept_name)
        except KeyError:
            mydict[person.person_name] = [dept.dept_name]

    print('\n\nThe following is a list of persons and the departments they\'ve worked for:\n')
    for k, v in mydict.items():
        print('    ', k, set(v))
    print('\n')

if __name__ == '__main__':
    populate_db()
    print_departments()
