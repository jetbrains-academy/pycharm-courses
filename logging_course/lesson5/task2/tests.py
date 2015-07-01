from test_helper import run_common_tests, failed, passed, get_answer_placeholders, check_answers


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    try:
        int_value = int(placeholder)
        if int_value > 0:
            passed()
        else:
            failed()

    except ValueError:
        if placeholder == 'True':
            passed()
        else:
            failed()

    placeholder = placeholders[1]
    if placeholder == 'root.addFilter(sanitize_filter)':
        passed()
    else:
        failed()

if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()


