import unittest


class TestIntegerTruthiness(unittest.TestCase):
    def test_zero(self):
        """check that the thruthiness of the integer zero is False"""
        write this test!

    def test_one(self):
        """check that the thruthiness of the integer one is True"""
        write this test!

    def test_other_value(self):
        """check the thruthiness of an integer other than zero"""
        write this test!


class TestNoneTruthiness(unittest.TestCase):
    def test_none(self):
        """check the thruthiness of None"""
        self.assertMethodName(None)


class TestContainerTruthiness(unittest.TestCase):
    # Note:
    # -----
    # Methods whose name starts with "_test" are not considered test methods,
    # just like all methods whose name doesn't begin with "test".

    def _test_container_class(self, empty_container, non_empty_container):
        self.assertchoose the proper assetion method(empty_container)
        self.assertchoose the proper assetion method(non_empty_container)

    def test_list(self):
        implement this test using _test_container_class()

    def test_tuple(self):
        implement this test using _test_container_class()

    def test_set(self):
        implement this test using _test_container_class()

    def test_dict(self):
        implement this test using _test_container_class()
