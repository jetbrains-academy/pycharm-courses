from test_helper import run_common_tests, failed, passed, get_file_output


def test_file_output():
    file_output = get_file_output()

    if (len(file_output) >= 2) and (file_output[-2:] == ['PLEASEORDERAPIZZA','ITISEXPENSIVE']):
        passed()
    else:
        failed(message='Please reload the file and try again')


if __name__ == '__main__':
    run_common_tests()
    test_file_output()


