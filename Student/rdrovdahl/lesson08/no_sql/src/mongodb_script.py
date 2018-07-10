"""
    mongodb example
"""

import pprint
import login_database
import utilities

log = utilities.configure_logger('default', '../logs/mongodb_script.log')


def run_example(furniture_items):
    """
    mongodb data manipulation
    """

    with login_database.login_mongodb_cloud() as client:
        log.info('Step 1: We are going to use a database called dev')
        log.info('But if it doesnt exist mongodb creates it')
        db = client['dev']

        log.info('And in that database use a collection called furniture')
        log.info('If it doesnt exist mongodb creates it')

        furniture = db['furniture']

        log.info('Step 2: Now we add data from the dictionary above')
        furniture.insert_many(furniture_items)

        log.info('Step 3: Find the products that are described as plastic')
        query = {'description': 'Plastic'}
        results = furniture.find_one(query)

        log.info('Step 4: Print the plastic products')
        print('Plastic products')
        pprint.pprint(results)

        log.info('Step 4a-1: Print all the couches')
        print('All the couches:')
        cursor = furniture.find({'product_type': 'couch'})
        for doc in cursor:
            pprint.pprint(doc)

        log.info('Step 4a-2: Print all the red items')
        print('All the red items:')
        cursor = furniture.find({'product_color': 'red'})
        for doc in cursor:
            pprint.pprint(doc)


        log.info('Step 4b: Check for couches that are blue')
        query = {"$and": [{"product_type": "couch"}, {"product_color": "blue"}]}
        results = furniture.find_one(query)
        pprint.pprint(results)


        log.info('Step 5: Delete all blue couches')
        furniture.remove(query)

        log.info('Step 6: Check it is deleted with a query and print')
        results = furniture.find_one(query)
        print('The blue couch is deleted, print should show none:')
        pprint.pprint(results)

        log.info(
            'Step 7: Find multiple documents, iterate though the results and print')

        cursor = furniture.find({'monthly_rental_cost': {'$gte': 15.00}}).sort('monthly_rental_cost', 1)
        print('Results of search')
        log.info('Notice how we parse out the data from the document')

        for doc in cursor:
            print(f"Cost: {doc['monthly_rental_cost']} product name: {doc['product_type']} Stock: {doc['in_stock_quantity']}")


        log.info('Step 7a: add new documents to the database')
        new_furniture_items = [{'product_type': 'dresser',
                                'product_color': 'black',
                                'description': 'rustic dresser',
                                'monthly_rental_cost': 10.00,
                                'in_stock_quantity': 2,
                                'number_of_drawers': 6},
                               {'product_type': 'bed',
                                'product_color': 'black',
                                'description': 'modern bed',
                                'monthly_rental_cost': 25.00,
                                'in_stock_quantity': 5,
                                'size': 'king'}]
        furniture.insert_many(new_furniture_items)

        log.info('Step 7b: Validate new documents made it into the database')
        print('query and print new items from database')
        query = {"$and": [{"product_type": "dresser"}, {"product_color": "black"}]}
        results = furniture.find_one(query)
        pprint.pprint(results)

        query = {"$and": [{"product_type": "bed"}, {"product_color": "black"}]}
        results = furniture.find_one(query)
        pprint.pprint(results)

        log.info('Step 8: Delete the collection so we can start over')
        db.drop_collection('furniture')
