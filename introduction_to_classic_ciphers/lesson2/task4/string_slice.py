MESSAGE = 'Hello, World!'

print '-- slicing with the start index --'
print MESSAGE[1:]  # extract the substring that starts with the character at index 1
print MESSAGE[3:]  # extract the substring that starts with the character at index 3


print '-- slicing with the stop index --'
print MESSAGE[:2]  # extract the substring that stops at (does not include) the character at index 2
print MESSAGE[:11]  # extract the substring that stops at (does not include) the character at index 11
print MESSAGE[: len(MESSAGE)-2]  # note: len(MESSAGE) returns the number of characters in MESSAGE
print MESSAGE[:-2]  # extract the substring that goes up to, but does not include, the final 2 characters

print '-- slicing with a start and stop index ---'
print MESSAGE[1:-1]
print MESSAGE[4:9]
print MESSAGE[4:-4]

print '-- review ---'
# fill in the index values so that only the 'World' part of MESSAGE gets printed
print MESSAGE[replace with the start index:replace with the stop index]

# fill in the index values so that only the ',' part of MESSAGE gets printed
print MESSAGE[replace with the start index:replace with the stop index]



