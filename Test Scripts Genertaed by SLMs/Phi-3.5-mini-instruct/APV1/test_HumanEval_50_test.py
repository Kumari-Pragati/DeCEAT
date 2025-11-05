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

 import unittest
from HumanEval_50_code import encode_shift, decode_shift

class TestShiftFunctions(unittest.TestCase):

    def test_encode_shift_with_lowercase(self):
        self.assertEqual(encode_shift('hello'), 'mjqqt')

    def test_encode_shift_with_uppercase(self):
        self.assertEqual(encode_shift('HELLO'), 'MJQQT')

    def test_encode_shift_with_mixed_case(self):
        self.assertEqual(encode_shift('Hello'), 'Mjqqt')

    def test_decode_shift_with_lowercase(self):
        self.assertEqual(decode_shift('mjqqt'), 'hello')

    def test_decode_shift_with_uppercase(self):
        self.assertEqual(decode_shift('MJQQT'), 'HELLO')

    def test_decode_shift_with_mixed_case(self):
        self.assertEqual(decode_shift('Mjqqt'), 'hello')

    def test_encode_shift_with_empty_string(self):
        self.assertEqual(encode_shift(''), '')

    def test_decode_shift_with_empty_string(self):
        self.assertEqual(decode_shift(''), '')

    def test_encode_shift_with_non_alphabetic_characters(self):
        self.assertEqual(encode_shift('abc123'), 'fgh678')

    def test_decode_shift_with_non_alphabetic_characters(self):
        self.assertEqual(decode_shift('fgh678'), 'abc123')

    def test_encode_shift_with_single_character(self):
        self.assertEqual(encode_shift('a'), 'f')

    def test_decode_shift_with_single_character(self):
        self.assertEqual(decode_shift('f'), 'a')

    def test_encode_shift_with_long_string(self):
        self.assertEqual(encode_shift('abcdefghijklmnopqrstuvwxyz'), 'fghijklmnopqrstuvwxyz')

    def test_decode_shift_with_long_string(self):
        self.assertEqual(decode_shift('fghijklmnopqrstuvwxyz'), 'abcdefghijklmnopqrstuvwxyz')

if __name__ == '__main__':
    unittest.main()