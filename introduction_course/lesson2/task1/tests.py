from test_helper import run_common_tests, failed, passed, import_task_file, get_answer_placeholders


def test_task_window():
    window = get_answer_placeholders()[0]
    if "another value" == window:
      failed("You should redefine the variable 'greetings'")
    else:
      passed()

def test_value():
    file = import_task_file()

    if file.greetings == "greetings":
        failed("You should assign a different value to the variable")
    else:
        passed()

if __name__ == '__main__':
    test_task_window()
    run_common_tests("You should redefine the variable 'greetings'")
    test_value()
