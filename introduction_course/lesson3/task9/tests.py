from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_value():
    window = get_answer_placeholders()[0]

    if "monty_python.upper()" in window:
        passed()
    else:
        failed("Use upper() method")

if __name__ == '__main__':
    run_common_tests()
    test_value()

