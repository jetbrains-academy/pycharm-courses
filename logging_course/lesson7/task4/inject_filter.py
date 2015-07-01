import logging
import time
import random
import logging.config
import threading

class LogUserInjector(logging.Filter):
    thread_local_data = threading.local()

    def enter the name of the method used to filter records(self, record):
        record.user_id = self.thread_local_data.user_id
        return enter the return value to always allow records to be handled

    @classmethod
    def set_userid(cls, user_id):
        cls.thread_local_data.user_id = user_id


def simulate_user(user_id):
    LogUserInjector.set_userid(user_id)

    logging.debug('user logged_in')
    time.sleep(random.random())
    logging.debug('user performed some activity')
    time.sleep(random.random())
    logging.debug('user logged_out')
    time.sleep(random.random())


if __name__ == '__main__':

    log_config = {
        'version': 1,
        'formatters': {
            'with_uid': {
                'format': '%(levelname)s - %(asctime)s - %(thread)s UID=%(user_id)d - %(message)s'
            }
        },
        'handlers': {
            'stderr': {
                'class': 'logging.StreamHandler',
                'formatter': 'with_uid',
                'filters': ['uid']
            }
        },
        'filters': {
            'uid': {
                '()': LogUserInjector
            }
        },
        'root': {
            'handlers': ['stderr'],
            'level': 'DEBUG'
        }
    }

    logging.config.dictConfig(log_config)

    threads = []
    for user_id in [1, 5, 2, 3]:
        thread = threading.Thread(target=simulate_user, args=(user_id,))
        thread.start()

    for thread in threads:
        thread.join()

