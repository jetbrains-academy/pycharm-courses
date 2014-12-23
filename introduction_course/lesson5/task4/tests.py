from test_helper import run_common_tests, get_answer_placeholders, passed, failed


def test_window1():
    window = get_answer_placeholders()[0]
    if "John" in window and "if " in window:
        if "==" in window or "is" in window:
            passed()
        else:
            failed("Check equality")
    else:
        failed("Use if keyword")


def test_window2():
    window = get_answer_placeholders()[1]
    if "else" in window:
        passed()
    else:
        failed("Use else keyword")


def test_columns():
    windows = get_answer_placeholders()
    if ":" in windows[0] and ":" in windows[1]:
        passed()
    else:
        failed("Don't forget a colon at the end")

if __name__ == '__main__':
    run_common_tests("Use if/else keywords")
    test_window1()
    test_window2()
    test_columns()
