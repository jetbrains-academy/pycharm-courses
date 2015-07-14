from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()

    if placeholders[0] == '25' and placeholders[1] == 'random_alphabet_index':
        passed()
    else:
        failed(message='Please try again')


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()


