system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_51_code import remove_vowels
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """
    return "".join([s for s in text if s.lower() not in ["a", "e", "i", "o", "u"]])assistant

Here is the complete unittest test suite for the `remove_vowels` function:

import unittest
from HumanEval_51_code import remove_vowels

class TestRemoveVowels(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(remove_vowels(""), "")

    def test_no_vowels(self):
        self.assertEqual(remove_vowels("bcdf\nghjklm"), "bcdf\nghjklm")

    def test_all_vowels(self):
        self.assertEqual(remove_vowels("abcdef"), "")

    def test_mixed_vowels(self):
        self.assertEqual(remove_vowels("aaBAA"), "B")

    def test_no_vowels_in_string(self):
        self.assertEqual(remove_vowels("zbcd"), "zbcd")

    def test_multiple_vowels(self):
        self.assertEqual(remove_vowels("aaaaa"), "")

if __name__ == '__main__':
    unittest.main()

This test suite covers the following test cases:

1. An empty string as input
2. A string with no vowels
3. A string with all vowels
4. A string with mixed vowels
5. A string with no vowels
6. A string with multiple vowels

Each test case uses the `assertEqual` method to verify that the output of the `remove_vowels` function matches the expected output.