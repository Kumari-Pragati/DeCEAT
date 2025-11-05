You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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
    return "".join([s for s in text if s.lower() not in ["a", "e", "i", "o", "u"]])


### Response:
Here is the unittest test suite for the given Python function:


import unittest
from HumanEval_51_code import remove_vowels

class TestRemoveVowels(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_vowels(''), '')

    def test_string_with_vowels(self):
        self.assertEqual(remove_vowels('abcdef\nghijklm'), 'bcdf\nghjklm')

    def test_string_without_vowels(self):
        self.assertEqual(remove_vowels('abcdef'), 'bcdf')

    def test_all_vowels(self):
        self.assertEqual(remove_vowels('aaaaa'), '')

    def test_mixed_case_vowels(self):
        self.assertEqual(remove_vowels('aaBAA'), 'B')

    def test_no_vowels(self):
        self.assertEqual(remove_vowels('zbcd'), 'zbcd')


if __name__ == '__main__':
    unittest.main()


This test suite includes tests for various scenarios including empty strings, strings with vowels, strings without vowels, strings with all vowels, strings with mixed case vowels, and strings without vowels at all.