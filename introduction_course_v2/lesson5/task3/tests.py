from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_window():
    window = get_answer_placeholders()[0]
    if ":" in window:
        passed()
    else:
        failed("Don't forget a column at the end")


def test_len():
    window = get_answer_placeholders()[0]
    if "len" in window:
        passed()
    elif "not" in window:
        passed()
    else:
        failed("Use len function to check that tasks is empty")


if __name__ == '__main__':
    run_common_tests()
    test_window()
    test_len()