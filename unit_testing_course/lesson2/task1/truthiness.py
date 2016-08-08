import unittest


class TestIntegerTruthiness(unittest.TestCase):
    def test_zero(self):
        """check that the thruthiness of the integer zero is False"""
        self.assertFalse(0)

    def test_one(self):
        """check that the thruthiness of the integer one is True"""
        self.assertTrue(1)

    def test_other_value(self):
        """check the thruthiness of an integer other than zero"""
        self.assertTrue(3)


class TestNoneTruthiness(unittest.TestCase):
    def test_none(self):
        """check the thruthiness of None"""
        self.assertFalse(None)


class TestContainerTruthiness(unittest.TestCase):
    # Note:
    # -----
    # Methods whose name starts with "_test" are not considered test methods,
    # just like all methods whose name doesn't begin with "test".

    def _test_container_class(self, empty_container, non_empty_container):
        self.assertFalse(empty_container)
        self.assertTrue(non_empty_container)

    def test_list(self):
        self._test_container_class([], [False])

    def test_tuple(self):
        self._test_container_class((), (False,))

    def test_set(self):
        self._test_container_class(set(), {False})

    def test_dict(self):
        self._test_container_class({}, {False: False})
