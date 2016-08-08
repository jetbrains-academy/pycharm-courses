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
                'handlers': ['console', ]
            }
        },
        'disable_existing_loggers': False
    }

    logging.config.dictConfig(log_config)

    logger.warn('This is a warning')
    logger.debug('test')

    logging.root.warn('This is a root logger warning')
