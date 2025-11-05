user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

Here is the unittest test script for the `remove_vowels` function:

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

    def test_no_vowels_at_all(self):
        self.assertEqual(remove_vowels("zbcd"), "zbcd")

    def test_multiple_vowels(self):
        self.assertEqual(remove_vowels("aaaaa"), "")

    def test_mixed_case(self):
        self.assertEqual(remove_vowels("AaEoIu"), "")

    def test_newline(self):
        self.assertEqual(remove_vowels("abcdef\nghijklm"), "bcdf\nghjklm")

    def test_multiple_lines(self):
        self.assertEqual(remove_vowels("abcdef\nghijklm\nnopqrst"), "bcdf\nghjklm\nnopqrst")

if __name__ == '__main__':
    unittest.main()

This script defines a `TestRemoveVowels` class with 8 test methods, each testing a specific scenario or edge case. The `assertEqual` method is used to verify that the output of the `remove_vowels` function matches the expected output.

You can run this script directly to execute the tests and verify that the `remove_vowels` function is working correctly.