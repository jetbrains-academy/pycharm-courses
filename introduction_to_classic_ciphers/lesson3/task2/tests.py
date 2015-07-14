from test_helper import run_common_tests, failed, passed, get_file_output

DECRYPTED_MESSAGE = 'STRIKEATDAWN'


def test_file_output():
    file_output = get_file_output()
    final_outputs = file_output[-2:]

    # check the two cases, where key=1, key=3, respectively
    decrypted_message_case_one = ''.join([word[1] for word in final_outputs[0].split(' ')])
    decrypted_message_case_two = ''.join([word[3] for word in final_outputs[1].split(' ')])
    if decrypted_message_case_one == DECRYPTED_MESSAGE and decrypted_message_case_two == DECRYPTED_MESSAGE:
        passed()
    else:
        failed(message='Please try again.')


if __name__ == '__main__':
    run_common_tests()
    test_file_output()


