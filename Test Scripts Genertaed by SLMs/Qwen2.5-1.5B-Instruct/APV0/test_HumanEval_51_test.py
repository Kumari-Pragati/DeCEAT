system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
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
    return "".join([s for s in text if s.lower() not in ["a", "e", "i", "o", "u"]])


assistant

import unittest

# Function to be tested
from HumanEval_51_code import remove_vowels

class TestRemoveVowels(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_vowels(""), "")

    def test_multiple_lines(self):
        self.assertEqual(remove_vowels("abcdef\nghijklm"), "bcdf\nghjklm")

    def test_single_char(self):
        self.assertEqual(remove_vowels("abcdef"), "bcdf")

    def test_all_same_case(self):
        self.assertEqual(remove_vowels("aaaaa"), "")
    
    def test_with_special_chars(self):
        self.assertEqual(remove_vowels("aaBAA"), "B")

    def test_with_uppercase(self):
        self.assertEqual(remove_vowels("zbcd"), "zbcd")

if __name__ == '__main__':
    unittest.main()


This script imports `unittest` and defines a class `TestRemoveVowels` within it. Each method of this class tests a specific case of the `remove_vowels` function using assertions. The `assertEqual` method checks whether the output of the function matches the expected result. Finally, the `unittest.main()` call runs all the tests defined in the class.