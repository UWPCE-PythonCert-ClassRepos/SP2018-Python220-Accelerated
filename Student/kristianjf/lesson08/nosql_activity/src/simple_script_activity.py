"""
pickle etc
"""

import pickle

import pprint
import utilities

log = utilities.configure_logger('default', '../logs/mongodb_script.log')

def run_pickle_activity():
    """
    Write and read with pickle
    """
    log.info("\n\n====")
    log.info('Step 1: Demonstrate persistence with pickle')
    log.info('Create some data (at least 10 rows with about 5 fields in each).')
    lakers_lineup = [
        {
            'name': 'JaVale McGee',
            'age': 30,
            'position': 'center',
            'ppg': 4.8,
            'salary': 2393887
        },
        {
            'product': 'Kyle Kuzma',
            'age': 22,
            'position': 'power forward',
            'ppg': 16.1,
            'salary': 1689840
        },
        {
            'product': 'Brandon Ingram',
            'age': 20,
            'position': 'small forward',
            'ppg': 16.1,
            'salary': 5757120
        },
        {
            'product': 'LeBron James',
            'age': 33,
            'position': 'shooting guard',
            'ppg': 27.5,
            'salary': 35600000
        },
        {
            'product': 'Rajon Rondo',
            'age': 32,
            'position': 'point guard',
            'ppg': 8.3,
            'salary': 9000000
        },
        {
            'name': 'Mo Wagner',
            'age': 21,
            'position': 'center',
            'ppg': 'N/A',
            'salary': 1764240
        },
        {
            'product': 'Isaac Bonga',
            'age': 18,
            'position': 'power forward',
            'ppg': 'N/A',
            'salary': 'N/A'
        },
        {
            'product': 'Luol Deng',
            'age': 33,
            'position': 'small forward',
            'ppg': 7.6,
            'salary': 18000000
        },
        {
            'product': 'Kentavious Caldwell-Pope',
            'age': 25,
            'position': 'shooting guard',
            'ppg': 13.4,
            'salary': 18000000
        },
        {
            'product': 'Lonzo Ball',
            'age': 20,
            'position': 'point guard',
            'ppg': 10.2,
            'salary': 7461960
        }
    ]
    pickle.dump(lakers_lineup, open('../data/data.pkl', 'wb'))

    log.info('Step 2: Now read it back from the pickle file')
    read_data = pickle.load(open('../data/data.pkl', 'rb'))
    log.info('Step 3: Show that the write and read were successful')
    assert read_data == lakers_lineup
    log.info("and print the data")
    pprint.pprint(read_data)
