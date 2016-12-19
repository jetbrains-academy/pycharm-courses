from test_helper import run_common_tests, failed, passed, get_answer_placeholders, test_answer_placeholders_text_deleted, \
    test_is_initial_text, test_is_not_empty, do_not_run_on_check


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if "blog" in placeholder and "post_list.html" in placeholder:
        passed()
    else:
        failed("Please, render blog/post_list.html template")


if __name__ == '__main__':
    do_not_run_on_check()
    test_is_initial_text()
    test_is_not_empty()
    test_answer_placeholders_text_deleted()
    test_answer_placeholders()


