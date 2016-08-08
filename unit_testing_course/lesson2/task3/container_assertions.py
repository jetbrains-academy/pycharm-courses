import unittest
import random


def random_shuffle(values):
    """return a new list of the given values in random order"""
    new_values = list(values)
    random.shuffle(new_values)
    return new_values


def broken_shuffle_1(values):
    """this doesn't actually shuffle anything!"""
    return list(values)


def broken_shuffle_2(values):
    """this returns a single instance of each value, shuffled"""
    new_values = list(set(values))
    random.shuffle(new_values)
    return new_values


def broken_shuffle_3(values):
    """this always returns the values sorted"""
    return list(sorted(values))


def broken_shuffle_4(values):
    """this shuffles the values and returns a new list, but also changes the given list"""
    random.shuffle(values)
    return list(values)


def broken_shuffle_5(values):
    """this shuffles the given list of values and returns it"""
    random.shuffle(values)
    return values


def broken_shuffle_6(values):
    """this returns a list of the same length but with unrelated values"""
    new_values = list(range(len(values)))
    random.shuffle(new_values)
    return new_values


def broken_shuffle_7(values):
    """this is broken in a hard to find way..."""
    new_values = []
    while True:
        value_index = random.randrange(0, len(values))
        new_values.append(values.pop(value_index))
        if len(values) == 0:
            break
    return new_values


class TestRandomShuffle(unittest.TestCase):
    """unit tests for the random_shuffle() function"""

    # IMPORTANT NOTE !!!
    # In these tests, just call the random_shuffle() function
    # when you want to call the tested function. Never call any
    # of the "broken_..." functions; those are just here for you
    # to look at. Don't worry, the tests will be run with them as
    # well, using some deep magic ;)

    def test_empty(self):
        """check that giving an empty list results in an empty list"""
        print("empty")
        self.assertCountEqual(random_shuffle([]), [])

    def test_same_length(self):
        """check that the returned list is of the same length as the one givne"""
        print("same")
        values = [1, 1, 1, 1]
        self.assertEqual(len(random_shuffle(values)), 4)

    def test_same_values(self):
        """check that the values in the return list are the same"""
        print("same value")
        values = [1, 1, 1, 1]
        self.assertCountEqual(random_shuffle(values), values)

    def test_values_are_shuffled(self):
        """check that the function does actually return the values in a different order"""
        print("shuffled")
        values = list(range(100))
        values_copy = values.copy()
        self.assertNotEqual(random_shuffle(values), values_copy)

    def test_input_not_mutated(self):
        """check that the input list of values is not mutated"""
        print("mutated")
        values = list(range(100))
        random_shuffle(values)
        self.assertEqual(values, list(range(100)))
