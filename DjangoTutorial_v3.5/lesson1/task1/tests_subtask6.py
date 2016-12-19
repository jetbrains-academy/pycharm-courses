from test_helper import run_common_tests, failed, passed, get_answer_placeholders, do_not_run_on_check


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if "{%" in placeholder and "%}" in placeholder and "for" in placeholder:
        passed()
    else:
        failed("Use '{% for ... in ... %}' tag")


def test_answer_placeholders1():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if "{%" in placeholder and "%}" in placeholder and "endfor" in placeholder:
        passed()
    else:
        failed("Don't forget to close for tag")


def test_answer_placeholders2():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if "{{" in placeholder and "}}" in placeholder and "post" in placeholder:
        passed()
    else:
        failed("Use {{ post }} to print post content")


if __name__ == '__main__':
    do_not_run_on_check()
    run_common_tests()
    test_answer_placeholders()
    test_answer_placeholders1()
    test_answer_placeholders2()


