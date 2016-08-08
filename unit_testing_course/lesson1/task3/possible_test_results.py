import unittest


class TestPossibleResults(unittest.TestCase):
    def test_success(self):
        pass

    def test_failure(self):
        self.assertEqual(True, False)

    def test_error(self):
        raise Exception()
