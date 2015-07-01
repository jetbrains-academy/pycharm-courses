from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    if placeholders[0] == "@logging_decorator":
        passed()
    else:
        failed()

    if placeholders[1] == "level=logging.DEBUG":
        passed()
    else:
        failed()


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()


