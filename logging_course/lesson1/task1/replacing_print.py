from __future__ import print_function
import math
import logging

def get_current_rate(years):
    print('Fetching current interest rate for %d years' % years)
    rate = 7.5   # Stub external service call
    print('Service returned interest rate %f' % rate)
    return rate

def get_monthly_payment(principal, years):
    print('Calling mortgage calculator')

    mon_rate = get_current_rate(years)/1200
    payments = years * 12
    print('Number of monthly payments %d' % payments)
    result = principal * (mon_rate/(1-math.pow((1+mon_rate), -payments)))

    print('Calculated result is %f' % result)
    print('Leaving mortgage calculator')
    return result

if __name__ == '__main__':
    payment = get_monthly_payment(100000, 30)
    print('Monthly payment is %f' % payment)
