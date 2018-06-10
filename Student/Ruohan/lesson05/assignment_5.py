import logging

format = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"
format_without_time = "%(filename)s:%(lineno)-4d %(levelname)s %(message)s"

formatter_withtime = logging.Formatter(format)
formatter_withouttime = logging.Formatter(format_without_time)

file_handler = logging.FileHandler('mylog.log')
file_handler.setLevel(logging.WARNING)           # Add this line
file_handler.setFormatter(formatter_withtime)

console_handler = logging.StreamHandler()        # Add this line
console_handler.setLevel(logging.DEBUG)          # Add this line
console_handler.setFormatter(formatter_withtime)          # Add this line

server_handler = logging.ServerHandler()        # Add this line
server_handler.setLevel(logging.ERROR)          # Add this line
server_handler.setFormatter(formatter_withouttime)

logger = logging.getLogger()
logger.setLevel(logging.NOTSET)                   # Add this line
logger.addHandler(file_handler)
logger.addHandler(console_handler)               # Add this line

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
