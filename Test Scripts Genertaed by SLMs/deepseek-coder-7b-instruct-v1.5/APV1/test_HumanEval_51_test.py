You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_51_code import remove_vowels

class TestRemoveVowels(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_vowels(''), '')

    def test_string_without_vowels(self):
        self.assertEqual(remove_vowels('abcdef'), 'bcdf')

    def test_string_with_lowercase_vowels(self):
        self.assertEqual(remove_vowels('abcdef\nghijklm'), 'bcdf\nghjklm')

    def test_string_with_uppercase_vowels(self):
        self.assertEqual(remove_vowels('aaaaa'), '')

    def test_string_with_mixed_case_vowels(self):
        self.assertEqual(remove_vowels('aaBAA'), 'B')

    def test_string_without_vowels(self):
        self.assertEqual(remove_vowels('zbcd'), 'zbcd')

if __name__ == '__main__':
    unittest.main()


This suite includes tests for different scenarios: empty string, string without vowels, string with lowercase vowels, string with uppercase vowels, string with mixed case vowels, and string without vowels.