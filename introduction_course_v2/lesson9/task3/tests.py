from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_window():
    window = get_answer_placeholders()[0]
    if "from " in window:
        passed()
    else:
        failed("Use hello_world imported from my_module")

if __name__ == '__main__':
    run_common_tests()
    test_window()
