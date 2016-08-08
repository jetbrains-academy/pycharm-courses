from custom_test_helpers import check_tests_pass, get_test_method_names, \
    run_test_case_tests
from test_helper import passed, failed, run_common_tests, \
    test_answer_placeholders_text_deleted, import_task_file


def check_tests_fail_on_broken_implementations():
    expected_results = {
        'broken_shuffle_1': {
            'test_empty': True,
            'test_same_length': True,
            'test_same_values': True,
            'test_values_are_shuffled': False,
            'test_input_not_mutated': True,
        },
        'broken_shuffle_2': {
            'test_empty': True,
            'test_same_length': False,
            'test_same_values': False,
            'test_values_are_shuffled': None,
            'test_input_not_mutated': True,
        },
        'broken_shuffle_3': {
            'test_empty': True,
            'test_same_length': True,
            'test_same_values': True,
            'test_values_are_shuffled': False,
            'test_input_not_mutated': True,
        },
        'broken_shuffle_4': {
            'test_empty': True,
            'test_same_length': True,
            'test_same_values': True,
            'test_values_are_shuffled': True,
            'test_input_not_mutated': False,
        },
        'broken_shuffle_5': {
            'test_empty': True,
            'test_same_length': True,
            'test_same_values': True,
            'test_values_are_shuffled': None,
            'test_input_not_mutated': False,
        },
        'broken_shuffle_6': {
            'test_empty': True,
            'test_same_length': True,
            'test_same_values': False,
            'test_values_are_shuffled': None,
            'test_input_not_mutated': True,
        },
        'broken_shuffle_7': {
            'test_empty': False,
            'test_same_length': None,
            'test_same_values': None,
            'test_values_are_shuffled': None,
            'test_input_not_mutated': False,
        },
    }

    task_module = import_task_file()
    orig_random_shuffle = task_module.random_shuffle
    for broken_func_name in sorted(expected_results):
        task_module.random_shuffle = getattr(task_module, broken_func_name)
        test_result = run_test_case_tests(task_module.TestRandomShuffle)

        test_method_name2failure = {
            test_case.id().rsplit('.', 1)[1]: test_case
            for (test_case, msg) in test_result.failures
        }
        test_method_name2error = {
            test_case.id().rsplit('.', 1)[1]: test_case
            for (test_case, msg) in test_result.errors
        }
        test_method_name2failure_or_error = {}
        test_method_name2failure_or_error.update(test_method_name2failure)
        test_method_name2failure_or_error.update(test_method_name2error)

        has_failed = False
        for test_method_name in get_test_method_names(task_module.TestRandomShuffle):
            expected_result = expected_results[broken_func_name][test_method_name]
            if expected_result is None:
                # ignore
                continue

            is_error_or_failure = test_method_name in test_method_name2failure_or_error

            if expected_result is True and is_error_or_failure:
                failed("{func_name} failed test {test_name}, which it should pass".format(
                    func_name=broken_func_name,
                    test_name="TestRandomShuffle."+test_method_name,
                ), name="test {}".format(broken_func_name))
                has_failed = True
                message = [x[1] for x in test_result.failures + test_result.errors if x[0].id().rsplit('.', 1)[1] == test_method_name][0]
                print(message)

            elif expected_result is False and not is_error_or_failure:
                failed("{func_name} passed test {test_name}, which it should fail".format(
                    func_name=broken_func_name,
                    test_name="TestRandomShuffle."+test_method_name,
                ), name="test {}".format(broken_func_name))
                has_failed = True

        if not has_failed:
            passed(name="test {}".format(broken_func_name))

    task_module.random_shuffle = orig_random_shuffle

if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders_text_deleted()

    check_tests_pass(import_task_file())
    check_tests_fail_on_broken_implementations()
