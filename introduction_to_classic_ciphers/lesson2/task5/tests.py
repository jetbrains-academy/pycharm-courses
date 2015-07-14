from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()

    if placeholders[0] == '%' and placeholders[1] == '10':
        passed()
    else:
        print placeholders
        failed(message='Please try again.')

if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()


