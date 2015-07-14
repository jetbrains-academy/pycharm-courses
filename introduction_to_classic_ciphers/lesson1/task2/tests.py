from test_helper import run_common_tests, failed, passed, get_file_output


def test_file_output():
    file_output = get_file_output()
    if len(file_output) < 3:
        failed(message="Please reload the task and try again")
        return

    if file_output[-3:] == ['HELLO WORLD', 'HE PURCHASED THREE ITEMS BREAD EGGS AND MILK', 'DOES HE HAVE THE TICKETS']:
        passed()
    else:
        failed(message="File output did not match the expected values. Please try again.")

if __name__ == '__main__':
    run_common_tests()
    test_file_output()