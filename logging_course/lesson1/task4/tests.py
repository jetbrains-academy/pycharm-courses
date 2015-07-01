from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    for placeholder in placeholders:
        if placeholder != 'logger':
            failed('Sorry, that is not correct. Please replace all instances of "logging" with "logger"')
            return
    passed()


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()


