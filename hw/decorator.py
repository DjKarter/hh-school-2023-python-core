import time
from datetime import datetime


def logger(function):
    def wrapped(*args):
        start_time = datetime.now()
        res = function(*args)
        print(f"\tMethod started at {start_time} and now is {datetime.now()}")
        return res
    return wrapped
