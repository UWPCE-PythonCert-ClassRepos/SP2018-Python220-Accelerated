"""
    Learning persistence with Peewee and sqlite
    delete the database to start over
        (but running this program does not require it)
"""

from personjob_model import *

import logging

def populate_db():
    """
        this is a proof of concept because i cant download peewee with only add department data to database
    """

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('personjob.db')

    logger.info('Working with Job class')
    logger.info('Creating Job records: just like Person. We use the foreign key')

    DEPARTMENT_NUMBER = 0
    DEPARTMENT_NAME = 1
    DEPARTMENT_MANAGER = 2

    departments = [
        ('PM01', 'Product Management', 'Mario Mario'),
        ('MK01', 'Marketing', 'Luigi Mario'),
        ('FN01', 'Finance', 'King Koopa')
        ]

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        for department in departments:
            with database.transaction():
                new_department = Department.create(
                    department_number = departments[DEPARTMENT_NUMBER],
                    department_name = departments[DEPARTMENT_NAME],
                    department_manager = departments[DEPARTMENT_MANAGER]
                new_department.save()

        logger.info('Reading and print all Department rows (note the value of person)...')
        for department in departments:
            logger.info(f'{department.department_number} : {department.department_name}')

    except Exception as e:
        logger.info(f'Error creating = {department[department_number]}')
        logger.info(e)

    finally:
        logger.info('database closes')
        database.close()

print_db():
'''
in theory this function should work, but it would be 50 times easier in sql
'''
departments = (Person
          .select(Person, Job)
          .join(Job))
for tweet in tweets:
    print(department.person_name, department.job.job_name, department.job.department_id)


if __name__ == '__main__':
    populate_db()
    print_db()
