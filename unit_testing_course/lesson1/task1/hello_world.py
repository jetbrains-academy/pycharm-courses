# this is the function that we will be testing
def hello_world():
    implement this function!


# import the unittest module, which we will use to write our tests
import unittest


# With unittest, tests are grouped as methods of classes.
# Each such class must be a sub-class of 'unittest.TestCase'.
# And that's about all you need to know about these classes!
class TestHelloWorld(unittest.TestCase):
    """Tests for the hello_world() function"""

    # Each test is written as a method with a name beginning with "test_"
    def test_return_value(self):
        # Writing a doc-string for each test, explaining what it tests,
        # is a good idea.
        """test that hello_world() returns 'Hello, World!'"""

        # self.assertEqual() will make the test fail if the arguments are not equal.
        self.assertEqual(hello_world(), "Hello, World!")

        # If no assertions fail, the test passes successfully. Note that this
        # happens automatically; we don't have to return a value or anything
        # of the sort.
