import functools
import unittest
import unittest.mock

from custom_test_helpers import inspect_assertions, run_test_case_tests, normalize_call_args
from test_helper import run_common_tests, test_answer_placeholders_text_deleted, import_task_file, passed, failed, \
    get_answer_placeholders


def check_integer_truthiness_tests():
    task_module = import_task_file()
    TestIntegerTruthiness = inspect_assertions(task_module.TestIntegerTruthiness)
    test_result = run_test_case_tests(TestIntegerTruthiness)

    if not test_result.wasSuccessful():
        failed("Some of the TestIntegerTruthiness tests failed!")

    placeholder_windows = get_answer_placeholders()[0:3]
    test_zero_window, test_one_window, test_other_value_window = placeholder_windows

    # check test_zero
    n_assertions = TestIntegerTruthiness.get_test_method_total_call_count("test_zero")
    test_name = "TestIntegerTruthiness.test_zero"
    if n_assertions > 1:
        failed(name=test_name, message="must use only one assertion")
    elif n_assertions == 0:
        failed(name=test_name, message="must use an assertion")
    elif unittest.mock.call(0) in TestIntegerTruthiness.per_method_counters["test_zero"]["assertFalse"].call_args_list:
        passed(name=test_name)
    else:
        failed(name=test_name)

    # check test_one
    n_assertions = TestIntegerTruthiness.get_test_method_total_call_count("test_one")
    test_name = "TestIntegerTruthiness.test_one"
    if n_assertions > 1:
        failed(name=test_name, message="must use only one assertion")
    elif n_assertions == 0:
        failed(name=test_name, message="must use an assertion")
    elif unittest.mock.call(1) in TestIntegerTruthiness.per_method_counters["test_one"]["assertTrue"].call_args_list:
        passed(name=test_name)
    else:
        failed(name=test_name)

    # check test_other_value
    wrapped_assertTrue = TestIntegerTruthiness.per_method_counters["test_other_value"]["assertTrue"]
    n_assertions = TestIntegerTruthiness.get_test_method_total_call_count("test_other_value")
    test_name = "TestIntegerTruthiness.test_other_value"
    if n_assertions > 1:
        failed(name=test_name, message="must use only one assertion")
    elif n_assertions == 0:
        failed(name=test_name, message="must use an assertion")
    elif (
            "self.assertTrue" in test_other_value_window and
            wrapped_assertTrue.call_count > 0 and
            isinstance(wrapped_assertTrue.call_args[0][0], int) and
            wrapped_assertTrue.call_args[0][0] not in {0, 1}
    ):
        passed(name=test_name)
    else:
        failed(name=test_name)


def check_none_truthiness_tests():
    task_module = import_task_file()
    TestNoneTruthiness = inspect_assertions(task_module.TestNoneTruthiness)
    test_result = run_test_case_tests(TestNoneTruthiness)

    if not test_result.wasSuccessful():
        failed("Some of the TestIntegerTruthiness tests failed!")

    wrapped_assertFalse = TestNoneTruthiness.per_method_counters["test_none"]["assertFalse"]

    n_assertions = TestNoneTruthiness.get_test_method_total_call_count("test_none")
    test_name = "TestNoneTruthiness.test_none"
    if n_assertions > 1:
        failed(name=test_name, message="must use only one assertion")
    elif n_assertions == 0:
        failed(name=test_name, message="must use an assertion")
    elif unittest.mock.call(None) in TestNoneTruthiness.per_method_counters["test_none"]["assertFalse"].call_args_list:
        passed(name=test_name)
    else:
        failed(name=test_name)


def check_test_container_class_assertion_methods():
    window1, window2 = get_answer_placeholders()[4:6]
    if window1 == 'False' and window2 == 'True':
        passed()
    else:
        failed()


def conditional_passed_or_failed(condition, name):
    if condition:
        passed(name=name)
    else:
        failed(name=name)


def check_container_truthiness_tests():
    task_module = import_task_file()
    test_case_class = inspect_assertions(task_module.TestContainerTruthiness)
    test_result = run_test_case_tests(test_case_class)

    conditional_passed_or_failed(test_result.wasSuccessful(), "TestContainerTruthiness tests pass")

    for (test_method_name, empty_container) in [
        ("test_list", []),
        ("test_tuple", ()),
        ("test_set", set()),
        ("test_dict", {}),
    ]:
        calls = test_case_class.per_method_counters[test_method_name]["assertFalse"].call_args_list
        normalized_calls = [
            normalize_call_args(c, func=functools.partial(test_case_class.assertFalse, None))
            for c in calls
        ]
        conditional_passed_or_failed(
            condition=any(args[0] == empty_container for args, kwargs in normalized_calls),
            name="{} properly tested empty container".format(test_method_name),
        )

        calls = test_case_class.per_method_counters[test_method_name]["assertTrue"].call_args_list
        normalized_calls = [
            normalize_call_args(c, func=functools.partial(test_case_class.assertTrue, None))
            for c in calls
        ]
        conditional_passed_or_failed(
            condition=any(
                type(args[0]) == type(empty_container) and args[0] != empty_container
                for args, kwargs in normalized_calls
            ),
            name="{} properly tested non-empty container".format(test_method_name),
        )


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders_text_deleted()

    check_integer_truthiness_tests()
    check_none_truthiness_tests()
    check_test_container_class_assertion_methods()
    check_container_truthiness_tests()
