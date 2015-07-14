from custom_test_helpers import run_test_case_tests, inspect_assertions, \
    normalize_call_args, check_used_only_assertions
from test_helper import passed, failed, run_common_tests, import_task_file, \
    test_answer_placeholders_text_deleted


import itertools
import unittest.mock
from tested_code import find_foo
import re


def check_test_not_42():
    has_failed = False

    task_module = import_task_file()
    test_case_class = inspect_assertions(task_module.TestRandomNot42)
    test_result = run_test_case_tests(test_case_class)

    if not test_result.wasSuccessful():
        failed("at least one test failed")
        has_failed = True

    if not check_used_only_assertions(test_case_class, ["assertNotEqual"]):
        has_failed = True


    mock_random_not_42 = unittest.mock.Mock(return_value=42)
    with unittest.mock.patch('tested_code.random_not_42', mock_random_not_42):
        task_module = import_task_file()
        test_result = run_test_case_tests(task_module.TestRandomNot42)
        if test_result.wasSuccessful():
            failed("tests passed with broken implementation")
            has_failed = True

    if not has_failed:
        passed()


def check_test_find_foo():
    has_failed = False

    task_module = import_task_file()
    test_case_class = inspect_assertions(task_module.TestFindFoo)
    test_result = run_test_case_tests(test_case_class)

    if not test_result.wasSuccessful():
        failed("at least one test failed")
        has_failed = True

    if not check_used_only_assertions(
            test_case_class,
            ["assertIsNone", "assertIsNotNone"],
    ):
        has_failed = True

    # check that all of the substrings were tested
    mock_find_foo = unittest.mock.Mock(wraps=find_foo)
    with unittest.mock.patch('tested_code.find_foo', mock_find_foo):
        task_module = import_task_file()
        test_case_class = task_module.TestFindFoo
        run_test_case_tests(test_case_class)

        normalized_call_args = [
            normalize_call_args(call_args, func=find_foo)
            for call_args in mock_find_foo.call_args_list
        ]
        for substring in itertools.chain(
                ["foo"],
                test_case_class.strings_with_foo,
                test_case_class.strings_without_foo
        ):
            if ((substring,), {}) not in normalized_call_args:
                failed("substring \"{}\" not tested".format(substring))
                has_failed = True

    # check with broken find_foo()
    def find_fo(s):
        return re.search(r"fo", s)
    for broken_find_fo in [
        find_fo,
        lambda s: None,
        lambda s: 0,
    ]:
        with unittest.mock.patch('tested_code.find_foo', broken_find_fo):
            task_module = import_task_file()
            test_result = run_test_case_tests(task_module.TestFindFoo)
            if test_result.wasSuccessful():
                failed("tests passed with broken implementation")
                has_failed = True

    if not has_failed:
        passed()


def check_test_random_float_between_inclusive():
    has_failed = False

    task_module = import_task_file()
    test_case_class = inspect_assertions(task_module.TestRandomFloatBetweenInclusive)
    test_result = run_test_case_tests(test_case_class)

    if not test_result.wasSuccessful():
        failed("at least one test failed")
        has_failed = True

    if not check_used_only_assertions(
            test_case_class,
            ["assertGreaterEqual", "assertLessEqual"],
    ):
        has_failed = True

    for broken_func in [
        lambda a, b: a - 1,
        lambda a, b: b + 1,
    ]:
        with unittest.mock.patch('tested_code.random_float_between_inclusive', broken_func):
            task_module = import_task_file()
            test_result = run_test_case_tests(task_module.TestRandomFloatBetweenInclusive)
            if test_result.wasSuccessful():
                failed("tests passed with broken implementation")
                has_failed = True

    if not has_failed:
        passed()


def check_test_random_float_between_noninclusive():
    has_failed = False

    task_module = import_task_file()
    test_case_class = inspect_assertions(task_module.TestRandomFloatBetweenNoninclusive)
    test_result = run_test_case_tests(test_case_class)

    if not test_result.wasSuccessful():
        failed("at least one test failed")
        has_failed = True

    if not check_used_only_assertions(
            test_case_class,
            ["assertGreater", "assertLess"],
    ):
        has_failed = True

    for broken_func in [
        lambda a, b: a - 1,
        lambda a, b: b + 1,
        lambda a, b: a,
        lambda a, b: b,
    ]:
        with unittest.mock.patch('tested_code.random_float_between_noninclusive', broken_func):
            task_module = import_task_file()
            test_result = run_test_case_tests(task_module.TestRandomFloatBetweenNoninclusive)
            if test_result.wasSuccessful():
                failed("tests passed with broken implementation")
                has_failed = True

    if not has_failed:
        passed()


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders_text_deleted()

    check_test_not_42()
    check_test_find_foo()
    check_test_random_float_between_inclusive()
    check_test_random_float_between_noninclusive()
