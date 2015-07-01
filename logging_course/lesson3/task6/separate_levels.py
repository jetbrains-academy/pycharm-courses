from __future__ import print_function
import math
import sys
import logging

logger = logging.getLogger('mortgage')

def get_current_rate(years):
    logging.debug('Fetching current interest rate for %d years', years)
    rate = 5.3   # Stub external service call
    logging.debug('Service returned interest rate %f', rate)
    return rate

def get_monthly_payment(principal, years):
    logging.info('Calling mortgage calculator')

    if years > 50:
        logging.warn('Term greater than 50 years')

    mon_rate = get_current_rate(years)/1200
    payments = years * 12
    logging.debug('Number of monthly payments %d', payments)
    result = principal * (mon_rate/(1-math.pow((1+mon_rate), -payments)))

    logging.debug('Calculated result is %f', result)
    logging.debug('Leaving mortgage calculator')
    return result

if __name__ == '__main__':
    log_filename = '../../Sandbox/separate_levels.log'
    file_handler = logging.FileHandler(log_filename)

    fmt = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    file_handler.setFormatter(fmt)

    root_logger = logging.getLogger()
    root_logger.addHandler(file_handler)

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(fmt)
    stdout_handler.set handler level
    root_logger.addHandler(stdout_handler)

    root_logger.setLevel(logging.DEBUG)

    payment = get_monthly_payment(100000, 80)
    print('Monthly payment is %f' % payment)
