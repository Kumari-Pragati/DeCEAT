system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
        # Test case 1: Normal encoding/decoding
        self.assertEqual(encode_shift('abc'), 'fgh')
        self.assertEqual(decode_shift('fgh'), 'abc')

        # Test case 2: Edge cases (empty string)
        self.assertEqual(encode_shift(""), "")
        self.assertEqual(decode_shift(""), "")

        # Test case 3: Case-insensitive characters
        self.assertEqual(encode_shift('Abc'), 'Fgh')
        self.assertEqual(decode_shift('Fgh'), 'Abc')

        # Test case 4: Non-alphabetical characters
        self.assertEqual(encode_shift('Hello!'), 'Mjqqt!')
        self.assertEqual(decode_shift('Mjqqt!'), 'Hello!')

        # Test case 5: Multiple shifts
        self.assertEqual(encode_shift('xyz'), 'abx')
        self.assertEqual(decode_shift('abx'), 'xyz')

        print("All tests passed!")

if __name__ == '__main__':
    unittest.main()


This script imports the necessary functions `encode_shift` and `decode_shift`, then defines a class `TestEncodeDecodeShift` that inherits from `unittest.TestCase`. It contains several test methods to ensure the correctness of both encoding and decoding functions. The `test_encode_decode` method includes various test cases covering different scenarios such as normal strings, empty strings, edge cases, non-alphabetical characters, multiple shifts, etc., ensuring comprehensive testing. Finally, it runs all the tests when executed directly.