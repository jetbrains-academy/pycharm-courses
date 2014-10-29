from test_helper import run_common_tests, passed, failed, get_answer_placeholders


def test_window1():
    windows = get_answer_placeholders()

    if windows[1].isdigit():
        passed()
    else:
        failed("Print digit")

def test_window():
    windows = get_answer_placeholders()

    if windows[0] == "%d":
        passed()
    else:
        failed("Use %d special symbol")


if __name__ == '__main__':
    run_common_tests()
    test_window()
    test_window1()

