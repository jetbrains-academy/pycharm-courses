from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_column():
    window = get_answer_placeholders()[0]
    if ":" in window:
        passed()
    else:
        failed("Don't forget about column at the end")


def test_window():
    window = get_answer_placeholders()[0]
    if "while " in window:
        passed()
    else:
        failed("Use while loop to iterate")

def test_window1():
    window = get_answer_placeholders()[0]
    if "number" in window:
        passed()
    else:
        failed("Use 'number' variable in while condition")


def test_window2():
    window = get_answer_placeholders()[0]
    if "<" in window and "10" in window:
        passed()
    else:
        failed("Check that 'number' is strictly less than 10 in condition")


if __name__ == '__main__':
    run_common_tests()
    test_window()
    test_window1()
    test_window2()
    test_column()