from test_helper import run_common_tests, failed, passed, get_answer_placeholders, test_answer_placeholders_text_deleted, \
    test_is_initial_text, test_is_not_empty, do_not_run_on_check


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if placeholder == "models.Model":
        passed()
    else:
        failed("Use models.Model as an ancestor")


def test_title():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[1]
    if "title" in placeholder:
        passed()
    else:
        failed("Define title variable")


def test_title1():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[1]
    if "CharField" in placeholder and "max_length" in placeholder and "200" in placeholder:
        passed()
    else:
        failed("Create models.CharField(max_length=200) here")


def test_published_date():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[2]
    if "published_date" in placeholder:
        passed()
    else:
        failed("Define published_date variable")


def test_published_date1():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[2]
    if "DateTimeField" in placeholder and "blank" in placeholder and "null" in placeholder:
        passed()
    else:
        failed("Define variable as DateTimeField(blank=True, null=True)")


if __name__ == '__main__':
    do_not_run_on_check()
    test_is_initial_text()
    test_is_not_empty()
    test_answer_placeholders_text_deleted()
    test_answer_placeholders()
    test_title()
    test_title1()
    test_published_date()
    test_published_date1()


