from test_helper import run_common_tests, passed, failed, import_task_file, get_task_windows


def test_value():
    file = import_task_file()
    if file.first_half == '''\nit's a really long string\ntriple-quoted st''':
        passed()
    else:
        failed("Remember about string slicing.")

def test_value_python3():
    import sys
    if sys.version[0] != "3":
        passed()
        return
    try:
        import_task_file()
        passed()
    except TypeError:
        failed("Division operator returns float in Python 3. Use int() function to convert float to integer.")

def test_window():
    window = get_task_windows()[0]
    if "phrase" in window and "len" in window:
        passed()
    else:
        failed("Remember about string slicing.")


if __name__ == '__main__':
    test_value_python3()
    run_common_tests()

    test_value()
    test_window()
