from pre_treat_message import pre_treat_message

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def decrypt(message, key):
    """ apply the null cipher, where the key tells at what index the letters of the plaintext are hidden in each
    5-letter 'word' of the encrypted text
    """
    message = pre_treat_message(message)  # convert to uppercase and remove punctuation

    words_in_message = message.split()

    decrypted_message = ''

    for word in words_in_message:
        decrypted_message += word[key % 5]  # find the letter whose index is equal to the key

    return decrypted_message

# do not modify this file beyond this point
ENCRYPTED_MESSAGE_ONE = 'KPDJT XLFEI UEVUP NATCZ JSNOF QEPLK NOATG SRUVS RDMBU DEOCA ORSIY JAMLB RPNZN CIJIG HZIZJ RZJML SAFMZ'
ENCRYPTED_MESSAGE_TWO = 'QWICU HYTWX VMIAE FMSEL SKEVT NVXMP RNPJI KJEME JKNKW IMSDM BTIWG PWVNZ OCEMT'

print decrypt(ENCRYPTED_MESSAGE_ONE, 1)  # decrypt the message using a key of 1
print decrypt(ENCRYPTED_MESSAGE_TWO, 7)  # decrypt the message using a key of 7
