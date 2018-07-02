'''
Wesley Wang
Activity 7
'''

from peewee import *

database = SqliteDatabase('C:\_Python220AC\SP2018-Python220-Accelerated\Student\WesWang\Lesson7\Activity\personjob.db')
database.connect()
database.execute_sql('PRAGMA foreign_keys = ON;')

class BaseModel(Model):
    class Meta:
        database = database


class Person(BaseModel):
    person_id = PrimaryKeyField()
    person_name = CharField(max_length = 30)
    lives_in_town = CharField(max_length = 40)
    nickname = CharField(max_length = 20, null = True)


class Department(BaseModel):
    dpt_number = CharField(primary_key = True ,max_length = 4)
    dpt_name = CharField(max_length = 30)
    dpt_mngr = CharField(max_length = 30)
    class Meta:
        constraints = [Check('SUBSTR(dpt_number,1) LIKE "[a-z][A-Z]"')]


class Job(BaseModel):
    job_id = PrimaryKeyField()
    job_name = CharField(max_length = 30)
    start_date = DateField(formats = 'YYYY-MM-DD')
    end_date = DateField(formats = 'YYYY-MM-DD')
    salary = DecimalField(max_digits = 7, decimal_places = 2)
    person_employed = ForeignKeyField(Person, related_name = 'was_filled_by', null = False)
    dpt_number = ForeignKeyField(Department, related_name = 'worked_at', null = False)


database.create_tables([Person, Department, Job])
