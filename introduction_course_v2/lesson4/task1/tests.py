from test_helper import run_common_tests, get_answer_placeholders, passed, failed, get_file_output, test_file_importable


def test_value():
    output = get_file_output()[1]
    if "[4, 9, 16]" in output:
        passed()
    else:
        failed("Use list slicing lst[index1:index2]")

def test_window():
    window = get_answer_placeholders()[0]
    if "squares" in window and "[" in window and "]" in window and ":" in window:
        passed()
    else:
        failed("Use list slicing lst[index1:index2]")

if __name__ == '__main__':
    test_file_importable()
    test_value()
    test_window()
    run_common_tests("Use list slicing lst[index1:index2]")

