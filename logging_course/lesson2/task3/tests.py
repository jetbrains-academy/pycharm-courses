from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if placeholder == "%(asctime)s %(levelname)s %(module)s %(funcName)s %(message)s":
        passed()
    else:
        failed('Sorry, that is not correct. Check the Hint for the correct answer.')


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()


