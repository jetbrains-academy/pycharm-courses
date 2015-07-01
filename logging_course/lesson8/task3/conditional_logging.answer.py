import logging
import time

logger = logging.getLogger(__name__)

def calculate_expensive_result(timeout):
    time.sleep(timeout)
    return 1


if __name__ == '__main__':
    logging.basicConfig(level=logging.WARNING)

    if logger.isEnabledFor(logging.DEBUG):
        logger.debug('expensive_result=%d', calculate_expensive_result(5))
