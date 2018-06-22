
# coding: utf-8

# ### Preface: ORM or not?
# 
# https://www.quora.com/What-are-the-pros-and-cons-of-using-raw-SQL-versus-ORM-for-database-development
# 
# https://www.quora.com/Which-is-better-ORM-or-Plain-SQL
# 
# http://mikehadlow.blogspot.com/2012/06/when-should-i-use-orm.html
# 
# https://enterprisecraftsmanship.com/2015/11/30/do-you-need-an-orm/
# 
# https://medium.com/@mithunsasidharan/should-i-or-should-i-not-use-orm-4c3742a639ce
# 
# https://xkcd.com/1409/
# 
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <div style="font-size:100px;vertical-align: middle;line-height: 2;">🐍</div>

# <div id="menuheading">
# <h2 class="caH2">Relational Databases</h2>
# </div>
# <h3>Introduction</h3>
# <p>In this lesson we are going to look at how to use a relational database with Python.&nbsp;<span>Using relational databases is a massive subject in its own right, but we are going to concentrate on how to use these technologies simply and effectively.</span></p>
# <p><span>What we learn here will be a foundation on which you can build as your database needs increase in volume and complexity.</span></p>
# <h3>Learning Objectives</h3>
# <p>Upon successful completion of this lesson, you will be able to:</p>
# <ul>
# <li>Apply data definition techniques to help assure the quality of the data your Python programs use.</li>
# <li>Store and retrieve single and multiple sets of records in a database from your Python programs so that you can leverage data management services from a database.</li>
# <li>Use simple techniques to help model data correctly in a relational database, and recognize the tradeoffs between different options for this.&nbsp;</li>
# </ul>
# <h3>New Words, Concepts, and Tools</h3>
# <ul>
# <li>We are going to learn about relational databases, data definition and management, and SQL. We will cover object relational mapping and relational database design, but all aligned to simplicity of use with Python.&nbsp;</li>
# </ul>
# <h3>Required Reading</h3>
# <ul>
# <li><span>Relational database <a href="https://www.tutorialspoint.com/sql/sql-rdbms-concepts.htm">concepts</a>.</span></li>
# <li><span>The Peewee&nbsp;<a href="http://docs.peewee-orm.com/en/latest/peewee/quickstart.html">Quickstart</a>.<br /></span></li>
# <li><span>Query&nbsp;</span><a href="http://docs.peewee-orm.com/en/latest/peewee/query_examples.html">examples</a>.</li>
# <li>Peewee <a href="http://docs.peewee-orm.com/en/latest/peewee/models.html">models</a>.</li>
# </ul>
# <h3><span>Optional Reading</span></h3>
# <ul>
# <li>How to <a href="http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html">interact</a> with sqlite from Python (does not use Peewee)</li>
# <li>How to interact with <a href="http://www.postgresqltutorial.com/postgresql-python/">PostgreSQL</a> from Python.</li>
# <li>A great reference book for SQL that shows details of SQL for several databases is "<a href="http://shop.oreilly.com/product/9780596518851.do">SQL in a Nutshell</a>: A Desktop Quick Reference Guide"</li>
# <li>
# <p>If you really want to understand the details of SQL, then this is an excellent book: "<a href="https://www.amazon.com/Celkos-Programming-Kaufmann-Management-Systems/dp/0120887975/ref=mt_paperback?_encoding=UTF8&amp;me=&amp;dpID=51KBLQqsLxL&amp;preST=_SX218_BO1,204,203,200_QL40_&amp;dpSrc=detail">Joe Celko's SQL Programming Style</a> (The Morgan Kaufmann Series in Data Management Systems)"</p>
# </li>
# <li>Data model design is a complex topic that requires lots of knowledge. If you do a lot of database work then the three books in the series "The Data Model Resource Book" (Vol. <a href="https://www.wiley.com/en-us/The+Data+Model+Resource+Book%2C+Volume+1%3A+A+Library+of+Universal+Data+Models+for+All+Enterprises%2C+Revised+Edition-p-9780471380238">1</a>, <a href="https://www.wiley.com/en-us/The+Data+Model+Resource+Book%2C+Volume+2%3A+A+Library+of+Universal+Data+Models+by+Industry+Types%2C+Revised+Edition-p-9780471353485">2</a> and <a href="https://www.wiley.com/en-us/The+Data+Model+Resource+Book%3A+Volume+3%3A+Universal+Patterns+for+Data+Modeling-p-9781118080832">3</a>) are invaluable (the links are the numbers).</li>
# </ul>
# <p><a href="https://github.com/coleifer/peewee/blob/master/docs/peewee/database.rst"></a></p>
# 
# 
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# 

# <div id="menuheading">
#     <h2 class="caH2">Relational Databases</h2>
# </div>
# <p>Here&nbsp;we are going to cover the background to why we use databases, and set the stage for later, when we will start to
#     develop a Python database application.</p>
# <p>You will probably wish to clone the repository you can find on
#     <a href="https://github.com/milesak60/RDBMS">GitHub</a>. For this first video, the files are in the "stuff" directory. These are the files&nbsp;we refer to, and they
#     are included here, below the video:</p>
# 
# <p>&nbsp;</p>
# <h3 style="color:blue"> Video 1: Relational Databases with Python</h3>
# 
# 
# <p><strong>simple_data_write.py</strong></p>

# In[ ]:


"""
write a csv file
data is "anonymous" (no schema)

Creates a file that looks like this:

John,502-77-3056,2/27/1985,117.45

"""

import csv

peopledata = ['John', '502-77-3056', '2/27/1985', 117.45]

with open('simple_data_write.csv', 'w') as people:
    peoplewriter = csv.writer(people, quotechar="'", quoting=csv.QUOTE_ALL)
    peoplewriter.writerow(peopledata)


# ```
# 'John','502-77-3056','2/27/1985','117.45'
# ```
# <br><br>
# <p><strong>simple_data_write_headers.py</strong></p>

# In[ ]:


"""
write a csv file
data is "anonymous" (no schema)

Creates a file that looks like this:

John,502-77-3056,2/27/1985,117.45

"""

import csv

people_headers = ['Person Name','SSN','BirthDate','Account Balance']
people_data = [ 
    ['John', '502-77-3056', '2/27/1985', 117.45],
    ['Jane', '756-01-5323', '12/01/1983', 120.9],   
]

with open('simple_data_write_headers.tsv', 'w') as people:
    peoplewriter = csv.writer(people, delimiter='|', quoting=csv.QUOTE_NONNUMERIC)
    peoplewriter.writerow(people_headers)
    for person in people_data:
        peoplewriter.writerow(person)


# ```
# "Person Name"|"SSN"|"BirthDate"|"Account Balance"
# "John"|"502-77-3056"|"2/27/1985"|"117.45"
# "Jane"|"756-01-5323"|"12/01/1983"|"120.9"
# 
# ```

# <p>&nbsp;</p>
# <p>We have covered the basis of data definition, and why it is important. We now know what a schema is and why it is important.
#     Now we can start to write a Python program that uses a database.</p>
# <p>&nbsp;</p>
# <p>
#     <span>Be sure you cloned the repository we mentioned prior to video 1 from&nbsp;</span>
#     <a href="https://github.com/milesak60/RDBMS">GitHub</a>
#     <span>. In this video we will be using the modules in the "src" directory We start with&nbsp;
#         <a id="fcada5e073825ac239eb86e3cc719691-60640590e74badbeab4e8621d9fdfb7f772c8e13"
#             class="js-navigation-open" title="v00_personjob_model.py" href="https://github.com/milesak60/RDBMS/blob/master/src/v00_personjob_model.py">v00_personjob_model.py</a>.&nbsp;</span>
# </p>
# <p>Key fragments are included here too, below the video.</p>
# 
# 
# <h3 style="color:blue"> Video 2: Using the Model, Using the Person Class, Using the Job Class</h3>
# 
# <p>&nbsp;Here is the model code:</p>
# 

# In[ ]:


"""
    Simple database example with Peewee ORM, sqlite and Python
    Here we define the schema
    Use logging for messages so they can be turned off
"""

import logging
from peewee import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info('One off program to build the classes from the model in the database')

logger.info('Here we define our data (the schema)')
logger.info('First name and connect to a database (sqlite here)')

logger.info('The next 3 lines of code are the only database specific code')

database = SqliteDatabase('personjob.db')
database.connect()
database.execute_sql('PRAGMA foreign_keys = ON;') # needed for sqlite only

logger.info('This means we can easily switch to a different database')
logger.info('Enable the Peewee magic! This base class does it all')
logger.info('By inheritance only we keep our model (almost) technology neutral')

class BaseModel(Model):
    class Meta:
        database = database

class Person(BaseModel):
    """
        This class defines Person, which maintains details of someone
        for whom we want to research career to date.
    """

    logger.info('Note how we defined the class')

    logger.info('Specify the fields in our model, their lengths and if mandatory')
    logger.info('Must be a unique identifier for each person')

    person_name = CharField(primary_key = True, max_length = 30)
    lives_in_town = CharField(max_length = 40)
    nickname = CharField(max_length = 20, null = True)

class Job(BaseModel):
    """
        This class defines Job, which maintains details of past Jobs
        held by a Person.
    """

    logger.info('Now the Job class with a simlar approach')
    job_name = CharField(primary_key = True, max_length = 30)
    logger.info('Dates')
    start_date = DateField(formats = 'YYYY-MM-DD')
    end_date = DateField(formats = 'YYYY-MM-DD')
    logger.info('Number')

    salary = DecimalField(max_digits = 7, decimal_places = 2)
    logger.info('Which person had the Job')
    person_employed = ForeignKeyField(Person, related_name='was_filled_by', null = False)

class PersonNumKey(BaseModel):
    """
        This class defines Person, which maintains details of someone
        for whom we want to research career to date.
    """

    logger.info('An alternate Person class')
    logger.info("Note: no primary key so we're give one 'for free'")

    person_name = CharField(max_length = 30)
    lives_in_town = CharField(max_length = 40)
    nickname = CharField(max_length = 20, null = True)

database.create_tables([
        Job,
        Person,
        PersonNumKey
    ])

database.close()


# 
# 
# <p>&nbsp;</p>
# <p>Now we have looked at the model, lets look at how we create, read, and delete data from the database, using the Person class.&nbsp;Here
#     we use the following code:
#     <span>&nbsp;
#         <a id="912612975805d4e38a8053ae19b98c92-ee318dcdd75197a58d088ae9d65388d47897f0ae" class="js-navigation-open" title="v3_p1_populate_db.py"
#             href="https://github.com/milesak60/RDBMS/blob/master/src/v3_p1_populate_db.py">v3_p1_populate_db.py</a>, then&nbsp;
#         <a id="912612975805d4e38a8053ae19b98c92-ee318dcdd75197a58d088ae9d65388d47897f0ae"
#             class="js-navigation-open" title="v3_p1_populate_db.py" href="https://github.com/milesak60/RDBMS/blob/master/src/v3_p1_populate_db.py">v3_p1_populate_db.py</a>&nbsp;and finally&nbsp;
#         <a id="547d78ff52b12e70bc17913560e473e3-ce96de431e669138e955363304c59f63c6a9c2bc"
#             class="js-navigation-open" title="v3_p3_add_and_delete.py" href="https://github.com/milesak60/RDBMS/blob/master/src/v3_p3_add_and_delete.py">v3_p3_add_and_delete.py</a>
#     </span>.</p>
# <h3 style="color:blue"> Video 3: Using the Person class</h3>
# 

# In[ ]:


# https://raw.githubusercontent.com/milesak60/RDBMS-example/master/personjob_learning_v3_p1.py
"""
    Learning persistence with Peewee and sqlite
    delete the database to start over
        (but running this program does not require it)
"""
import logging
# from personjob_model import *

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
                        person_name = person[PERSON_NAME],
                        lives_in_town = person[LIVES_IN_TOWN],
                        nickname = person[NICKNAME])
                new_person.save()
                logger.info('Database add successful')

        logger.info('Print the Person records we saved...')
        for saved_person in Person:
            logger.info(f'{saved_person.person_name} lives in {saved_person.lives_in_town} ' +                f'and likes to be known as {saved_person.nickname}')

    except Exception as e:
        logger.info(f'Error creating = {person[PERSON_NAME]}')
        logger.info(e)
        logger.info('See how the database protects our data')

    finally:
        logger.info('database closes')
        database.close()

populate_db()


# In[ ]:


# https://raw.githubusercontent.com/milesak60/RDBMS-example/master/personjob_learning_v3_p2.py
"""
    Learning persistence with Peewee and sqlite
    delete the database to start over
        (but running this program does not require it)
"""

# from personjob_model import *

import logging

def select_and_update():
    """"
        show how we can select a specific record, and then search and read through several records
    """

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('personjob.db')

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')

        logger.info('Find and display by selecting a spcific Person name...')
        aperson = Person.get(Person.person_name == 'Susan')

        logger.info(f'{aperson.person_name} lives in {aperson.lives_in_town} ' +         f' and likes to be known as {aperson.nickname}')

        logger.info('Search and display all Person with missing nicknames')
        logger.info('Our person class inherits select(). Specify search with .where()')
        logger.info('Peter gets a nickname but noone else')

        for person in Person.select().where(Person.nickname == None):
            logger.info(f'{person.person_name} does not have a nickname; see: {person.nickname}')
            if person.person_name == 'Peter':
                logger.info('Changing nickname for Peter')
                logger.info('Update the database')
                person.nickname = 'Painter'
                person.save()
            else:
                logger.info(f'Not giving a nickname to {person.person_name}')

        logger.info('And here is where we prove it by finding Peter and displaying')
        aperson = Person.get(Person.person_name == 'Peter')
        logger.info(f'{aperson.person_name} now has a nickname of {aperson.nickname}')

    except Exception as e:
        logger.info(e)

    finally:
        database.close()

select_and_update()


# In[ ]:


# https://raw.githubusercontent.com/milesak60/RDBMS-example/master/personjob_learning_v3_p3.py

"""
    Learning persistence with Peewee and sqlite
    delete the database to start over
        (but running this program does not require it)
"""

import logging

# from personjob_model import *

database = SqliteDatabase('personjob.db')

def add_and_delete():
    """"
        show how we can add a record, and delete a record
    """

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('personjob.db')
    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')

        logger.info('Add and display a Person called Fred; then delete him...')
        logger.info('Add Fred in one step')

        new_person = Person.create(
            person_name = 'Fred',
            lives_in_town = 'Seattle',
            nickname = 'Fearless')
        new_person.save()

        logger.info('Show Fred')
        aperson = Person.get(Person.person_name == 'Fred')

        logger.info(f'We just created {aperson.person_name}, who lives in {aperson.lives_in_town}')
        logger.info('but now we will delete him...')

        aperson.delete_instance()

        logger.info('Reading and print all Person records (but not Fred; he has been deleted)...')

        for person in Person:
            logger.info(f'{person.person_name} lives in {person.lives_in_town} and likes to be known as {person.nickname}')

    except Exception as e:
        logger.info(e)

    finally:
        database.close()

add_and_delete()


# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# <p>&nbsp;</p>
# <p>Working with one class is not typical. Usually we will have several. We'll illustrate this by working with the Job class.
#     He we will use all the Python modules for the repository that start with v4:</p>
# <h3 style="color:blue"> Video 4: Using the Job class</h3>
# 
# 
# 
# 
# 
# 
# 
# 
# 

# In[ ]:


# https://github.com/milesak60/RDBMS-example/blob/master/personjob_learning_v5_p1.py

"""
    Learning persistence with Peewee and sqlite
    delete the database to start over
        (but running this program does not require it)
"""

# from personjob_model import *

import logging

def populate_db():
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

populate_db()


# In[ ]:


# https://raw.githubusercontent.com/milesak60/RDBMS-example/master/personjob_learning_v5_p2.py

"""
    Learning persistence with Peewee and sqlite
    delete the database to start over
        (but running this program does not require it)
"""

def join_classes():
    """
        demonstrate how to join classes together : matches
    """

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('personjob.db')

    logger.info('Working with Job class')

    logger.info('Now resolve the join and print (INNER shows only jobs that match person)...')
    logger.info('Notice how we use a query variable in this case')
    logger.info('We select the classes we need, and we join Person to Job')
    logger.info('Inner join (which is the default) shows only records that match')

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        query = (Person
                 .select(Person, Job)
                 .join(Job, JOIN.INNER)
                )

        logger.info('View matching records from both tables')
        for person in query:
            logger.info(f'Person {person.person_name} had job {person.job.job_name}')

    except Exception as e:
        logger.info(f'Error creating = {job[JOB_NAME]}')
        logger.info(e)

    finally:
        logger.info('database closes')
        database.close()

join_classes()


# In[ ]:


# https://raw.githubusercontent.com/milesak60/RDBMS-example/master/personjob_learning_v5_p3.py


"""
    Learning persistence with Peewee and sqlite
    delete the database to start over
        (but running this program does not require it)
"""

def join_classes():
    """
        demonstrate how to join classes together : no matches too
    """

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('personjob.db')

    logger.info('View matching records and Persons without Jobs (note LEFT_OUTER)')

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        query = (Person
                 .select(Person, Job)
                 .join(Job, JOIN.LEFT_OUTER)
                )

        for person in query:
            try:
                logger.info(f'Person {person.person_name} had job {person.job.job_name}')

            except Exception as e:
                logger.info(f'Person {person.person_name} had no job')


        logger.info('Example of how to summarize data')
        logger.info('Note select() creates a count and names it job_count')
        logger.info('group_by and order_by control level and sorting')

        query = (Person
                 .select(Person, fn.COUNT(Job.job_name).alias('job_count'))
                 .join(Job, JOIN.LEFT_OUTER)
                 .group_by(Person)
                 .order_by(Person.person_name))

        for person in query:
            logger.info(f'{person.person_name} had {person.job_count} jobs')


    except Exception as e:
        logger.info(e)

    finally:
        database.close()

join_classes()


# In[ ]:


# https://raw.githubusercontent.com/milesak60/RDBMS-example/master/personjob_learning_v5_p4.py
"""
    Learning persistence with Peewee and sqlite
    delete the database to start over
        (but running this program does not require it)
"""

def show_integrity_add():
    """
        demonstrate how database protects data inegrity : add
    """

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('personjob.db')

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        with database.transaction():
            logger.info('Try to add a new job where a person doesnt exist...')

            addjob = ('Sales', '2010-04-01', '2018-02-08', 80400, 'Harry')

            logger.info('Adding a sales job for Harry')
            logger.info(addjob)
            new_job = Job.create(
                job_name = addjob[JOB_NAME],
                start_date = addjob[START_DATE],
                end_date = addjob[END_DATE],
                salary = addjob[SALARY],
                person_employed = addjob[PERSON_EMPLOYED])
            new_job.save()

    except Exception as e:
        logger.info('Add failed because Harry is not in Person')
        logger.info(f'For Job create: {addjob[0]}')
        logger.info(e)

show_integrity_add()


# In[ ]:


# https://raw.githubusercontent.com/milesak60/RDBMS-example/master/personjob_learning_v5_p5.py
"""
    Learning persistence with Peewee and sqlite
    delete the database to start over
        (but running this program does not require it)
"""

def show_integrity_del():
    """
        demonstrate how database protects data inegrity : delete
    """
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('personjob.db')

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        logger.info('Try to Delete a person who has jobs...')
        with database.transaction():
            aperson = Person.get(Person.person_name == 'Andrew')
            logger.info(f'Trying to delete {aperson.person_name} who lives in {aperson.lives_in_town}')
            aperson.delete_instance()

    except Exception as e:
        logger.info('Delete failed because Andrew has Jobs')
        logger.info(f'Delete failed: {aperson.person_name}')
        logger.info(e)

    finally:
        database.close()
        
show_integrity_del()


# In[ ]:


# https://raw.githubusercontent.com/milesak60/RDBMS-example/master/personjob_learning_v5_p6.py
"""
    Learning persistence with Peewee and sqlite
    delete the database to start over
        (but running this program does not require it)
"""

def add_with_without_BK():
    """
        demonstrate impact of business keys
    """

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

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    database = SqliteDatabase('personjob.db')

    logger.info('Try creating Person records again: it will fail')

    try:
        database.connect()
        database.execute_sql('PRAGMA foreign_keys = ON;')
        try:
            with database.transaction():
                for person in people:
                    new_person = Person.create(
                        person_name = person[PERSON_NAME],
                        lives_in_town = person[LIVES_IN_TOWN],
                        nickname = person[NICKNAME])
                    new_person.save()
                    logger.info('Database add successful')

        except Exception as e:
            logger.info(f'Error creating = {person[PERSON_NAME]}')
            logger.info(e)

        logger.info('We make sure duplicates are not unintentionally created this way')
        logger.info('BUT: how do we really identify a Person (uniquely)?')

        logger.info('Creating Person records, but in a new table with generated PK...')
        try:
            with database.transaction():
                for person in people:
                    new_person = PersonNumKey.create(
                        person_name = person[PERSON_NAME],
                        lives_in_town = person[LIVES_IN_TOWN],
                        nickname = person[NICKNAME])
                    new_person.save()

        except Exception as e:
            logger.info(f'Error creating = {person[0]}')
            logger.info(e)

        logger.info('Watch what happens when we do it again')

        try:
            with database.transaction():
                for person in people:
                    new_person = PersonNumKey.create(
                        person_name = person[PERSON_NAME],
                        lives_in_town = person[LIVES_IN_TOWN],
                        nickname = person[NICKNAME])
                    new_person.save()

        except Exception as e:
            logger.info(f'Error creating = {person[0]}')
            logger.info(e)

        logger.info('Note no PK specified, no PK violation; "duplicates" created!')
        for person in PersonNumKey.select():
            logger.info(f'Name : {person.person_name} with id: {person.id}')

    except Exception as e:
        logger.info(e)

    finally:
        database.close()

add_with_without_BK()


# In[ ]:


# https://raw.githubusercontent.com/milesak60/RDBMS-example/master/personjob_learning_v5_p7.py
"""
    Learning persistence with Peewee and sqlite
    delete the database to start over
        (but running this program does not require it)
"""

def cant_change_PK():
    """
        show that PKs cant be changed (and that there is no error!)
    """

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    logger.info("Back to Person class: try to change Peter's name")

    aperson = Person.get(Person.person_name == 'Peter')
    logger.info(f'Current value is {aperson.person_name}')

    logger.info('Update Peter to Peta, thereby trying to change the PK...')

    try:
        try:
            with database.transaction():
                aperson = Person.get(Person.person_name == 'Peter')
                aperson.person_name = 'Peta'
                aperson.save()
                logger.info(f'Tried to change Peter to {aperson.person_name}')

        except Exception as e:
            logger.info(f'Cant change a PK and caught you trying') # not caught; no error thrown by Peewee
            logger.info(e)

        aperson = Person.get(Person.person_name == 'Peter')
        logger.info(f'Looked for Peter: found! -> {aperson.person_name}')

        try:
            aperson = Person.get(Person.person_name == 'Peta')

        except Exception as e:
            logger.info(f'Looking for Peta results in zero records. PK changes are ignored and do not throw an error!!!!')
            logger.info(f'Cant change a PK')
            logger.info('PK "change" can only be achieved with a delete and new create')

    finally:
        database.close()

cant_change_PK()


# 
# 
# 
# 
# 
# 
# 
# 
# <p>&nbsp;</p>
# <p>Now we are going to learn about the best way to design the data in our database. &nbsp;We will use the digram in the "stuff"
#     directory, which is also included below, along with the SQL code:</p>
# <p>&nbsp;</p>
# <h3 style="color:blue"> Video: Behind the scenes / Database Technologies</h3>
# 
# <p>&nbsp;</p>
# <p>Database diagram:</p>
# <p>&nbsp;
#     <img src="DatabaseDiagram.jpeg"/>&nbsp;</p>
# <p>Code samples from the video:</p>
# <p>SQL statement</p>
# <div style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">
#     <pre style="margin: 0; line-height: 125%;"><span style="color: #008800; font-weight: bold;">select</span><span style="color: #333333;">*</span> <span style="color: #008800; font-weight: bold;">from</span> person;
# </pre>
# </div>
# <p>Start sqlite3 database (from the command line):</p>
# <div style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">
#     <pre style="margin: 0; line-height: 125%;">sqlite3 personjob.db
# </pre>
# </div>
# <p>The sqlite&gt; prompt indicates we are ready to enter sqlite commands.</p>
# <div style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">
#     <pre style="margin: 0; line-height: 125%;">sqlite&gt; .tables
# job person personnumkey
# </pre>
# </div>
# <p>&nbsp; Here is how sqlite sees the schema:</p>
# <div style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">
#     <pre style="margin: 0; line-height: 125%;">sqlite<span style="color: #333333;">&gt;</span> .<span style="color: #008800; font-weight: bold;">schema</span>
# 
# <span style="color: #008800; font-weight: bold;">CREATE</span> <span style="color: #008800; font-weight: bold;">TABLE</span> IF <span style="color: #008800; font-weight: bold;">NOT</span> <span style="color: #008800; font-weight: bold;">EXISTS</span> <span style="color: #aa6600;">"person"</span> (<span style="color: #aa6600;">"person_name"</span> <span style="color: #007020;">VARCHAR</span>(<span style="color: #0000dd; font-weight: bold;">30</span>) <span style="color: #008800; font-weight: bold;">NOT</span> <span style="color: #008800; font-weight: bold;">NULL</span> <span style="color: #008800; font-weight: bold;">PRIMARY</span> <span style="color: #008800; font-weight: bold;">KEY</span>, <span style="color: #aa6600;">"lives_in_town"</span> <span style="color: #007020;">VARCHAR</span>(<span style="color: #0000dd; font-weight: bold;">40</span>) <span style="color: #008800; font-weight: bold;">NOT</span> <span style="color: #008800; font-weight: bold;">NULL</span>, <span style="color: #aa6600;">"nickname"</span> <span style="color: #007020;">VARCHAR</span>(<span style="color: #0000dd; font-weight: bold;">20</span>));<br />
# <span style="color: #008800; font-weight: bold;">CREATE</span> <span style="color: #008800; font-weight: bold;">TABLE</span> IF <span style="color: #008800; font-weight: bold;">NOT</span> <span style="color: #008800; font-weight: bold;">EXISTS</span> <span style="color: #aa6600;">"job"</span> (<span style="color: #aa6600;">"job_name"</span> <span style="color: #007020;">VARCHAR</span>(<span style="color: #0000dd; font-weight: bold;">30</span>) <span style="color: #008800; font-weight: bold;">NOT</span> <span style="color: #008800; font-weight: bold;">NULL</span> <span style="color: #008800; font-weight: bold;">PRIMARY</span> <span style="color: #008800; font-weight: bold;">KEY</span>, <span style="color: #aa6600;">"start_date"</span> <span style="color: #007020;">DATE</span> <span style="color: #008800; font-weight: bold;">NOT</span> <span style="color: #008800; font-weight: bold;">NULL</span>, <span style="color: #aa6600;">"end_date"</span> <span style="color: #007020;">DATE</span> <span style="color: #008800; font-weight: bold;">NOT</span> <span style="color: #008800; font-weight: bold;">NULL</span>, <span style="color: #aa6600;">"salary"</span> <span style="color: #007020;">DECIMAL</span>(<span style="color: #0000dd; font-weight: bold;">7</span>, <span style="color: #0000dd; font-weight: bold;">2</span>) <span style="color: #008800; font-weight: bold;">NOT</span> <span style="color: #008800; font-weight: bold;">NULL</span>, <span style="color: #aa6600;">"person_employed_id"</span> <span style="color: #007020;">VARCHAR</span>(<span style="color: #0000dd; font-weight: bold;">30</span>) <span style="color: #008800; font-weight: bold;">NOT</span> <span style="color: #008800; font-weight: bold;">NULL</span>, <span style="color: #008800; font-weight: bold;">FOREIGN</span> <span style="color: #008800; font-weight: bold;">KEY</span> (<span style="color: #aa6600;">"person_employed_id"</span>) <span style="color: #008800; font-weight: bold;">REFERENCES</span> <span style="color: #aa6600;">"person"</span> (<span style="color: #aa6600;">"person_name"</span>));<br />
# <span style="color: #008800; font-weight: bold;">CREATE</span> <span style="color: #008800; font-weight: bold;">INDEX</span> <span style="color: #aa6600;">"job_person_employed_id"</span> <span style="color: #008800; font-weight: bold;">ON</span> <span style="color: #aa6600;">"job"</span> (<span style="color: #aa6600;">"person_employed_id"</span>);<br />
# <span style="color: #008800; font-weight: bold;">CREATE</span> <span style="color: #008800; font-weight: bold;">TABLE</span> IF <span style="color: #008800; font-weight: bold;">NOT</span> <span style="color: #008800; font-weight: bold;">EXISTS</span> <span style="color: #aa6600;">"personnumkey"</span> (<span style="color: #aa6600;">"id"</span> <span style="color: #007020;">INTEGER</span> <span style="color: #008800; font-weight: bold;">NOT</span> <span style="color: #008800; font-weight: bold;">NULL</span> <span style="color: #008800; font-weight: bold;">PRIMARY</span> <span style="color: #008800; font-weight: bold;">KEY</span>, <span style="color: #aa6600;">"person_name"</span> <span style="color: #007020;">VARCHAR</span>(<span style="color: #0000dd; font-weight: bold;">30</span>) <span style="color: #008800; font-weight: bold;">NOT</span> <span style="color: #008800; font-weight: bold;">NULL</span>, <span style="color: #aa6600;">"lives_in_town"</span> <span style="color: #007020;">VARCHAR</span>(<span style="color: #0000dd; font-weight: bold;">40</span>) <span style="color: #008800; font-weight: bold;">NOT</span> <span style="color: #008800; font-weight: bold;">NULL</span>, <span style="color: #aa6600;">"nickname"</span> <span style="color: #007020;">VARCHAR</span>(<span style="color: #0000dd; font-weight: bold;">20</span>));<br />
# </pre>
# </div>
# <p>&nbsp;</p>
# <p>&nbsp;</p>
# <div style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">
#     <pre style="margin: 0; line-height: 125%;">sqlite<span style="color: #333333;">&gt;</span> .<span style="color: #008800; font-weight: bold;">mode</span> <span style="color: #008800; font-weight: bold;">column</span>
# sqlite<span style="color: #333333;">&gt;</span> .width <span style="color: #0000dd; font-weight: bold;">15</span> <span style="color: #0000dd; font-weight: bold;">15</span> <span style="color: #0000dd; font-weight: bold;">15</span> <span style="color: #0000dd; font-weight: bold;">15</span> <span style="color: #0000dd; font-weight: bold;">15</span>
# sqlite<span style="color: #333333;">&gt;</span> .headers <span style="color: #008800; font-weight: bold;">on</span>
# </pre>
# </div>
# <p>&nbsp;</p>
# <div style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">
#     <pre style="margin: 0; line-height: 125%;">sqlite<span style="color: #333333;">&gt;</span> <span style="color: #008800; font-weight: bold;">select</span> <span style="color: #333333;">*</span> <span style="color: #008800; font-weight: bold;">from</span> person;
# sqlite<span style="color: #333333;">&gt;</span> <span style="color: #008800; font-weight: bold;">select</span> <span style="color: #333333;">*</span> <span style="color: #008800; font-weight: bold;">from</span> job;
# </pre>
# </div>
# <p>Enter .quit to leave sqlite.</p>
# <h2>Lesson Summary</h2>
# <p>In this lesson we have learned about how we define, store and retrieve data in a relational database using Python, Peewee
#     and sqlite.</p>
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 

# <p>&nbsp;</p>
# <h3 style="color:blue"> Video: Conclusion</h3>
# <p>&nbsp;
#     <a href="https://github.com/coleifer/peewee/blob/master/docs/peewee/database.rst">PeeWee documentation</a>
# </p>
# <p>&nbsp;</p>

# <br>
# <br>
# <br>
# <br>
# <br>
# 
# ## Non-ORM Example

# In[ ]:


import sqlite3
import os

database_filename = "personjob.db"

try:
    # remove if file exists
    os.remove(database_filename)
except:
    # ignore if file doesn't exist
    pass 

statements = [
    """CREATE TABLE IF NOT EXISTS "person" ("person_name" VARCHAR(30) NOT NULL PRIMARY KEY, "lives_in_town" VARCHAR(40) NOT NULL, "nickname" VARCHAR(20));""",
    """CREATE TABLE IF NOT EXISTS "job" ("job_name" VARCHAR(30) NOT NULL PRIMARY KEY, "start_date" DATE NOT NULL, "end_date" DATE NOT NULL, "salary" DECIMAL(7, 2) NOT NULL, "person_employed_id" VARCHAR(30) NOT NULL, FOREIGN KEY ("person_employed_id") REFERENCES "person" ("person_name"));""",
    """CREATE INDEX "job_person_employed_id" ON "job" ("person_employed_id");""",
    """CREATE TABLE IF NOT EXISTS "personnumkey" ("id" INTEGER NOT NULL PRIMARY KEY, "person_name" VARCHAR(30) NOT NULL, "lives_in_town" VARCHAR(40) NOT NULL, "nickname" VARCHAR(20));""",
]

with sqlite3.connect(database_filename) as conn:
    try:        
        for stmt in statements:
            print(stmt)
            conn.execute(stmt)
    except Exception as e:
        print(e)


# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# 
# 
# <div id="menuheading">
# <h2 class="caH2">Activity</h2>
# </div>
# <h3><span>Warm up for the assignment</span></h3>
# <p><span>Before we launch into the&nbsp;</span>assignment, let's be sure that you have everything you need to get started. We'll enhance the modules from the video along the way.</p>
# <h3>Preparing</h3>
# <p>Be sure to</p>
# <div style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">
# <pre style="margin: 0; line-height: 125%;">pip install peewee
# </pre>
# </div>
# <p>&nbsp;first.</p>
# <p>Also, be sure that&nbsp;&nbsp;</p>
# <div style="background: #ffffff; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">
# <pre style="margin: 0; line-height: 125%;">sqlite3 -version
# </pre>
# </div>
# <p><span>returns the sqlite3 version number, indicating it is installed. It should be, as it's bundled with Python 3.</span></p>
# <p><span>Clone the repo at&nbsp;</span></p>
# <pre>git@github.com:milesak60/RDBMS.git</pre>
# <p><span>although you should&nbsp;already have that from earlier in this lesson.</span></p>
# <p>Make sure everything runs before proceeding to the next step.</p>
# <h3>Let's add a department</h3>
# <p>We have details of Persons. We have details of Jobs. Now we need to track in which Department a Person held a Job. For a Department, we need to know it's department number, which is 4 characters long and start with a letter. We need to know the department name (30 characters), and the name of the department manager (30 characters). We also need to know the duration in days that the job was held. Think about this last one carefully.</p>
# <p>Make the necessary changes, annotating the code with log statements to explain what's going on. Also, draw a digram to help think through how you will incorporate Department into the programs.</p>
# <p>Finally, produce a list using pretty print that shows all of the departments a person worked in for every job they ever had.&nbsp;</p>
# <h3><span>Instructions</span></h3>
# <p><span></span>Once you've completed the activity from the lesson content, commit your changes and submit:</p>
# <ul>
# <li>a link to your repository&nbsp;on GitHub</li>
# <li>the relevant .py file(s)</li>
# </ul>
# <p>We'll be grading this&nbsp;activity&nbsp;purely on the percentage of included tests that pass.</p>
# <h3>Submitting Your Work&nbsp;</h3>
# <p>Put the&nbsp;file(s) (ex: a_new_file.py) in your student directory in a new subdirectory named for this lesson, and add it to your clone early (git add a_new_file.py). Make frequent commits with good, clear messages about what you're doing and why.</p>
# <p>When you're done and ready for the instructors to review your work, push your changes to your GitHub fork (git push) and then go to the GitHub website and make a pull request. Copy the link to the pull request.</p>
# <p>Click&nbsp;the <em>Submit Assignment</em> button in the upper right.</p>
# <p><strong>Part 1: File(s)</strong></p>
# <p>Use the&nbsp;<em>Choose File</em>&nbsp;button to find and select the saved&nbsp;.py file or, if there are multiple files for the assignment, the .zip file.</p>
# <p><strong>Part 2: GitHub Link</strong></p>
# <p>Paste the GitHub link to the pull request in the comments area.</p>
# <p>Click the&nbsp;<em>Submit Assignment </em>button.</p>

# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# 
# 
# <div id="menuheading">
# <h2 class="caH2">Assignment</h2>
# </div>
# <h3>Instructions</h3>
# <p><span><strong>Goal:</strong></span></p>
# <p><span>Redesign&nbsp;the object oriented mailroom program from class one using Peewee classes so that the data is persisted in sqlite. The approach you used in the OO exercise will naturally lend itself to this.</span> <i>(See Lesson 4, video 2)</i></p>
# <p><span><strong>Suggestions</strong></span></p>
# <p><span>You will need ways to add, update and delete data. Update and delete will mean that you need to find the data to update / delete. Perhaps you can do this by allowing a search first, and then selecting the particular instance to delete.</span></p>
# <p>Remember that you need to read from the database, rather than relying on data held in variables when your program is running. To show you understand how this works, run the donor report from a separate program that read the database.</p>
# <p><span>Generally, be sure to adapt the exception handling so that it helps identify any database errors, and consider how you may need to adapt your tests.</span></p>
# <p><span>Be sure to give a lot of thought to what you should use as the primary key for your Peewee classes. In doing this, just consider data items that are unique in the context of the mailroom application. If you have to resort to generated keys, be sure to note why in the applicable docstring. And talking of which, be sure to define all your classes, as you learned in the videos.</span></p>
# <p><span>The example programs for the videos will be a good starting point for reminders of syntax, but remember that the primary determinate of the structure of your solution will be a good object oriented Python application. The fact that it will now be persistent should not make too ,much difference.</span>&nbsp;</p>
# <h3><span></span></h3>
# <h3>Submitting Your Work&nbsp;</h3>
# <p>Put the&nbsp;file(s) (ex: a_new_file.py) in your student directory in a new subdirectory named for this lesson, and add it to your clone early (git add a_new_file.py). Make frequent commits with good, clear messages about what you're doing and why.</p>
# <p>When you're done and ready for the instructors to review your work, push your changes to your GitHub fork (git push) and then go to the GitHub website and make a pull request. Copy the link to the pull request.</p>
# <p>Click&nbsp;the <em>Submit Assignment</em> button in the upper right.</p>
# <p><strong>Part 1: File(s)</strong></p>
# <p>Use the&nbsp;<em>Choose File</em>&nbsp;button to find and select the saved&nbsp;.py file or, if there are multiple files for the assignment, the .zip file.</p>
# <p><strong>Part 2: GitHub Link</strong></p>
# <p>Paste the GitHub link to the pull request in the comments area.</p>
# <p>Click the&nbsp;<em>Submit Assignment </em>button.</p>

# <div style="font-size:100px;vertical-align: middle;line-height: 2;">👹</div>
