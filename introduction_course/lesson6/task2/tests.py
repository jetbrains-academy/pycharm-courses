from test_helper import run_common_tests, failed, passed, get_answer_placeholders, import_task_file


def test_value():
    file = import_task_file()
    if hasattr(file, "length") and file.length == 13:
        passed()
    else:
        failed("Count again")

def test_window():
    window = get_answer_placeholders()[0]
    if "for " in window:
        passed()
    else:
        failed("Use a for loop to iterate over the hello_world string")


if __name__ == '__main__':
    run_common_tests()
    test_window()
    test_value()