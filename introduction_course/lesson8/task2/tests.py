from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_window():
    window = get_answer_placeholders()[0]
    if "my_object" in window and "variable1" in window:
        passed()
    else:
        failed("Access 'variable1' using my_object.variable1")

def test_window1():
    window = get_answer_placeholders()[0]
    if "my_object " in window or "my_object." in window:
        passed()
    else:
        failed("Access 'variable1' using my_object.variable1")

if __name__ == '__main__':
    run_common_tests()
    test_window()
    test_window1()
