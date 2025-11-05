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

 import unittest
from HumanEval_162_code import string_to_md5

class TestStringToMD5(unittest.TestCase):

    def test_empty_string(self):
        self.assertIsNone(string_to_md5(''))

    def test_regular_string(self):
        expected_hash = '3e25960a79dbc69b674cd4ec67a72c62'
        self.assertEqual(string_to_md5('Hello world'), expected_hash)

    def test_special_characters(self):
        expected_hash = '7c211433f020f58aa4e4342f9d7a163d'
        self.assertEqual(string_to_md5('!@#$%^&*()'), expected_hash)

    def test_numeric_string(self):
        expected_hash = 'e4d909c2968c31bd5eabd9cee3d7678e'
        self.assertEqual(string_to_md5('1234567890'), expected_hash)

    def test_whitespace_string(self):
        expected_hash = 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
        self.assertEqual(string_to_md5('    '), expected_hash)

    def test_case_sensitivity(self):
        expected_hash = 'e4d909c2968c31bd5eabd9cee3d7678e'
        self.assertEqual(string_to_md5('Hello'), expected_hash)
        self.assertEqual(string_to_md5('hello'), expected_hash)

    def test_unicode_string(self):
        expected_hash = 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
        self.assertEqual(string_to_md5('你好'), expected_hash)

if __name__ == '__main__':
    unittest.main()