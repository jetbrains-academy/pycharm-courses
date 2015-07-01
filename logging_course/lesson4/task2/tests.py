from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0].replace('"', "'")
    if placeholder == "'S'" or placeholder == "'s'":
        passed()
    else:
        failed()

    placeholder = placeholders[1]
    if placeholder == "2":
        passed()
    else:
        failed()

if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()


