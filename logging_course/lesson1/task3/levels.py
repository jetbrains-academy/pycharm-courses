from __future__ import print_function
import math
import logging

def get_current_rate(years):
    logging.debug('Fetching current interest rate for %d years' % years)
    rate = 7.5   # Stub external service call
    logging.debug('Service returned interest rate %f' % rate)
    return rate

def get_monthly_payment(principal, years):
    logging.debug('Calling mortgage calculator')

    if years > 50:
        write_a_warning_message_to_logging

    mon_rate = get_current_rate(years)/1200
    payments = years * 12
    logging.debug('Number of monthly payments %d' % payments)
    result = principal * (mon_rate/(1-math.pow((1+mon_rate), -payments)))

    logging.debug('Calculated result is %f' % result)
    logging.debug('Leaving mortgage calculator')
    return result

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    payment = get_monthly_payment(100000, 30)
    print('Monthly payment is %f' % payment)
