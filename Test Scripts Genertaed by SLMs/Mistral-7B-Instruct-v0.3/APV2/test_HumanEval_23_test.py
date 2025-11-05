You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_23_code import strlen
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def strlen(string: str) -> int:
    """Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

 Here is a complete unittest test suite for the `strlen` function:


import unittest
from HumanEval_23_code import strlen

class TestStrlen(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(strlen(''), 0)

    def test_single_character_string(self):
        self.assertEqual(strlen('a'), 1)
        self.assertEqual(strlen('z'), 1)

    def test_multi_character_string(self):
        self.assertEqual(strlen('abc'), 3)
        self.assertEqual(strlen('xyz'), 3)

    def test_long_string(self):
        long_string = 'abcdefghijklmnopqrstuvwxyz' * 10
        self.assertEqual(strlen(long_string), 260)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for an empty string, single character strings, multi-character strings, and long strings. It uses the `assertEqual` method to compare the expected and actual results.