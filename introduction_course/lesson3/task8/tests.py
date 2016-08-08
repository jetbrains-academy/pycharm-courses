from test_helper import run_common_tests, get_answer_placeholders, passed, failed, get_file_output


def test_value():
    window = get_answer_placeholders()[0]

    first = "The name of this ice-cream is \\\"Sweet'n'Tasty\\\""
    second = 'The name of this ice-cream is "Sweet\\\'n\\\'Tasty"'

    if first in window or second in window:
        passed()
    else:
        if '\\\"Sweet' in window or 'Tasty\\\"' in window:
            failed("There is no need to escape double quotation mark in single quoted string")
        failed("Sorry, the wrong string is printed")


def test_output():
    output = get_file_output()
    index = output.index('''\"Sweet\" is an ice-cream''')
    if index > 0:
        if len(output) > index + 2:
            failed("Print output in one line")
    passed()


if __name__ == '__main__':
    run_common_tests()
    test_output()
    test_value()
