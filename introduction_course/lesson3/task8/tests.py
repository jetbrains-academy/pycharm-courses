from test_helper import run_common_tests, get_answer_placeholders, passed, failed


def test_value():
    window = get_answer_placeholders()[0]

    first = "The name of this ice-cream is \\\"Sweeet'n'Tasty\\\""
    second = 'The name of this ice-cream is "Sweeet\\\'n\\\'Tasty"'

    if first in window or second in window:
        passed()
    else:
        failed("Sorry, the wrong string is printed")


if __name__ == '__main__':
    run_common_tests()
    test_value()
