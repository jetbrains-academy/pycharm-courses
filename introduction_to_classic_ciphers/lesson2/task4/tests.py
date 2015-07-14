from test_helper import run_common_tests, failed, passed, get_answer_placeholders

MESSAGE = 'Hello, World!'


def test_case_one():
    placeholders = get_answer_placeholders()
    if placeholders[0] == '7' and (placeholders[1] == '-1' or placeholders[1] == '12'):
        passed()
    else:
        failed(message = 'At least one of the values for the first task is incorrect. Please try again.')

def test_case_two():
    placeholders = get_answer_placeholders()
    if placeholders[2] == '5' and (placeholders[3] == '6' or placeholders[3] == '-7'):
        passed()
    else:
        failed(message = 'At least one of the values for the second task is incorrect. Please try again.')


if __name__ == '__main__':
    run_common_tests()
    test_case_one()
    test_case_two()