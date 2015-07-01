from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if placeholder == "info":
        passed()
    else:
        failed('Sorry, that is not correct. Please use the info() method.')

    if placeholders[1].startswith('logging.warn'):
        passed()
    else:
        failed('Sorry, that is not correct. Place use the warn() method.')

if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()


