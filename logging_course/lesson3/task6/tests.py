from test_helper import run_common_tests, failed, passed, get_answer_placeholders, check_answers


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    answers = [
        ['setLevel(logging.WARNING)', 'setLevel(logging.WARN)']
    ]
    check_answers(placeholders, answers)


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()


