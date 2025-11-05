system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
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


assistant

import unittest
from HumanEval_162_code import string_to_md5

class TestStringToMD5(unittest.TestCase):

    def test_string_to_md5(self):
        self.assertEqual(string_to_md5('Hello world'), '3e25960a79dbc69b674cd4ec67a72c62')
        self.assertIsNone(string_to_md5(''))
        self.assertIsNone(string_to_md5(None))
        self.assertIsNone(string_to_md5(123))

if __name__ == '__main__':
    unittest.main()


This script imports `unittest` and `string_to_md5`, then defines a class `TestStringToMD5` that inherits from `unittest.TestCase`. It includes two test cases to verify the functionality of `string_to_md5`: one case checks the expected output for a non-empty string, another checks for an empty string, and a third checks for a non-string input (like 123). The `assertEqual` method is used to compare the actual result of `string_to_md5` with the expected result in each test case. Finally, it calls `unittest.main()` to run all tests when the script is executed directly.