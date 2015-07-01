import logging

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    log_filter = logging.Filter('A')

    logger1 = logging.getLogger('A')
    logger1.debug('This is written to log output')

    logger2 = logging.getLogger('A.B')
    logger2.debug('This is written to log output')

    logger3 = logging.getLogger('B')
    add a null handler to logger3
    logger3.propagate = False
    logger3.debug('This is NOT written to log output, because only names start with "B" are allowed by filter')
