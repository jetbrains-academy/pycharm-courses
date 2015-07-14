import random
import re


def random_not_42():
    value = 42
    while value == 42:
        value = random.randint(-(2 ** 31), 2 ** 31 - 1)
    return value


def find_foo(s):
    return re.search(r"foo", s)


def random_float_between_inclusive(a, b):
    return random.uniform(a, b)


def random_float_between_noninclusive(a, b):
    if a == b:
        raise ValueError("a must be different than b!")
    result = a
    while result == a or result == b:
        result = random.uniform(a, b)
    return result
