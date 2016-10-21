from test_helper import run_common_tests, passed, failed, import_task_file, get_answer_placeholders


def test_value():
    file = import_task_file()
    if hasattr(file, "ten_of_hellos") and file.ten_of_hellos == "hellohellohellohellohellohellohellohellohellohello":
        passed()
    else:
        failed("Use multiplication")

def test_window():
    window = get_answer_placeholders()[0]
    if "*" in window:
        passed()
    else:
        failed("Use multiplication")

if __name__ == '__main__':
    run_common_tests("You should modify the file")

    test_value()
    test_window()
