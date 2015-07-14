import unittest.mock as mock

from custom_test_helpers import check_tests_pass, check_tests_fail, \
    reload_module, abort_tests
from test_helper import run_common_tests, test_answer_placeholders_text_deleted, \
    passed, failed, import_task_file


if __name__ == '__main__':
    from hello_someone import hello_someone

    run_common_tests()
    test_answer_placeholders_text_deleted()

    task_tests_module = import_task_file()

    # check that all tests pass
    check_tests_pass(task_tests_module)

    # check that the function hello_someone() is called at least once by the tests
    counting_hello_someone = mock.Mock(wraps=hello_someone)
    with mock.patch('{}.{}'.format('hello_someone', 'hello_someone'), counting_hello_someone):
        module = import_task_file()
        check_tests_pass(module)
        if counting_hello_someone.call_count > 0:
            passed("Test called the 'hello_someone' function")
        else:
            failed("Test never called the 'hello_someone' function")

    # check that the tests fail on a broken implementation
    def broken_hello_someone(someone):
        # omit the comma
        return "Hello {}!".format(someone)

    with mock.patch('{}.{}'.format('hello_someone', 'hello_someone'), broken_hello_someone):
        module = import_task_file()
        check_tests_fail(module)
