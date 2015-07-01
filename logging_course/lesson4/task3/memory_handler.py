from __future__ import print_function
import math
import logging
import logging.handlers

logger = logging.getLogger('mortgage')

def get_current_rate(years):
    logger.debug('Fetching current interest rate for %d years', years)
    rate = 5.3   # Stub external service call
    logger.debug('Service returned interest rate %f', rate)
    return rate

def get_monthly_payment(principal, years):
    logger.info('Calling mortgage calculator')

    if years > 50:
        logger.warn('Term greater than 50 years')

    result = None
    try:
        mon_rate = get_current_rate(years)/1200
        payments = years * 12
        logger.debug('Number of monthly payments %d', payments)
        result = principal * (mon_rate/(1-math.pow((1+mon_rate), -payments)))

        logger.debug('Calculated result is %f', result)
    except:
        logger.exception('caught exception')

    logger.debug('Leaving mortgage calculator')
    return result

if __name__ == '__main__':

    log_filename = '../../Sandbox/memory_handler.log'
    file_handler = logging.FileHandler(log_filename, mode='w')

    fmt = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    file_handler.setFormatter(fmt)

    memory_handler = logging.handlers.MemoryHandler(capacity=2, target=use the FileHandler object)

    root_logger = logging.getLogger()
    root_logger.addHandler(memory_handler)
    root_logger.setLevel(logging.DEBUG)

    payment = get_monthly_payment(100000, 0)
    print('Monthly payment is %s' % payment)

    # Remove file handler target to prevent logging.shutdown() from explicitly
    # flushing all handlers, causing any recent DEBUG output to be written
    # to the FileHandler.
    memory_handler.setTarget(None)
