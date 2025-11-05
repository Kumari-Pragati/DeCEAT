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

 Here is a unittest test script for the `encode_shift` and `decode_shift` functions:


import unittest
from HumanEval_50_code import encode_shift, decode_shift

class TestShiftFunctions(unittest.TestCase):

    def test_encode_shift(self):
        self.assertEqual(encode_shift("hello"), "mjqqt")
        self.assertEqual(encode_shift("world"), "nzrhz")
        self.assertEqual(encode_shift("Python"), "Zyuulv")
        self.assertEqual(encode_shift("12345"), "67890")
        self.assertEqual(encode_shift("ABCDE"), "FGHIJ")

    def test_decode_shift(self):
        self.assertEqual(decode_shift("mjqqt"), "hello")
        self.assertEqual(decode_shift("nzrhz"), "world")
        self.assertEqual(decode_shift("Zyuulv"), "Python")
        self.assertEqual(decode_shift("67890"), "12345")
        self.assertEqual(decode_shift("FGHIJ"), "ABCDE")

    def test_special_characters(self):
        self.assertEqual(encode_shift("!@#$%^&*()_+-="), "|?{}[]\:;'<,>.`~")
        self.assertEqual(decode_shift("|?{}[]\:;'<,>.`~"), "!@#$%^&*()_+-=")

    def test_numbers(self):
        self.assertEqual(encode_shift("1234567890"), "654321890723")
        self.assertEqual(decode_shift("654321890723"), "1234567890")

if __name__ == '__main__':
    unittest.main()


This test script includes tests for the `encode_shift` and `decode_shift` functions, covering various cases such as lowercase and uppercase letters, numbers, special characters, and combinations of these. The test cases are designed to ensure that the functions work correctly for the given problem statement.