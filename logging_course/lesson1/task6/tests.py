from test_helper import run_common_tests, failed, passed, get_answer_placeholders, check_answers


def test_answer_placeholders():
    answers = [
        ['logger.log(logging.DEBUG,'],
        ['logger.log(logging.DEBUG,'],
        ['logger.log(logging.INFO,'],
        ['logger.log(logging.WARN,', 'logger.log(logging.WARNING,'],
        ['logger.log(logging.DEBUG,'],
        ['logger.log(logging.DEBUG,'],
        ['logger.log(logging.DEBUG,']
    ]

    check_answers(get_answer_placeholders(), answers)


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()

