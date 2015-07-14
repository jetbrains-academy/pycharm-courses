from test_helper import run_common_tests, failed, passed, get_answer_placeholders

def test_answer_placeholders():
    placeholders = get_answer_placeholders()

    if placeholders[0][1:-1] == 'World' and (placeholders[1] == 'MESSAGE' or placeholders[1][1:-1] == 'Hello, World'):
        passed()
    else:
        failed(message = 'Please try again.')

if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()
