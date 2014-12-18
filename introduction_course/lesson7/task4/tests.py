from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_window():
    window = get_answer_placeholders()[0]
    if "=" in window:
        passed()
    else:
        failed("Add a default value to the parameter")

def test_window_names():
    window = get_answer_placeholders()[0]
    if "subject" in window and "name" in window:
        passed()
    else:
        failed("Add a default value to the parameter")

if __name__ == '__main__':
    run_common_tests()
    test_window()
    test_window_names()