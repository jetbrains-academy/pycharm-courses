from custom_test_helpers import check_tests_pass
from test_helper import run_common_tests, test_answer_placeholders_text_deleted, import_task_file


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders_text_deleted()

    module = import_task_file()
    check_tests_pass(module)
