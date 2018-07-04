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

        log.info('Step 5: Delete the blue couch (actually deletes all blue couches)')
        furniture.remove({"product": {"$eq": "Blue couch"}})

        log.info('Step 6: Check it is deleted with a query and print')
        query = {'product': 'Blue couch'}
        results = furniture.find_one(query)
        print('The blue couch is deleted, print should show none:')
        pprint.pprint(results)

        log.info(
            'Step 7: Find multiple documents, iterate though the results and print')

        cursor = furniture.find({'monthly_rental_cost': {'$gte': 15.00}}).sort('monthly_rental_cost', 1)
        print('Results of search')
        log.info('Notice how we parse out the data from the document')

        for doc in cursor:
            print(f"Cost: {doc['monthly_rental_cost']} product name: {doc['product']} Stock: {doc['in_stock_quantity']}")

        log.info('Step 8: Delete the collection so we can start over')
        db.drop_collection('furniture')

def run_example_activity(furniture_items):
    """
    mongodb data manipulation -- activity 8
    """
    with login_database.login_mongodb_cloud() as client:
        log.info('Step 1: We are going to use a database called dev')
        log.info('But if it doesnt exist mongodb creates it')
        db = client['dev']

        log.info('And in that database use a collection called furniture')
        log.info('If it doesnt exist mongodb creates it')

        furniture = db['furniture']

        '''Add some extra furniture items for mongodb.
        And while you're doing that, separate the product field in to 2 fields;
        one called product type, one called color.
        Start by amending the data,
        then change the Mongodb program to store and retrieve using these new values.
        '''
        log.info('Amending furuniture items with "some extra furniture items"')
        add_furniture_items = [
            {
                'product': 'Red Chair',
                'description': 'Plastic',
                'monthly_rental_cost': 2.00,
                'in_stock_quantity': 10
            },
            {
                'product': 'Blue Chair',
                'description': 'Plastic',
                'monthly_rental_cost': 3.00,
                'in_stock_quantity': 25
            }
        ]
        furniture_items.extend(add_furniture_items)

        log.info('Separating the product field into 2 fields; product type and color.')
        colors = ['Red', 'Blue', 'White']
        for entry in furniture_items:
            for word in entry['product'].split():
                if word in colors:
                    entry['color'] = word
                    break
                else:
                    entry['color'] = 'Undefined'
            entry['product type'] = ' '.join([x for x in entry['product'].split() \
            if x not in colors]).capitalize()
            del entry['product']

        log.info('Step 2: Now we add data from the dictionary above')
        furniture.insert_many(furniture_items)

        log.info('Step 3.1: Retrieve and print just the red products.')
        query = {'color': 'Red'}
        results = furniture.find(query)
        for entry in results:
            pprint.pprint(entry)

        log.info('Step 3.2: Retrieve and print just the couches.')
        query = {'product type': 'Couch'}
        results = furniture.find(query)
        for entry in results:
            pprint.pprint(entry)

        log.info('Step 4: Delete the collection so we can start over')
        db.drop_collection('furniture')
