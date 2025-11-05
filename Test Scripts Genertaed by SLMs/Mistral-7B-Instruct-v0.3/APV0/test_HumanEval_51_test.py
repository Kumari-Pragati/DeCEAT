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
    return "".join([s for s in text if s.lower() not in ["a", "e", "i", "o", "u"]])

 Here is a unittest test script for the `remove_vowels` function:


import unittest
from HumanEval_51_code import remove_vowels

class TestRemoveVowels(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(remove_vowels(""), "")

    def test_single_letter(self):
        for char in ["b", "c", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]:
            self.assertEqual(remove_vowels(char), char)

    def test_multiple_letters(self):
        test_cases = [("abcdef", "bcdf"), ("ghijklm", "ghjklm"), ("aaaaa", ""), ("aaBAA", "B")]
        for test_case in test_cases:
            self.assertEqual(remove_vowels(test_case[0]), test_case[1])

    def test_special_cases(self):
        self.assertEqual(remove_vowels("zbcd"), "zbcd")

if __name__ == '__main__':
    unittest.main()


This script includes a test case for an empty string, single letters, multiple letters, and special cases where the input string does not contain any vowels. You can run this script directly to test the `remove_vowels` function.