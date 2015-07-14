from pre_treat_message import pre_treat_message

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def decrypt(message):

    message = pre_treat_message(message)

    decrypted_message = ''

    # assemble the plaintext message by decrypting the message one letter at a time
    for c in message:
        if c not in ALPHABET:
            decrypted_message += c
            continue

        # find the corresponding decrypted letter and append it to decrypted_message
        replace with the logic for decrypting the letter    return decrypted_message


# do not modify this file beyond this point
MESSAGE_ONE = 'RG RH HGROO HMLDRMT'
MESSAGE_TWO = 'HSLFOW DV TL HOVWWRMT'
MESSAGE_THREE = 'R XZMMLG URMW NB YLLGH'

print decrypt(MESSAGE_ONE)
print decrypt(MESSAGE_TWO)
print decrypt(MESSAGE_THREE)