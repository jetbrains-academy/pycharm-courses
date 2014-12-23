from test_helper import run_common_tests, passed, failed, get_answer_placeholders


def test_window():
    window = get_answer_placeholders()[0]
    if "phone_book" in window and "values()" in window:
        passed()
    else:
        failed("Use values() method")


if __name__ == '__main__':
    run_common_tests()
    test_window()
