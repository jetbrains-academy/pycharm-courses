import logging
import time
import functools

def logging_decorator(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        logging.debug('Entering %s', f.__name__)
        start = time.time()
        f(*args, **kwargs)
        end = time.time()
        logging.debug('Exiting %s in %-5.2f secs', f.__name__, end-start)

    return wrapper

add our logging decorator do this function
def do_work(timeout):
    # Doing something expensive
    time.sleep(timeout)


if __name__ == '__main__':
    logging.basicConfig(configure the log level to ensure we see the decorator output)
    do_work(5)

