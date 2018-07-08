# Primarily based off of the sample program provided

"""
    Simple database examle with Peewee ORM, sqlite and Python
    Here we define the schema
"""

from peewee import *

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
        This class defines Job, which maintains details of past Jobs held by a Person.
    """
    job_name = CharField(primary_key=True, max_length=30)
    start_date = DateField(formats='YYYY-MM-DD')
    end_date = DateField(formats='YYYY-MM-DD')
    salary = DecimalField(max_digits=7, decimal_places=2)
    person_employed = ForeignKeyField(
        Person, related_name='was_filled_by', null=False)


class PersonNumKey(BaseModel):
    """
        This class defines Person, which maintains details of someone
        for whom we want to research career to date.
    """
    person_name = CharField(max_length=30)
    lives_in_town = CharField(max_length=40)
    nickname = CharField(max_length=20, null=True)


class Department(BaseModel):
    """
    Class that defines the department details by a Person.
    """
    dept_number = CharField(primary_key = True, max_length = 4)
    dept_name = CharField(max_length = 30)
    dept_manager = CharField(max_length = 30)
    job_duration = IntegerField()
    job_title = ForeignKeyField(Job, related_name = '')

database.create_tables([Person, Job, Department, PersonNumKey])

database.close()
