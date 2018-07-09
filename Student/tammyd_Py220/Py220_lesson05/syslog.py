#syslog.py

import logging, sys
import logging.handlers

log = logging.getLogger(__name__)

log.setLevel(logging.DEBUG)

handler = logging.handlers.SysLogHandler(address="/var/run/syslog")

formatter = logging.Formatter('%(module)s.%(funcName)s: %(message)s')

handler.setFormatter(formatter)

log.addHandler(handler)

def hello():
    log.debug('Hello from Python!!! This is a DEBUG message.')
    log.critical('Hello from Python!!! This is a CRITICAL message.')

if __name__ == "__main__":
    hello()