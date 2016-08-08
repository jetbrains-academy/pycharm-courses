from test_helper import run_common_tests, failed, passed, get_answer_placeholders, get_file_output


def test_column():
    window = get_answer_placeholders()[0]
    if ":" in window:
        passed()
    else:
        failed("Don't forget a colon at the end")


def test_window():
    window = get_answer_placeholders()[0]
    if "while " in window:
        passed()
    else:
        failed("Use a while loop to iterate")


def test_window1():
    window = get_answer_placeholders()[0]
    if "number" in window:
        passed()
    elif 'square' in window:
        passed()
    else:
        failed("Use 'number' variable in the while condition")


def test_window2():
    window = get_answer_placeholders()[0]
    if "10" in window:
        if "<" in window or "10 >" in window:
            passed()
    elif 'square' in window:
        if "<" and "81" in window:
            passed()
    else:
        failed("Check that 'number' is strictly less than 10 in the condition")


def test_output():
    output = get_file_output()
    if "Finished" not in output:
        failed("Sorry, this answer is wrong")
        return
    border = output.index("Finished")
    user_squares = output[border + 1:]
    user_squares = [x for x in user_squares if x]
    correct_answer = list(map(str, [x * x for x in range(1, 10)]))
    if correct_answer == user_squares:
        passed()
    else:
        failed("Sorry, this answer is wrong")

if __name__ == '__main__':
    run_common_tests()
    test_window()
    test_window1()
    test_window2()
    test_column()
    test_output()
