from test_helper import run_common_tests, failed, passed, get_answer_placeholders, get_file_output


def test_window():
    window = get_answer_placeholders("read_file.py")[0]
    if "print" in window and "line" in window:
        passed()
    else:
        failed("Use print function")


def test_window2():
    default_error = "Use 'readline' method"
    window = get_answer_placeholders("read_file.py")[1]
    output = get_file_output()
    if len(output) > 2 and output[1] == "My first line":
        passed()
        return
    if "print" not in window:
        failed("Don't forget to print the line")
        return
    failed(default_error)


def test_window3():
    window = get_answer_placeholders("read_file.py")[2]
    if "f1" in window and "close" in window and "(" in window:
        passed()
    else:
        failed("Call 'close' method")

if __name__ == '__main__':
    run_common_tests()
    test_window()
    test_window2()
    test_window3()
