import logging

logger = logging.getLogger(__name__)

class FirstClass():
    def __init__(self):
        self.log = logging.getLogger(__name__ + '.first_class')

    def do_something(self):
        self.log.debug('FirstClass do_something() called')


class SecondClass():
    def __init__(self):
        self.log = logging.getLogger(__name__ + '.second_class')

    def do_something(self):
        self.log.debug('SecondClass do_something() called')

if __name__ == '__main__':
    logging.basicConfig(level=logging.WARNING)

    logger.debug('module scope log output')

    first = FirstClass()
    first.do_something()

    second = SecondClass()
    second.do_something()

    first_logger = logging.getLogger(__name__ + 'first class logger specific name')
    set the logging level to DEBUG
    first.do_something()
    second.do_something()


