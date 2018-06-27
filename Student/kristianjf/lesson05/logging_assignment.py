#!/usr/bin/env python3
import logging, logging.handlers

'''To complete this assignment, modify simple.py to satisfy the following goals:

You want ALL log messages logged to the console.
The format of these messages should include the current time.
You want WARNING and higher messages logged to a file named { todays-date }.log.
    The format of these messages should include the current time.
You want ERROR and higher messages logged to a syslog server.
    The syslog server will be appending its own time stamps to the messages that it receives,
    so DO NOT include the current time in the format of the log messages that you send
    to the server.
'''

format_console = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"
format_syslog = "%(filename)s:%(lineno)-3d %(levelname)s %(message)s"
formatter_console = logging.Formatter(format_console)
formatter_syslog = logging.Formatter(format_syslog)

file_handler = logging.FileHandler('mylog.log')
file_handler.setLevel(logging.WARNING)
file_handler.setFormatter(formatter_console)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter_console)

syslog_handler = logging.handlers.DatagramHandler('127.0.0.1', 514)
syslog_handler.setLevel(logging.ERROR)
syslog_handler.setFormatter(formatter_syslog)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)
logger.addHandler(console_handler)
logger.addHandler(syslog_handler)

def my_fun(n):
    for i in range(0, n):
        logging.debug(i)
        if i == 50:
            logging.warning("The value of i is 50.")
        try:
            i / (50 - i)
        except ZeroDivisionError:
            logging.error("Tried to divide by zero. Var i was {}. Recovered gracefully.".format(i))

if __name__ == "__main__":
    my_fun(100)
