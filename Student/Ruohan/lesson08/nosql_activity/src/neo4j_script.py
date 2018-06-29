"""
    neo4j example
"""


import utilities
import login_database
import utilities
import random

log = utilities.configure_logger('default', '../logs/neo4j_script.log')


def run_example():

    log.info('Step 1: First, clear the entire database, so we can start over')
    log.info("Running clear_all")

    driver = login_database.login_neo4j_cloud()
    with driver.session() as session:
        session.run("MATCH (n) DETACH DELETE n")

    log.info("Step 2: Add a few people and color")

    with driver.session() as session:

        log.info('Adding a few Person nodes and new Person for activity')
        log.info('The cyph language is analagous to sql for neo4j')
        names = [('Bob', 'Jones'),
                ('Nancy', 'Cooper'),
                ('Alice', 'Cooper'),
                ('Fred', 'Barnes'),
                ('Mary', 'Evans'),
                ('Marie', 'Curie'),
                ('Ellen', 'DeGeneres'),
                ('Cara', 'Delevine'),
                ]
        for first, last in names:
            cyph = "CREATE (n:Person {first_name:'%s', last_name: '%s'})" % (first, last)
            session.run(cyph)

        # Add some colors
        log.info("Adding some colors")
        colors = [('Red'),
                  ('Yellow'),
                  ('White'),
                  ('Blue'),
                  ('Pink'),
                  ('Green'),
                  ('Brown'),
                  ]
        for color in colors:
            cyph = "CREAT (n:Color {color: '%s'})" % (color)
            session.run(cyph)

        log.info("Step 3: Get all of people and color in the DB:")
        cyph = """MATCH (p:Person)
                  RETURN p.first_name as first_name, p.last_name as last_name
                """
        result = session.run(cyph)
        print("People in database:")
        for record in result:
            print(record['first_name'], record['last_name'])

        cyph = """MATCH (p:Color)
                  RETURN p.color as color
                """
        result = session.run(cyph)
        print("Color in database:")
        for record in result:
            print(record['color'])

        #creat associations between Person and color
        log.info('Step 4: Create some relationships')
        log.info('Create associations between Person and Color')
        #assume person has two favorate color, random seleced from colors
        i1 = random.randrange(0, len(colors))
        i2 = random.randrange(0, len(colors))
        for first, last in names:
            cypher = """
              MATCH (p1:Person {first_name: '%s', last_name: '%s'})
              CREAT (p1)-[favorate_color: FAVORATE_COLOR]->(p2:Color{color: '%s', '%s'})
              RETURN p1.first_name as first_name, p1.last_name as last_name, p2.color as color
            """ % (first, last, color[i1], color[i2])
            result = session.run(cypher)
            for record in result:
                print(record['first_name'],' ',{record['last_name']},' favorate color are ', record['color'] )

        log.info('Create associations among Person')
        log.info("Bob Jones likes Alice Cooper, Fred Barnes and Marie Curie")

        for first, last in [("Alice", "Cooper"),
                            ("Fred", "Barnes"),
                            ("Marie", "Curie")]:
            cypher = """
              MATCH (p1:Person {first_name:'Bob', last_name:'Jones'})
              CREATE (p1)-[friend:FRIEND]->(p2:Person {first_name:'%s', last_name:'%s'})
              RETURN p1
            """ % (first, last)
            session.run(cypher)

        log.info("Step 5: Find all of Bob's friends")
        cyph = """
          MATCH (bob {first_name:'Bob', last_name:'Jones'})
                -[:FRIEND]->(bobFriends)
          RETURN bobFriends
          """
        result = session.run(cyph)
        print("Bob's friends are:")
        for rec in result:
            for friend in rec.values():
                print(friend['first_name'], friend['last_name'])

        log.info("Setting up Marie's friends")

        for first, last in [("Mary", "Evans"),
                            ("Alice", "Cooper"),
                            ('Fred', 'Barnes'),
                            ]:
            cypher = """
              MATCH (p1:Person {first_name:'Marie', last_name:'Curie'})
              CREATE (p1)-[friend:FRIEND]->(p2:Person {first_name:'%s', last_name:'%s'})
              RETURN p1
            """ % (first, last)

            session.run(cypher)

        print("Step 6: Find all of Marie's friends?")
        cyph = """
          MATCH (marie {first_name:'Marie', last_name:'Curie'})
                -[:FRIEND]->(friends)
          RETURN friends
          """
        result = session.run(cyph)
        print("\nMarie's friends are:")
        for rec in result:
            for friend in rec.values():
                print(friend['first_name'], friend['last_name'])
