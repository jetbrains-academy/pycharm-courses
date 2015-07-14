import random
import unittest

from tested_code import random_not_42, find_foo, \
    random_float_between_inclusive, random_float_between_noninclusive


class TestRandomNot42(unittest.TestCase):
    def test_many_values(self):
        """call the function 100 times and make sure the result isn't 42"""
        write this test!


class TestFindFoo(unittest.TestCase):
    """tests for the find_foo() function

    find_foo(s) returns an object if "foo" is a sub-string of s,
    and None otherwise.
    """
    # valid_names = [
    #     'foo',
    #     'Bar',
    #     'foorBar',
    #     'foo_bar',
    #     '_fooBar',
    #     'foo1',
    #     'foo_',
    # ]
    #
    # invalid_names = [
    #     '1foo',
    #     'foo-bar',
    #     '$foo',
    #     'foo bar',
    #     'foo+bar4ever',
    # ]

    strings_with_foo = [
        'foo',
        'aaa foo bbb',
        'aaa foo',
        'foo bbb',
        'no foo for you, come back oen year!'
    ]

    strings_without_foo = [
        'boo',
        'aaa bbb',
        'four',
    ]

    def test_identical(self):
        """check that find_foo finds 'foo' in 'foo'"""
        write this test!

    def test_strings_with_foo(self):
        """check that find_foo finds 'foo' in all of the strings with 'foo'"""
        write this test!

    def test_strings_without_foo(self):
        """check that find_foo finds 'foo' in all of the strings with 'foo'"""
        write this test!


class TestRandomFloatBetweenInclusive(unittest.TestCase):
    def test_random_values(self):
        for i in range(100):
            start = random.random()
            end = random.random()
            if start > end:
                start, end = end, start
            value = random_float_between_inclusive(start, end)

            check the returned value


class TestRandomFloatBetweenNoninclusive(unittest.TestCase):
    def test_random_values(self):
        for i in range(100):
            start = random.random()
            end = random.random()
            if start > end:
                start, end = end, start
            value = random_float_between_noninclusive(start, end)

            check the returned value
