"""
    Learning persistence with Peewee and sqlite
    delete the database to start over
        (but running this program does not require it)
"""
import logging
from personjob_model import *

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

    dept_number = 0
    dept_name = 1
    dept_manager = 2

    department = [
        ('A001', 'Comms', 'Andy'),
        ('B002', 'Marketing', 'Tammy'),
        ('C003', 'Fancy', 'Beannie'),
        ]

    logger.info('Creating Person records: iterate through the list of tuples')
    logger.info('Prepare to explain any errors with exceptions')
    logger.info('and the transaction tells the database to fail on error')

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        for department in department:
            with database.transaction():
                new_dept = Department.create(
                        dept_number = department[dept_number],
                        dept_name = department[dept_name],
                        dept_manager = department[dept_manager])
                new_dept.save()
                logger.info('Database add successful')

        logger.info('Print the Department records we saved...')
        for saved_dept in Department:
            logger.info(f'{saved_dept.dept_number} department is for {saved_dept.dept_name} ' +\
                f'and likes to be known as {saved_dept.dept_manager}')

    except Exception as e:
        logger.info(f'Error creating = {department[dept_number]}')
        logger.info(e)
        logger.info('See how the database protects our data')

    finally:
        logger.info('database closes')
        database.close()

if __name__ == '__main__':
    populate_db()