from test_helper import run_common_tests, get_task_windows, passed, failed, get_file_output


def test_value():
    output = get_file_output()
    if "[4, 9, 16]" in output:
        passed()
    else:
        failed("Use list slicing lst[index1:index2]")

def test_window():
    window = get_task_windows()[0]
    if "squares" in window and "[" in window and "]" in window and ":" in window:
        passed()
    else:
        failed("Use list slicing lst[index1:index2]")

if __name__ == '__main__':
    test_value()
    test_window()
    run_common_tests("Use list slicing lst[index1:index2]")
