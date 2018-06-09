# simple.py


import logging
import logging.handlers
from time import strftime

format = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"
sysformat = "%(filename)s:%(lineno)-3d %(levelname)s %(message)s"

formatter = logging.Formatter(format)
sysformatter = logging.Formatter(sysformat)

file_handler = logging.FileHandler(strftime('mylog_%Y_%m_%d.log'))
file_handler.setLevel(logging.WARNING)
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

sys_handler = logging.handlers.SysLogHandler(address=('localhost', 514))
sys_handler.setLevel(logging.ERROR)
sys_handler.setFormatter(sysformatter)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)
logger.addHandler(console_handler)
logger.addHandler(sys_handler)



def my_fun(n):
    for i in range(0, n):
        logging.debug(i)
        if i == 50:
            logging.warning("The value of i is 50.")
        try:
            i / (50 - i)
        except ZeroDivisionError:
            logging.error("Tried to divide by zero. Var i was {}."
                          " Recovered gracefully.".format(i))


if __name__ == "__main__":

    my_fun(100)