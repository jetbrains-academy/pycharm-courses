from test_helper import run_common_tests, passed, failed, get_answer_placeholders, import_task_file, get_file_output


def test_window1():
    windows = get_answer_placeholders()

    if windows[1].isdigit():
        passed()
        return
    else:
        output = get_file_output()
        if len(output) > 1:
            import re

            p = re.compile("I'm (\d*) years old")
            if p.match(output[1]) is not None:
                passed()
                return
    failed("Print digit")


def test_window():
    windows = get_answer_placeholders()

    if windows[0] == "%d":
        passed()
    else:
        failed("Use %d special symbol")


if __name__ == '__main__':
    run_common_tests()
    test_window()
    test_window1()
