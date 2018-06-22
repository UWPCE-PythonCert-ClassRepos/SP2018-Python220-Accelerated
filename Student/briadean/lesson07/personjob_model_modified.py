#!/usr/bin/env python3
"""
Simple database example with Peewee ORM, sqlite and Python
Here we define the schema and create the database tables
"""

from peewee import *

database = SqliteDatabase('personjob.db')
database.connect()
database.execute_sql('PRAGMA foreign_keys = ON;')


class BaseModel(Model):
    class Meta:
        database = database


class Person(BaseModel):
    person_name = CharField(primary_key=True, max_length=30)
    lives_in_town = CharField(max_length=30)
    nickname = CharField(max_length=20, null=True)


class Department(BaseModel):
    dept_id = CharField(primary_key=True, max_length=4)
    dept_name = CharField(max_length=30)
    dept_manager = CharField(max_length=30)


class Job(BaseModel):
    job_name = CharField(primary_key=True, max_length=30)
    start_date = DateField(formats='YYYY-MM-DD')
    end_date = DateField(formats='YYYY-MM-DD')
    salary = DecimalField(max_digits=7, decimal_places=2)
    person_employed = ForeignKeyField(Person, related_name='was_filled_by', null=False)
    job_duration = IntegerField()
    dept_id = ForeignKeyField(Department, related_name='department_id', null=False)


class PersonNumKey(BaseModel):
    person_name = CharField(max_length=30)
    lives_in_town = CharField(max_length=30)
    nickname = CharField(max_length=20, null=True)


database.create_tables([Job,
                        Person,
                        PersonNumKey,
                        Department])
