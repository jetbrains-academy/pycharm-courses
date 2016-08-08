import random

# print a random value between 0 and 2 (includes 0 and 2).
# we'll repeat it a few times. Observe the variation in the values printed to the console.
print '-- picking a random integer between 0 and 2 (inclusive) ---'
print random.randint(0, 2)
print random.randint(0, 2)
print random.randint(0, 2)
print random.randint(0, 2)
print random.randint(0, 2)


# if we're careful about the bounds, we can treat that random integer as index in a string...
# here, we get a randomly-chosen integer between 0 and 25, and print the letter at the corresponding index in ALPHABET
print '-- picking a random letter ---'
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
random_integer = random.randint(0, 25)  # 25 is the highest index value in ALPHABET
print ALPHABET[random_integer]

# and a step further, we could create a string of random letters...
# review exercise: print a string of 10 randomly-chosen letters
print '-- picking a string of 10 random letters ---'
string_of_random_letters = ''
for i in range(0, 10):
    random_alphabet_index = random.randint(0, 25)
    string_of_random_letters += ALPHABET[random_alphabet_index]

print string_of_random_letters
