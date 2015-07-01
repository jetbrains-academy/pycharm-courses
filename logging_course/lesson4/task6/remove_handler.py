import logging

def setup_loggers():
    stream_handler = logging.StreamHandler()
    fmt = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    stream_handler.setFormatter(fmt)

    root = logging.getLogger()
    root.addHandler(stream_handler)
    #root.setLevel(logging.DEBUG)

    b_log = logging.getLogger('A.B')
    b_log.addHandler(stream_handler)


if __name__ == '__main__':
    setup_loggers()

    c_log = logging.getLogger('A.B.C')
    c_log.warn('This message should be output once to console (but is output twice instead)')

    b_log = logging.getLogger(enter the logger name)

    # Remove all handlers attached to logger
    while len(b_log.handlers):
        handler = b_log.handlers[0]
        insert code to remove handler from A.B logger

    c_log.warn('This message should be output once to console')
