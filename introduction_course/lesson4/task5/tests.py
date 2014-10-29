from test_helper import run_common_tests, get_answer_placeholders, passed, failed


def test_window():
    window = get_answer_placeholders()[0]
    if "phone_book" in window and "Jane" in window:
        passed()
    else:
        failed("Use indexing e.g. dct[key]")

if __name__ == '__main__':
    run_common_tests("Use indexing e.g. dct[key]")
    test_window()
