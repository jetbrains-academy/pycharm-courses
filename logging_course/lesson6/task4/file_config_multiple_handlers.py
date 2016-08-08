import logging
import logging.config

config = """
[loggers]
keys=root

[formatters]
keys=formatter1

[handlers]
keys=handler1, file

[formatter_formatter1]
format=%(asctime)s %(levelname)s %(message)s

[handler_handler1]
class=StreamHandler
args=()
formatter=formatter1

[handler_file]
class=FileHandler
args=("../../Sandbox/file_config_example.log", )
formatter=formatter1

[logger_root]
handlers=handler1, file
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
