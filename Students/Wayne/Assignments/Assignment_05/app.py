import logging
import socket
from logging.handlers import SysLogHandler

logger = logging.getLogger()
logger.setLevel(logging.INFO)

syslog = SysLogHandler(address=('127.0.0.1', 9999))
formatter = logging.Formatter(
    '%(asctime)s'
    'FAKE_APP_NAME: %(message)s',
    datefmt='%b %d %H:%M:%S'
)

syslog.setFormatter(formatter)
logger.addHandler(syslog)

logger.info("This is a message")
