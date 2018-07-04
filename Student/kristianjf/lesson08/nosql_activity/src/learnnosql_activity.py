"""

Integrated example for nosql databases

"""

import learn_data
import mongodb_script
import redis_script
import neo4j_script
import simple_script_activity
import utilities


def showoff_databases_activity():
    """
    Here we illustrate basic interaction with nosql databases
    """

    log = utilities.configure_logger('default', '../logs/nosql_dev.log')

    log.info("Mongodb example to use data from Furniture module, so get it")
    furniture = learn_data.get_furniture_data()

    mongodb_script.run_example_activity(furniture)

    log.info("Other databases use data embedded in the modules")

    redis_script.run_example_activity()
    neo4j_script.run_example_activity()
    simple_script_activity.run_pickle_activity()


if __name__ == '__main__':
    """
    orchestrate nosql examples
    """

    showoff_databases_activity()
