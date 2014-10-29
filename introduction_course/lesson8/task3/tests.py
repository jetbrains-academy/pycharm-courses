from test_helper import run_common_tests, get_answer_placeholders, passed, failed


def test_window():
    window = get_answer_placeholders()[0]
    if "Car" in window and "(" in window and ")" in window:
        passed()
    else:
        failed("Create new car using Car()")


def test_window2():
    window = get_answer_placeholders()[1]
    if "car2" in window and "color" in window:
        passed()
    else:
        failed("Change color using car2.color = ")


if __name__ == '__main__':
    run_common_tests()
    test_window()
    test_window2()