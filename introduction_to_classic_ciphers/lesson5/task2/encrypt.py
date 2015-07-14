from pre_treat_message import pre_treat_message

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encrypt(message):

    message = pre_treat_message(message)

    encrypted_message = ''

    # assemble the encrypted message by replacing the letters one at a time
    for c in message:
        if c not in ALPHABET:
            encrypted_message += c
            continue

        index_in_alphabet = ALPHABET.find(c)

        shifted_index = replace with the code that finds the index of the letter to use  # calculate the index of the substitute letter
        encrypted_message += ALPHABET[shifted_index]

    return encrypted_message


# do not modify this file beyond this point
MESSAGE_ONE = 'I ordered eight pizzas.'
MESSAGE_TWO = 'We are expecting guests.'
MESSAGE_THREE = 'They love pizza.'

print encrypt(MESSAGE_ONE)
print encrypt(MESSAGE_TWO)
print encrypt(MESSAGE_THREE)


