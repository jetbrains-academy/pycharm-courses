from __future__ import print_function
import math
import logging

logger = logging.getLogger('mortgage')

def get_current_rate(years):
    logger.log(logging.DEBUG,'Fetching current interest rate for %d years' % years)
    rate = 5.3   # Stub external service call
    logger.log(logging.DEBUG,'Service returned interest rate %f' % rate)
    return rate

def get_monthly_payment(principal, years):
    logger.log(logging.INFO,"Calling mortgage calculator")

    if years > 50:
        logger.log(logging.WARNING,'Term greater than 50 years')

    mon_rate = get_current_rate(years)/1200
    payments = years * 12
    logger.log(logging.DEBUG,'Number of monthly payments %d' % payments)
    result = principal * (mon_rate/(1-math.pow((1+mon_rate), -payments)))

    logger.log(logging.DEBUG,"Calculated result is %f" % result)
    logger.log(logging.DEBUG,"Leaving mortgage calculator")
    return result

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    payment = get_monthly_payment(100000, 30)
    print('Monthly payment is %f' % payment)
