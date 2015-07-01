from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0].replace('"', "'")
    if placeholder == "logger = logging.getLogger('mortgage.rate')":
        passed()
    else:
        failed('Sorry, that is not correct. Check the Hint for more help.')


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()


