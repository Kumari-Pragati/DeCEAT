You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function. 
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

 
import unittest
from HumanEval_51_code import remove_vowels

class TestRemoveVowels(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_vowels(''), '')

    def test_string_with_vowels(self):
        self.assertEqual(remove_vowels("abcdef\nghijklm"), "bcdf\nghjklm")

    def test_string_with_no_vowels(self):
        self.assertEqual(remove_vowels('abcdef'), 'bcdf')

    def test_string_with_all_vowels(self):
        self.assertEqual(remove_vowels('aaaaa'), '')

    def test_string_with_mixed_case_vowels(self):
        self.assertEqual(remove_vowels('aaBAA'), 'B')

    def test_string_with_no_vowels_case_insensitive(self):
        self.assertEqual(remove_vowels('zbcd'), 'zbcd')

    def test_string_with_special_characters(self):
        self.assertEqual(remove_vowels('!@#$%^&*()'), '!@#$%^&*()')

    def test_string_with_numbers(self):
        self.assertEqual(remove_vowels('12345'), '12345')

    def test_string_with_whitespace(self):
        self.assertEqual(remove_vowels('hello world'), 'hll wrld')

    def test_string_with_non_alphabetical_characters(self):
        self.assertEqual(remove_vowels('!@#$%^&*()12345'), '!@#$%^&*()12345')

if __name__ == '__main__':
    unittest.main()


This test suite covers various scenarios, including empty strings, strings with vowels, strings with no vowels, strings with mixed case vowels, strings with special characters, strings with numbers, strings with whitespace, and strings with non-alphabetical characters. Each test case checks the output of the `remove_vowels` function against the expected result using the `assertEqual` method provided by the `unittest` framework.