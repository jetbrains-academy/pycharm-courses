# use find() to get the index in the string at which the substring starts.
MESSAGE = 'Hello, World! Hello!'

# for substring 'Hello', it's at index 0 that we see the match.
# for substring 'ello', it's at index 1 that we see the  match.
print '-- general cases --'
print MESSAGE.find('Hello')
print MESSAGE.find('ello')
print MESSAGE.find('Zebra')  # returns -1, because the substring was not found


# note, find() starts its search from left and moves to the right, returning the first match it sees;
# to return the last match in the string, you could rfind() to run the search from right to left
print '-- find() vs rfind() --'
print MESSAGE.find('o')  # the first instance, when you move left to right
print MESSAGE.rfind('o')  # the first instance, when you move from right to left


print '-- review --'
# print the index at which 'World' starts in MESSAGE
print replace with the string to search.find(replace with the word to find)
# print the index of the last (ie right-most) match of 'Hello' in MESSAGE
print replace with the string to search.rfind(replace with the word to find)
