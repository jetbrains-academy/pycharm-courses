from test_helper import run_common_tests, failed, passed, get_file_output


def test_outputs():

    outputs = get_file_output()
    if len(outputs) >= 3 and outputs[-3:] == ['IT IS STILL SNOWING', 'SHOULD WE GO SLEDDING', 'I CANNOT FIND MY BOOTS']:
        passed()
    else:
        failed(message='Please try again.')

if __name__ == '__main__':
    run_common_tests()
    test_outputs()