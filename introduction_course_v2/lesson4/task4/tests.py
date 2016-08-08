from test_helper import run_common_tests, passed, failed, get_answer_placeholders


def test_window():
    window = get_answer_placeholders()[0]
    if "len(" in window:
        passed()
    else:
        failed("Use len() function")


if __name__ == '__main__':
    run_common_tests("Use len() function")
    test_window()