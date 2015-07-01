import logging

def truncate(obj, nlen):
    """ Convert 'obj' to string and truncate if greater than length"""
    str_value = str(obj)
    if len(str_value) > nlen:
        return str_value[:nlen-3] + '...'
    return str_value

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    long_string = 'A' * 2000
    logging.debug('something happened with value=%s', long_string)

    # Truncate result (no ellipses)
    logging.debug('something happened with value=%.10s', long_string)

    # Create a large list
    big_list = [1] * 2000

    # Log the full list
    logging.debug('something happened with the list=%s', big_list)

    # Truncate result (with ellipses)
    logging.debug('something happened with the list=%s', big_list)
