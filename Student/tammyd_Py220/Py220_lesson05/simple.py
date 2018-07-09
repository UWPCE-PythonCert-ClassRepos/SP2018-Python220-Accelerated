import logging
import logging.handlers
import syslog
from datetime import datetime

format = "%(asctime)s %(filename)s:%(lineno)-4d %(levelname)s %(message)s"  # Add/modify these
# logging.basicConfig(level=logging.WARNING, format=format, filename='mylog.log')                   # two lines

# Create a "formatter" using our format string
formatter_console = logging.Formatter(format)
formatter_syslog = logging.Formatter(format)

# Create a log message handler that sends output to the file 'mylog.log'
file_handler = logging.FileHandler('{}.log'.format(datetime.now()))
# You want WARNING and higher messages logged to a file named { todays-date }.log. The format of these messages should include the current time.
file_handler.setLevel(logging.WARNING)
# Set the formatter for this log message handler to the formatter we created above.
file_handler.setFormatter(formatter_console)


console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter_console)

#The address and port will be '127.0.0.1' and 514, respectively
syslog_handler = logging.handlers.SysLogHandler(address = ("127.0.0.1", 514))
syslog_handler.setFormatter(formatter_syslog)



# Get the "root" logger. More on that below.
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
# Add our file_handler to the "root" logger's handlers.
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

















