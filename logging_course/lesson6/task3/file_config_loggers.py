import logging
import logging.config

config = """
[formatters]
keys=formatter1

[handlers]
keys=handler1

[loggers]
keys=enter root logger instance name

[formatter_formatter1]
format=%(asctime)s %(levelname)s %(message)s

[handler_handler1]
class=StreamHandler
args=()
formatter=formatter1

[logger_enter name of root logger instance]
handlers=enter name of handler instance
level=DEBUG
"""

config_filename = 'logging.ini'

def write_config_file(filename, data):
    with open(filename, 'w') as fp:
        fp.write(data)


if __name__ == '__main__':
    write_config_file(config_filename, config)

    logging.config.fileConfig(config_filename)

    logging.debug('this is a debug message')
    logging.warning('this is a warning message')