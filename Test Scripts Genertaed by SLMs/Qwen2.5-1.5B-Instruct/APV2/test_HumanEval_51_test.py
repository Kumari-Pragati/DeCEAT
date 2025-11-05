system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
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


assistant

import unittest

# Provided function to be tested
from HumanEval_51_code import remove_vowels

class TestRemoveVowels(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_vowels(""), "")

    def test_single_char(self):
        self.assertEqual(remove_vowels("a"), "")
        self.assertEqual(remove_vowels("b"), "b")

    def test_multiple_chars(self):
        self.assertEqual(remove_vowels("abcde"), "bcde")
        self.assertEqual(remove_vowels("hello world"), "hll wrld")

    def test_lowercase_input(self):
        self.assertEqual(remove_vowels("Hello World!"), "Hll Wrld!")

    def test_uppercase_input(self):
        self.assertEqual(remove_vowels("HELLO WORLD!"), "HLLO WRLD!")

    def test_punctuation(self):
        self.assertEqual(remove_vowels("Hi, how are you?"), "H, h vw r y?")
        self.assertEqual(remove_vowels("No vowels here..."), "N hvrs hcrr")

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for various edge cases including empty strings, single characters, multiple characters, lowercase and uppercase input, and punctuation. It uses assertEqual methods to check if the function behaves as expected across different scenarios.