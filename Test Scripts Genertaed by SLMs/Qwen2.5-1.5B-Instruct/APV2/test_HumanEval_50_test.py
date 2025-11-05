system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

# Provided functions
from HumanEval_50_code import encode_shift, decode_shift

class TestEncodeDecode(unittest.TestCase):

    def test_encode_decode(self):
        # Test cases for encoding and decoding
        self.assertEqual(encode_shift('abc'), 'fgh')
        self.assertEqual(decode_shift('fgh'), 'abc')

        self.assertEqual(encode_shift('xyz'), 'abc')
        self.assertEqual(decode_shift('abc'), 'xyz')

        self.assertEqual(encode_shift('Hello World!'), 'Mjqqt Bmmlqg!')
        self.assertEqual(decode_shift('Mjqqt Bmmlqg!'), 'Hello World!')

        self.assertEqual(encode_shift('Zebra Horse'), 'Fkxjv Jnbsl')
        self.assertEqual(decode_shift('Fkxjv Jnbsl'), 'Zebra Horse')

        print("All tests passed!")

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases that cover various scenarios including uppercase letters, lowercase letters, punctuation, and spaces. It ensures that both `encode_shift` and `decode_shift` functions work correctly across different inputs.