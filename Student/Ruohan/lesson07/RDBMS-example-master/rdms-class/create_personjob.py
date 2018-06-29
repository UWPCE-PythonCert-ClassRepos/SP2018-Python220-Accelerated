"""
    Create database examle with Peewee ORM, sqlite and Python

"""

from personjob_model import *

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from peewee import *

logger.info('One off program to build the classes from the model in the database')

database.create_tables([
        Department,
        Job,
        Person,
        PersonNumKey
    ])

database.close()
