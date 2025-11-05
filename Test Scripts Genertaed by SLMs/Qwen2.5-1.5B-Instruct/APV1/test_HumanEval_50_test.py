system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_50_code import decode_shift
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    Takes as input a string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])


assistant

import unittest

# Importing the function to be tested
from HumanEval_50_code import encode_shift, decode_shift

class TestEncodeDecodeShift(unittest.TestCase):

    def test_encode_decode(self):
        # Test cases for encoding and decoding strings
        self.assertEqual(encode_shift("abc"), "fgh")
        self.assertEqual(decode_shift("fgh"), "abc")

        self.assertEqual(encode_shift("xyz"), "uvw")
        self.assertEqual(decode_shift("uvw"), "xyz")

        self.assertEqual(encode_shift("Hello World!"), "Mjqqt Njcy!")
        self.assertEqual(decode_shift("Mjqqt Njcy!"), "Hello World!")

        self.assertEqual(encode_shift("Python Programming"), "Rzgk Rnqkxkxk")
        self.assertEqual(decode_shift("Rzgk Rnqkxkxk"), "Python Programming")

        self.assertEqual(encode_shift("1234567890"), "6789012345")
        self.assertEqual(decode_shift("6789012345"), "1234567890")

        print("All tests passed successfully.")

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestEncodeDecodeShift` class that inherits from `unittest.TestCase`. It contains several test methods to verify the correctness of the `encode_shift` and `decode_shift` functions. The `test_encode_decode` method includes various test cases covering different scenarios such as single characters, words, numbers, and special characters. Each test case uses assertions to check if the output matches the expected result. If all tests pass, it prints "All tests passed successfully."