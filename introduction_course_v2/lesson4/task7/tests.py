from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_window():
    window = get_answer_placeholders()[0]
    if "grocery_dict" in window and " in " in window:
        passed()
    else:
        failed("Use in keyword")

def test_fish():
    window = get_answer_placeholders()[0]
    if "fish" in window:
        passed()
    else:
        failed("Check if grocery_dict keys contain fish")

if __name__ == '__main__':
    run_common_tests("Use in keyword")
    test_window()
    test_fish()