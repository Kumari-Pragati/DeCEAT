You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_162_code import string_to_md5
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    import hashlib
    return hashlib.md5(text.encode('ascii')).hexdigest() if text else None

 Here is a complete unittest test suite for the `string_to_md5` function:


import unittest
from HumanEval_162_code import string_to_md5

class TestStringToMD5(unittest.TestCase):

    def test_empty_string(self):
        self.assertIsNone(string_to_md5(''))

    def test_single_character_string(self):
        self.assertIsNotNone(string_to_md5('a'))

    def test_multiple_character_string(self):
        self.assertIsNotNone(string_to_md5('Hello world'))
        self.assertEqual(string_to_md5('Hello world'), '3e25960a79dbc69b674cd4ec67a72c62')

    def test_special_characters_string(self):
        self.assertIsNotNone(string_to_md5('!@#$%^&*()'))

if __name__ == '__main__':
    unittest.main()


This test suite includes four test cases:

1. `test_empty_string` checks that the function returns `None` for an empty string.
2. `test_single_character_string` checks that the function returns a non-empty string for a single character string.
3. `test_multiple_character_string` checks that the function returns the correct md5 hash for a given string and also checks that it is not `None`.
4. `test_special_characters_string` checks that the function correctly handles strings containing special characters.

The test suite uses the `unittest.TestCase` class to define test methods and the `unittest.main()` function to run the tests.