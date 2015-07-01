from __future__ import print_function
import logging

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logging.basicConfig(level=logging.WARNING)

    logging.debug('this message is not formatted; value=%s', 'value')

    logging.debug('this message is not formatted; value=%s' % ('value', ))


