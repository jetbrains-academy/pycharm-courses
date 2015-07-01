import logging
import json
import datetime
import traceback

class JsonFormatter(logging.Formatter):
    def format(self, record):
        if record.exc_info:
            exc = traceback.format_exception(*record.exc_info)
        else:
            exc = None

        return json.dumps({
            'msg': record.msg % record.args,
            'timestamp': datetime.datetime.utcfromtimestamp(record.created).isoformat() + 'Z',
            'func': record.funcName,
            'level': record.levelname,
            'module': record.module,
            'process_id': record.process,
            'thread_id': record.thread,
            'exception': exc
        })

if __name__ == '__main__':
    handler = logging.StreamHandler()

    fmt = JsonFormatter()
    add the formatter to the handler

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    root_logger.addHandler(handler)

    try:
        raise Exception('This is an exception')
    except:
        root_logger.exception('caught exception')

    root_logger.warn('this is a test message')
    root_logger.debug('this request_id=%d name=%s', 1, 'John')


