from test_helper import run_common_tests, get_answer_placeholders, passed, failed


def test_window():
    window = get_answer_placeholders()[0]
    if "a" in window:
        passed()
    else:
        failed("Use 'a' modifier to append lines to the end of file")


def test_window1():
    window = get_answer_placeholders()[1]
    if "write" in window:
        passed()
    else:
        failed("Use 'write' method")


def test_window3():
    window = get_answer_placeholders()[2]
    if "f" in window and "close" in window and "(" in window:
        passed()
    else:
        failed("Call 'close' method")

if __name__ == '__main__':
    run_common_tests()
    test_window()
    test_window1()
    test_window3()