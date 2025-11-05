You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_50_code import encode_shift, decode_shift

class TestShiftCipher(unittest.TestCase):
    def test_encode_decode(self):
        s = "hello"
        encoded = encode_shift(s)
        decoded = decode_shift(encoded)
        self.assertEqual(decoded, s)

    def test_encode_shift(self):
        s = "abc"
        expected = "fgh"
        self.assertEqual(encode_shift(s), expected)

    def test_decode_shift(self):
        s = "fgh"
        expected = "abc"
        self.assertEqual(decode_shift(s), expected)

    def test_encode_shift_special_chars(self):
        s = "!@#"
        expected = "!@#"
        self.assertEqual(encode_shift(s), expected)

    def test_decode_shift_special_chars(self):
        s = "!@#"
        expected = "!@#"
        self.assertEqual(decode_shift(s), expected)

    def test_encode_shift_upper_case(self):
        s = "ABC"
        expected = "FGH"
        self.assertEqual(encode_shift(s), expected)

    def test_decode_shift_upper_case(self):
        s = "FGH"
        expected = "ABC"
        self.assertEqual(decode_shift(s), expected)

if __name__ == '__main__':
    unittest.main()


This suite includes tests for encoding and decoding a simple string, encoding and decoding strings with special characters, and encoding and decoding strings with upper-case letters.

Please note that the `HumanEval_50_code` module should contain the `encode_shift` and `decode_shift` functions for these tests to pass.