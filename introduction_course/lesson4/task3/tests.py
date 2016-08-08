from test_helper import run_common_tests, failed, passed, import_task_file, get_answer_placeholders


def test_value():
    file = import_task_file()
    if hasattr(file, "animals") and not file.animals:
        passed()
    else:
        failed("Clear animals list")

def test_window():
    window = get_answer_placeholders()[0]
    if "animals" in window:
        passed()
    else:
        failed("Clear animals list")

if __name__ == '__main__':
    run_common_tests("Use assignment to empty list")
    test_window()
    test_value()
