from __future__ import print_function
import math
import logging

logger = logging.getLogger('mortgage')

def get_current_rate(years):
    create_a_new_logger_instance

    logger.debug('Fetching current interest rate for %d years' % years)
    rate = 5.3   # Stub external service call
    logger.debug('Service returned interest rate %f' % rate)
    return rate

def get_monthly_payment(principal, years):
    logger.info('Calling mortgage calculator')

    if years > 50:
        logger.warn('Term greater than 50 years')

    mon_rate = get_current_rate(years)/1200
    payments = years * 12
    logger.debug('Number of monthly payments %d' % payments)
    result = principal * (mon_rate/(1-math.pow((1+mon_rate), -payments)))

    logger.debug('Calculated result is %f' % result)
    logger.debug('Leaving mortgage calculator')
    return result

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    payment = get_monthly_payment(100000, 30)
    print('Monthly payment is %f' % payment)
