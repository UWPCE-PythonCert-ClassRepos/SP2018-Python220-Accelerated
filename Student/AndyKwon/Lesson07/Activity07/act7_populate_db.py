import logging
from peewee import *
from datetime import datetime
from act7_personjob_model import Person, Job, Department

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def populate_person():
    """
    add person data to database
    """

    database = SqliteDatabase('personjob.db')

    people = [
        ('Andrew', 'Sumner', 'Andy'),
        ('Peter', 'Seattle', None),
        ('Susan', 'Boston', 'Beannie'),
        ('Pam', 'Coventry', 'PJ'),
        ('Steven', 'Colchester', None),
        ]

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        for person in people:
            with database.transaction():
                new_person = Person.create(
                        person_name = person[0],
                        lives_in_town = person[1],
                        nickname = person[2])
                new_person.save()
                logger.info('Database add successful')

    except Exception as e:
        logger.info(f'Error creating = {person[0]}')
        logger.info(e)

    finally:
        logger.info('database closes')
        database.close()

def populate_job():
    """
    add job data to database
    """
    database = SqliteDatabase('act7.db')
    logger.info('Working with Job class')

    jobs = [
        ('Account Executive', '2016-09-22', '2018-01-30', 55000, 'Andrew'),
        ('Account Manager', '2014-02-01', '2018-03-22', 60000, 'Susan'),
        ('Accounts Payable', '2006-10-23', '2018-04-24', 45000, 'Steven'),
        ('Project Manager', '2012-10-01', '2018-05-10', 80000, 'Pam'),
        ('Project Engineer', '2014-11-14', '2018-06-05', 70000, 'Peter')
    ]

    # write jobs to db... 
    # currently receiving the following error:
    # peewee.IntegrityError: UNIQUE constraint failed: job.job_name...database
    # 
    database.connect()
    database.execute_sql('PRAGMA foreign_keys = ON;')
    for job in jobs:
        with database.transaction():
            new_job = Job.create(
                job_name=job[0],
                start_date=job[1],
                end_date=job[2],
                salary=job[3],
                person_employed=job[4])
            new_job.save()


    database.close()


def populate_department():
    """
    add department data to database
    """
    database = SqliteDatabase('act7.db')
    logger.info('Working with Dept class')

    depts = [
        ('1021', 'Sales', 'Tom', 'Account Executive'),
        ('1021', 'Sales', 'Tom', 'Account Manager'),
        ('1001', 'Accounting', 'Heather', 'Accounts Payable'),
        ('1022', 'Projects', 'Neil', 'Project Manager'),
        ('1022', 'Projects', 'Neil', 'Project Engineer')
    ]

    database.connect()
    database.execute_sql('PRAGMA foreign_keys = ON;')
    for dept in depts:
        with database.transaction():
            new_dept = Department.create(
                dept_num = dept[0],
                dept_name = dept[1],
                dept_mgr_name = dept[2],
                job_name = dept[3])
            new_dept.save()

    database.close()


if __name__ == '__main__':
    populate_person()
    populate_job()
    populate_department()