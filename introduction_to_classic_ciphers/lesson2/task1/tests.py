from test_helper import run_common_tests, failed, passed, get_answer_placeholders

def test_answer_placeholders():
    placeholders = get_answer_placeholders()

    if placeholders[0] == placeholders[2]:
        passed()
    else:
        failed()

    if placeholders[1][1:-1] == 'It is snowing.' or placeholders[1] == 'SECOND_MESSAGE':
        passed()
    else:
        failed(message='The string used in the for loop does not match the value of SECOND_MESSAGE')

if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()


