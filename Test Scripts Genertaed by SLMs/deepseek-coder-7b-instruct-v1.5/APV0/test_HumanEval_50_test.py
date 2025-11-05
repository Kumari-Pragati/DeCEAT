You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest script for the given Python functions:


import unittest
from HumanEval_50_code import encode_shift, decode_shift

class TestShift(unittest.TestCase):

    def test_encode_decode(self):
        test_str = "hello"
        encoded = encode_shift(test_str)
        self.assertEqual(decode_shift(encoded), test_str)

    def test_encode_special_chars(self):
        test_str = "hel!lo"
        encoded = encode_shift(test_str)
        self.assertEqual(decode_shift(encoded), test_str)

    def test_encode_upper_case(self):
        test_str = "Hello"
        encoded = encode_shift(test_str)
        self.assertEqual(decode_shift(encoded), test_str.lower())

    def test_encode_empty_string(self):
        test_str = ""
        encoded = encode_shift(test_str)
        self.assertEqual(decode_shift(encoded), test_str)

if __name__ == '__main__':
    unittest.main()


This script includes 4 tests:

1. `test_encode_decode`: Tests if the encoding and decoding functions work together correctly.
2. `test_encode_special_chars`: Tests if the functions work with special characters.
3. `test_encode_upper_case`: Tests if the functions work with upper case letters.
4. `test_encode_empty_string`: Tests if the functions work with an empty string.

Please note that the `HumanEval_50_code` module should contain the `encode_shift` and `decode_shift` functions for these tests to work.