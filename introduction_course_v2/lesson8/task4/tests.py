from test_helper import run_common_tests, get_answer_placeholders, passed, failed


def test_window():
    window = get_answer_placeholders()[0]
    if "self" in window and "amount" in window:
        passed()
    else:
        failed("Access the current variable of the class using self.current")

def test_window2():
    window = get_answer_placeholders()[0]
    if "amount" in window:
        passed()
    else:
        failed("Add the value of 'amount' to self.current")

def test_window3():
    window = get_answer_placeholders()[0]
    if "+=" in window or ("+" in window and "=" in window):
        passed()
    else:
        failed("Add amount value to self.current")

if __name__ == '__main__':
    run_common_tests()
    test_window()
    test_window2()
    test_window3()