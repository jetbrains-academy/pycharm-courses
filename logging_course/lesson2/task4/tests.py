from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0].replace('"', "'")
    if placeholder.startswith("logger.exception(") and placeholder.find("'") != -1:
        passed()
    else:
        failed("That is not correct. Be sure to call exception() with a string argument.")


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()


