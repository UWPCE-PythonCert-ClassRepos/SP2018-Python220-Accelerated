#simple.py
import logging
from logging.handlers import SysLogHandler
from datetime import date

format = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"
format2 = "%(lineno)-3d %(levelname)s %(message)s"
current_date = str(date.today())

formatter = logging.Formatter(format)
formatter2 = logging.Formatter(format2)

file_handler = logging.FileHandler('{}.log'.format(current_date))
file_handler.setLevel(logging.WARNING)           
file_handler.setFormatter(formatter)

syslog_handler = SysLogHandler(address=("127.0.0.1", 514))
syslog_handler.setLevel(logging.ERROR)           
syslog_handler.setFormatter(formatter2)

console_handler = logging.StreamHandler()        
console_handler.setLevel(logging.DEBUG)          
console_handler.setFormatter(formatter)          

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)                   
logger.addHandler(file_handler)
logger.addHandler(syslog_handler)
logger.addHandler(console_handler)              

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


# output for terminal running pysyslog.py:
# $ python pysyslog.py
# 127.0.0.1 :  b'<11>39  ERROR Tried to divide by zero. Var i was 50. Recovered gr
# acefully.\x00'

