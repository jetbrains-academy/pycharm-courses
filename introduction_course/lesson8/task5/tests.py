from test_helper import run_common_tests, get_answer_placeholders, passed, failed


def test_window():
    window = get_answer_placeholders()[0]
    if "color" in window:
        passed()
    else:
        failed("Add a color parameter")


def test_window1():
    window = get_answer_placeholders()[0]
    if "self" in window:
        passed()
    else:
        failed("Don't forget about the self parameter")

if __name__ == '__main__':
    run_common_tests()
    test_window()
    test_window1()
