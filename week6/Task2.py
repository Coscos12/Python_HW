import logging
import time

logging.basicConfig(filename="my_log.log", level=logging.INFO)

def log_time_decorator(func):
    def wrapper(*args, **kwargs):

        start = time.time()
        result = func(*args, **kwargs)
        run_time = time.time()-start
        logging.info(f'Running "{func.__name__}" function with {*args, **kwargs} in {round(run_time,2)} seconds')
        return result
    return wrapper
