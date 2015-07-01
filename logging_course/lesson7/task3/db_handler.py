from __future__ import print_function
import logging
import logging.config
import datetime
import sqlite3 as sqlite


class DatabaseHandler(logging.Handler):
    """ Store log records in a sqlite database.
    """
    def __init__(self, filename):
        super(DatabaseHandler, self).__init__()
        self.db = sqlite.connect(filename)
        try:
            self.db.execute(
                        "CREATE TABLE logger(record_id INTEGER PRIMARY KEY, name TEXT," \
                        "asctime TEXT, level TEXT, funcName TEXT, lineno INTEGER," \
                        "module TEXT, message TEXT);")
            self.db.commit()

        except sqlite.OperationalError as e:
            logging.info('database filename=%s already exists', filename)


    def insert the method name used by a handler to output log records(self, record):
        if self.db:
            timestring = datetime.datetime.utcfromtimestamp(record.created).isoformat() + 'Z'
            message = record.msg % record.args

            self.acquire()
            try:
                self.db.execute("INSERT INTO logger(name, asctime, level, funcName, lineno, module, message) " \
                    "VALUES(?, ?, ?, ?, ?, ?, ?);",
                    (record.name, timestring, record.levelname, record.funcName, record.lineno, record.module, message))
                self.db.commit()
            finally:
                self.release()

    def close(self):
        self.db.close()
        self.db = None
        super(DatabaseHandler, self).close()


if __name__ == '__main__':
    db_filename = '../../Sandbox/log.db'

    log_config = {
        'version': 1,
        'handlers': {
            'db': {
                'class': 'db_handler.DatabaseHandler',
                'filename': db_filename
            }
        },
        'root': {
            'handlers': ['db'],
            'level': 'DEBUG'
        }
    }


    logging.config.dictConfig(log_config)
    logging.debug('Configured logging to database filename=%s', db_filename)

    logging.warn('root logger warning message')
    logging.debug('Connecting to database to read warning counts')

    db = sqlite.connect(db_filename)
    result = db.execute('select count(*) from logger where level="WARNING"')
    print('Number of WARNING log messages in database is %s' % result.fetchone()[0])

    result = db.execute('select count(*) from logger where level="DEBUG"')
    print('Number of DEBUG log messages in database is %s' % result.fetchone()[0])
