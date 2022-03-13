from rearrnage import rearrange_name  # importing the rearrange_name function from the rearrange module

import unittest  # include class and methods that less easily creating testing functions under the TestCase class


class TestRearrange(unittest.TestCase):  # our class inhert functions from TestCase
    # Any methods we define in our TestRearrange class that start with the prefix test will automatically become tests that can be run by the testing framework.
    def test_basic(self):
        testcase = "Love, ada"
        expected = "ada Love"
        self.assertEqual(rearrange_name(testcase), expected)
        # assertEqual basiclly check that both args are equal we inhert this from the unittest.Testcase

    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)


unittest.main()
