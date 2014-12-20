from test_helper import run_common_tests, get_answer_placeholders, passed, failed, get_file_output


def test_window():
    window = get_answer_placeholders()[0]
    if "Car" in window and "(" in window and ")" in window:
        passed()
    else:
        failed("Create a new car using Car()")


def test_window2():
    window = get_answer_placeholders()[1]
    output = get_file_output()
    if len(output) > 1 and output[1] == "This is a red car.":
        passed()
    else:
        failed("Change color using assignment to the car2.color")


if __name__ == '__main__':
    run_common_tests()
    test_window()
    test_window2()
