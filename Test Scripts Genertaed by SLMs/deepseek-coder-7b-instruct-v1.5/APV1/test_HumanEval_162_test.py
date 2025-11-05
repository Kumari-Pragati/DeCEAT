You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_162_code import string_to_md5

class TestStringToMD5(unittest.TestCase):
    def test_empty_string(self):
        self.assertIsNone(string_to_md5(''))

    def test_hello_world(self):
        self.assertEqual(string_to_md5('Hello world'), '3e25960a79dbc69b674cd4ec67a72c62')

    def test_non_ascii_string(self):
        self.assertIsNone(string_to_md5('非ASCII字符串'))

    def test_long_string(self):
        long_string = 'a' * 10000
        self.assertEqual(len(string_to_md5(long_string)), 32)

if __name__ == '__main__':
    unittest.main()


This test suite includes four tests:

1. `test_empty_string`: Tests that the function returns `None` when given an empty string.
2. `test_hello_world`: Tests that the function returns the correct MD5 hash for the string 'Hello world'.
3. `test_non_ascii_string`: Tests that the function correctly handles non-ASCII strings.
4. `test_long_string`: Tests that the function can handle long strings by checking the length of the returned hash.

Please note that the `test_non_ascii_string` test is expected to fail, because the `string_to_md5` function does not handle non-ASCII strings correctly. This is a limitation of the `hashlib.md5` function, which only accepts ASCII strings.