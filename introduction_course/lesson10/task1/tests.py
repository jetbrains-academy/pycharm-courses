from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_window():
    window = get_answer_placeholders("read_file.py")[0]
    if "print" in window and "line" in window:
        passed()
    else:
        failed("Use print function")


def test_window2():
    window = get_answer_placeholders("read_file.py")[1]
    if "f1" in window and "readline" in window:
        passed()
    else:
        failed("Use 'readline' method")


def test_window3():
    window = get_answer_placeholders("read_file.py")[2]
    if "f1" in window and "close" in window and "(" in window:
        passed()
    else:
        failed("Call 'close' method")

if __name__ == '__main__':
    run_common_tests()
    test_window()
    test_window2()
    test_window3()