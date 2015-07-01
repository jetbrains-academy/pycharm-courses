import logging

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    user_id = 1001
    ip = '10.0.0.15'
    port = 5555
    account_id = 3551
    version = '1.5.2'

    logging.log(logging.enter level name, 'Service restarted - version %s', version)

    logging.log(logging.enter level name, 'Failed to connect to calculator service at ip=%s:%d', ip, port)

    logging.log(logging.enter level name, 'Created user account id=%d', user_id)

    logging.log(logging.enter level name, 'User entered invalid account id=%d account_id=%d', user_id, account_id)

    logging.log(logging.enter level name, 'Could not connect to user database')

    logging.log(logging.enter level name, 'DB Transaction created for updating user id=%d', user_id)
