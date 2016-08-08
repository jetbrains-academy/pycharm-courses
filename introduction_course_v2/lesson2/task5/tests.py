from test_helper import run_common_tests, passed, failed, import_task_file, get_answer_placeholders


def test_division():
    file = import_task_file()
    if file.result == 4.5:
        passed()
    else:
        failed("Wrong result")


def test_remainder():
    file = import_task_file()
    if file.remainder == 1.0:
        passed()
    else:
        failed("Wrong remainder")


def test_windows():
    windows = get_answer_placeholders()
    if not "/" in windows[0]:
        failed("Use / operator")
        return
    if not "%" in windows[1]:
        failed("Use % operator")
        return
    if "number" in windows[0] and "number" in windows[1]:
        passed()
    else:
        failed("Use the value stored in the variable \"number\"")


if __name__ == '__main__':
    run_common_tests("Use / and % operators")
    test_windows()
    test_division()
    test_remainder()