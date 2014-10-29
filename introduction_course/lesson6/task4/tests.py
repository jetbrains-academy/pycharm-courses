from test_helper import run_common_tests, passed, failed, get_answer_placeholders


def test_window():
    window = get_answer_placeholders()[0]
    if "elephant" in window and "animal" in window:
        passed()
    else:
        failed("Use == to check that animal is equal to 'elephant'")



if __name__ == '__main__':
    run_common_tests()
    test_window()