import unittest

from hello_someone import hello_someone


class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_someone("World"), "Hello, World!")
