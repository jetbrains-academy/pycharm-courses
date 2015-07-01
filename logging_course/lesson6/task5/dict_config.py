import logging
import logging.config

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    log_config = {
        'version': 1,
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'formatter1',
                'stream': 'ext://sys.stdout'
            }

        },
        'formatters': {
            'formatter1': {
                'format': '%(asctime)s - %(levelname)s - %(message)s'
            }
        },
        'loggers': {
            '': {
                'level': 'DEBUG',
                'handlers': ['insert name of stream handler object key', ]
            }
        }
    }

    logging.config.dictConfig(pass the dict object containing log configuration)

    logger.warn('This is a warning')
    logger.debug('test')

    logging.root.warn('This is a root logger warning')