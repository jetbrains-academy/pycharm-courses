import functools
import inspect
import types
import sys
from unittest import defaultTestLoader, TestResult
import unittest

from test_helper import failed, passed


def abort_tests(message="Critical failure; aborting tests."):
    print(message)
    sys.exit(0)


def reload_module(module):
    if sys.version_info < (3,):
        reload(module)
    else:
        import importlib
        importlib.reload(module)


def run_module_tests(module):
    test_suite = defaultTestLoader.loadTestsFromModule(module)
    test_result = TestResult()
    test_suite.run(test_result)
    return test_result


def run_test_case_tests(test_case_class):
    test_suite = defaultTestLoader.loadTestsFromTestCase(test_case_class)
    test_result = TestResult()
    test_suite.run(test_result)
    return test_result


def check_tests_pass(module, error_text="Some tests failed! Fix your code..."):
    test_result = run_module_tests(module)

    if test_result.wasSuccessful():
        passed()
    else:
        failed(error_text)


def check_tests_fail(module, error_text="All tests passed on a bad implementation! Improve your tests..."):
    test_result = run_module_tests(module)

    if test_result.wasSuccessful():
        failed(error_text)
    else:
        passed()


def _get_assertion_method_names(class_):
    return [
        name for name in dir(class_)
        if name.startswith(("assert", "failIf", "failUnless"))
        and "_" not in name
        and isinstance(getattr(class_, name), types.FunctionType)
    ]
ASSERTION_METHOD_NAMES = frozenset(_get_assertion_method_names(unittest.TestCase))


def get_test_method_names(class_):
    return [
        name for name in dir(class_)
        if (name == 'runTest' or name.startswith("test"))
        and isinstance(getattr(class_, name), types.FunctionType)
    ]


def _override_method_with_mock(test_case_instance, method_name):
    orig_method = getattr(test_case_instance, method_name)
    mock_method = unittest.mock.Mock(wraps=orig_method)
    setattr(test_case_instance, method_name, mock_method)
    return orig_method, mock_method


# def inspect_assertions(test_case_class):
#     orig_methods = {}
#     new_methods = {}
#     for assertion_method_name in ASSERTION_METHOD_NAMES:
#         orig_method, mock_method = _override_method_with_mock(
#             test_case_class, assertion_method_name)
#         orig_methods[assertion_method_name] = orig_method
#         new_methods[assertion_method_name] = mock_method
#     test_case_class.wrapped_methods = new_methods
#
#     @classmethod
#     def get_total_call_count(cls, method_names=None):
#         if method_names is None:
#             method_names = ASSERTION_METHOD_NAMES
#         return sum(
#             new_methods[method_name].call_count
#             for method_name in method_names
#         )
#     test_case_class.get_total_call_count = get_total_call_count
#
#     return test_case_class


def inspect_assertions(test_case_class):
    test_method_names = get_test_method_names(test_case_class)

    class_counters = {}
    test_case_class.class_counters = class_counters
    for assertion_method_name in ASSERTION_METHOD_NAMES:
        counter_method = unittest.mock.Mock(return_value=None)
        class_counters[assertion_method_name] = counter_method

    per_method_counters = {}
    test_case_class.per_method_counters = per_method_counters
    for test_method_name in test_method_names:
        per_method_counters[test_method_name] = method_counters = {}
        for assertion_method_name in ASSERTION_METHOD_NAMES:
            counter_method = unittest.mock.Mock(return_value=None)
            method_counters[assertion_method_name] = counter_method

    def make_wrapper(orig_method, test_method_name, assertion_method_name):
        @functools.wraps(orig_method)
        def wrapper(*args_, **kwargs_):
            class_counters[assertion_method_name](*args_, **kwargs_)
            per_method_counters[test_method_name][assertion_method_name](*args_, **kwargs_)
            return orig_method(*args_, **kwargs_)
        return wrapper

    for test_method_name in test_method_names:
        def make_new_test_method(test_method_name, orig_test_method):
            @functools.wraps(orig_test_method)
            def new_test_method(self, *args, **kwargs):
                orig_methods = {}
                for assertion_method_name in ASSERTION_METHOD_NAMES:
                    orig_method = getattr(self, assertion_method_name)
                    orig_methods[assertion_method_name] = orig_method
                    wrapper = make_wrapper(orig_method, test_method_name, assertion_method_name)
                    setattr(self, assertion_method_name, wrapper)

                try:
                    return orig_test_method(self, *args, **kwargs)
                finally:
                    for assertion_method_name, orig_method in orig_methods.items():
                        setattr(self, assertion_method_name, orig_method)

            return new_test_method

        orig_test_method = getattr(test_case_class, test_method_name)
        new_test_method = make_new_test_method(test_method_name, orig_test_method)
        setattr(test_case_class, test_method_name, new_test_method)

    @classmethod
    def get_total_call_count(cls, method_names=None):
        if method_names is None:
            method_names = ASSERTION_METHOD_NAMES
        return sum(
            cls.class_counters[method_name].call_count
            for method_name in method_names
        )
    test_case_class.get_total_call_count = get_total_call_count

    @classmethod
    def get_test_method_total_call_count(cls, test_method_name, method_names=None):
        if method_names is None:
            method_names = ASSERTION_METHOD_NAMES
        return sum(
            cls.per_method_counters[test_method_name][method_name].call_count
            for method_name in method_names
        )
    test_case_class.get_test_method_total_call_count = get_test_method_total_call_count

    return test_case_class


def normalize_call_args(call_args, func=None, signature=None, with_defaults=True):
    if func is None and signature is None:
        raise ValueError("Must supply either func or signature")
    if func is not None and signature is not None:
        raise ValueError("Must supply either func or signature; not both")

    if signature is None:
        signature = inspect.signature(func)

    args, kwargs = call_args
    bound_args = signature.bind(*args, **kwargs)

    # based on code from the Python docs:
    # https://docs.python.org/3/library/inspect.html#inspect.BoundArguments
    if with_defaults:
        for param in signature.parameters.values():
            if (
                    param.name not in bound_args.arguments
                    and param.default is not param.empty
            ):
                bound_args.arguments[param.name] = param.default

    return bound_args.args, bound_args.kwargs


def check_used_only_assertions(test_case_class, assertion_method_names):
    cond = not (
        test_case_class.get_total_call_count() >
        test_case_class.get_total_call_count(assertion_method_names)
    )
    if not cond:
        if len(assertion_method_names) == 1:
            assertion_names_str = assertion_method_names[0]
        else:
            assertion_names_str = ', '.join(
                assertion_method_names[:-2] +
                [' and '.join(assertion_method_names[-2:])]
            )
        failed("should use only {}".format(assertion_names_str),
               name=test_case_class.__name__)
    return cond
