Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 Here is a unittest test script for the `string_to_md5` function:


import unittest
from HumanEval_162_code import string_to_md5

class TestStringToMD5(unittest.TestCase):

    def test_empty_string(self):
        self.assertIsNone(string_to_md5(''))

    def test_single_character_string(self):
        self.assertIsNotNone(string_to_md5('a'))

    def test_multiple_characters_string(self):
        self.assertIsNotNone(string_to_md5('Hello world'))
        self.assertIsNotNone(string_to_md5('abcdefghijklmnopqrstuvwxyz'))

    def test_special_characters_string(self):
        self.assertIsNotNone(string_to_md5('!@#$%^&*()_+-=[]{}|;:'\''".,<>/?'))

    def test_case_sensitive_string(self):
        self.assertIsNotNone(string_to_md5('HelloWorld'))
        self.assertNotEqual(string_to_md5('HelloWorld'), string_to_md5('helloWorld'))

    def test_md5_output(self):
        self.assertEqual(string_to_md5('Hello world'), '3e25960a79dbc69b674cd4ec67a72c62')
        self.assertEqual(string_to_md5('abcdefghijklmnopqrstuvwxyz'), '9eb105dd7c0f11498ead9080a3dd25f2')

if __name__ == '__main__':
    unittest.main()


This test script includes various test cases to ensure that the `string_to_md5` function works correctly for different inputs, including empty strings, single character strings, multiple character strings, strings with special characters, and case-sensitive strings. It also tests the output of the function for specific inputs to ensure that it generates the correct MD5 hash.