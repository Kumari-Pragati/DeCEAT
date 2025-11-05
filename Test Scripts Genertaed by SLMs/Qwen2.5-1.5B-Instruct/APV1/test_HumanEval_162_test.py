system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
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


assistant

import unittest
from HumanEval_162_code import string_to_md5

class TestStringToMD5(unittest.TestCase):

    def test_string_to_md5(self):
        # Test with non-empty string
        self.assertEqual(string_to_md5("Hello world"), "3e25960a79dbc69b674cd4ec67a72c62")

        # Test with empty string
        self.assertIsNone(string_to_md5(""))

        # Test with None input
        self.assertIsNone(string_to_md5(None))

        # Test with bytes input (should raise TypeError)
        try:
            string_to_md5(b"Bytes")
        except TypeError as e:
            self.assertTrue(str(e).startswith("TypeError: expected str, bytes or bytearray, got"))

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `unittest` test case class `TestStringToMD5` that tests the `string_to_md5` function using various inputs and edge cases. It includes assertions to check both successful conversions and failure scenarios such as handling of empty strings, None values, and byte inputs.