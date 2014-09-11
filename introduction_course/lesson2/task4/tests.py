from test_helper import run_common_tests, get_task_windows, passed, failed


def test_window():
    window = get_task_windows()[0]
    if "int" in window and "float_number" in window:
        passed()
    else:
        failed("Use int() function")

if __name__ == '__main__':
    run_common_tests()
    test_window()