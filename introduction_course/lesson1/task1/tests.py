from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_ASCII():
    windows = get_answer_placeholders()
    for window in windows:
        all_ascii = all(ord(c) < 128 for c in window)
        if not all_ascii:
            failed("Please use only English characters this time.")
            return
    passed()


def test_is_alpha():
    window = get_answer_placeholders()[0]
    is_multiline = window.find("\n")
    if is_multiline != -1:
        window = window[:is_multiline-1]
    splitted = window.split()
    for s in splitted:
        if not s.isalpha():
            failed("Please use only English characters this time.")
            return

    passed()


if __name__ == '__main__':
    test_ASCII()
    run_common_tests("You should enter your name")
    test_is_alpha()


