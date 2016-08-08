for i in range(5):
    if i == 3:
        continue   # skip the rest of the code inside loop for current i value
    print(i)

for x in range(10):
    if x % 2 == 0:
        continue   # skip print(x) for this loop
    print(x)
