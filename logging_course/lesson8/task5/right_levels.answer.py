import logging

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    user_id = 1001
    ip = '10.0.0.15'
    port = 5555
    account_id = 3551
    version = '1.5.2'

    logging.log(logging.INFO, 'Service restarted - version %s', version)

    logging.log(logging.ERROR, 'Failed to connect to calculator service at ip=%s:%d', ip, port)

    logging.log(logging.INFO, 'Created user account id=%d', user_id)

    logging.log(logging.WARN, 'User entered invalid account id=%d account_id=%d', user_id, account_id)

    logging.log(logging.CRITICAL, 'Could not connect to user database')

    logging.log(logging.DEBUG, 'DB Transaction created for updating user id=%d', user_id)
