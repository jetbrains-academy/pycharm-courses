def pre_treat_message(message):
    """ removes punctuation (:;,.?!) and converts message to upper case """
    treated_message = message

    # remove punctuation, one symbol at a time
    treated_message = treated_message.replace(':', '')  # remove colons
    treated_message = treated_message.replace(';', '')  # remove semicolons
    treated_message = treated_message.replace(',', '')  # remove commas
    treated_message = treated_message.replace('.', '')  # remove periods
    treated_message = treated_message.replace('?', '')  # remove question marks
    treated_message = treated_message.replace('!', '')  # remove exclamation points

    # convert to uppercase
    treated_message = treated_message.upper()

    return treated_message


MESSAGE_ONE = 'Hello, World!'
MESSAGE_TWO = 'He purchased three items: bread, eggs, and milk.'
MESSAGE_THREE = 'Does he have the tickets?'

# do not modify this file beyond this point
print pre_treat_message(MESSAGE_ONE)
print pre_treat_message(MESSAGE_TWO)
print pre_treat_message(MESSAGE_THREE)
