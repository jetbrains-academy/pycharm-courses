from test_helper import run_common_tests, failed, passed, get_answer_placeholders

MESSAGE = 'Hello, World! Hello!'

def test_answer_placeholders():
    placeholders = get_answer_placeholders()

    if (placeholders[0] == 'MESSAGE' or placeholders[0] == MESSAGE) \
            and (placeholders[2] == 'MESSAGE' or placeholders[2] == MESSAGE) \
            and placeholders[1][1:-1] == 'World' \
            and placeholders[3][1:-1] == 'Hello':  # slice [1:-1] to omit the starting and trailing ' or "
        passed()
    else:
        print placeholders
        failed(message='Please try again.')

if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()


