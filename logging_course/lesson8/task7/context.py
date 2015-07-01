import logging

def do_service_lookup(service_address):
    try:
        raise Exception('Connection refused.')

    except:
        logging.exception(enter a message with relevent context)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    do_service_lookup('10.0.0.15')
