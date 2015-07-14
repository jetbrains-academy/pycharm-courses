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
