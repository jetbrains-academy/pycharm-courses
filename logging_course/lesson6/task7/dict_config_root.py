import logging
import logging.config

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    log_config = {
        'version': 1,
        'disable_existing_loggers': False,
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
        'enter name of root logger': {
            'level': 'DEBUG',
            'handlers': ['console', ]
        }
    }

    logging.config.dictConfig(log_config)

    logger.warn('This is a warning')
    logger.debug('test')
