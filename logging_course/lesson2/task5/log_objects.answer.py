# This example shows logging objects
#

import logging

logger = logging.getLogger('mortgage')

class Mortgage(object):
    def __init__(self, principal, rate, term):
        self.principal = principal
        self.rate = rate
        self.term = term

    def __str__(self):
        return 'Mortgage principal %f for %f years at %f rate' % (
            self.principal, self.term, self.rate)

    def __repr__(self):
        return 'Mortgage(%f, %f, %f)' % (self.principal, self.rate, self.term)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    obj = Mortgage(100000, 4.1, 15)
    logger.debug('Created object: %s', repr(obj))
