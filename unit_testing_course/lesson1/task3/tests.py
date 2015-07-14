from custom_test_helpers import run_module_tests
from test_helper import run_common_tests, test_answer_placeholders_text_deleted, import_task_file, passed, failed


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders_text_deleted()

    task_module = import_task_file()
    test_result = run_module_tests(task_module)

    if (
        test_result.testsRun == 3 and
        len(test_result.failures) == 1 and
        len(test_result.errors) == 1
    ):
        passed("check number of successes, failures and errors")
    else:
        failed("check number of successes, failures and errors")

    if not any(
        "test_failure" in formatted_traceback
        for test_case, formatted_traceback
        in test_result.failures
    ):
        failed("test_failure should fail")
    else:
        passed("test_failure should fail")

    if not any(
        "test_error" in formatted_traceback
        for test_case, formatted_traceback
        in test_result.errors
    ):
        failed("test_error should cause an error")
    else:
        passed("test_error should cause an error")
