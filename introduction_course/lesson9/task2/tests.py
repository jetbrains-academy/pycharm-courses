from test_helper import run_common_tests, failed, passed, get_answer_placeholders, get_file_output


def test_window():
    window = get_answer_placeholders()[0]
    output = get_file_output()
    if "datetime" not in window:
        failed("Use datetime module")
    elif len(output) > 0 and "<" not in output[0]:
        passed()
    else:
        failed("Print the current date")


def test_current_date():
    output = get_file_output()
    import datetime
    now = str(datetime.datetime.today())[:10]
    if output[0].startswith(now):
        passed()
    else:
        failed("Print the current date")

if __name__ == '__main__':
    run_common_tests()
    test_window()
    test_current_date()
