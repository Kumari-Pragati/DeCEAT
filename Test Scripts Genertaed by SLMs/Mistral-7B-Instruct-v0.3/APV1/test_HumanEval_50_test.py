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

 Here is a simple unittest test suite for the `encode_shift` and `decode_shift` functions. I've included some test cases to cover different scenarios, such as lowercase and uppercase letters, numbers, and special characters.


import unittest
from HumanEval_50_code import encode_shift, decode_shift

class TestShiftFunctions(unittest.TestCase):

    def test_encode_shift(self):
        self.assertEqual(encode_shift("hello"), "mjqqt")
        self.assertEqual(encode_shift("Hello"), "MjQQt")
        self.assertEqual(encode_shift("123"), "567")
        self.assertEqual(encode_shift("!@#$%^&*()"), "&*+,-./:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"),

    def test_decode_shift(self):
        self.assertEqual(decode_shift("mjqqt"), "hello")
        self.assertEqual(decode_shift("MjQQt"), "Hello")
        self.assertEqual(decode_shift("567"), "123")
        self.assertEqual(decode_shift("&*+,-./:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"), "!@#$%^&*()")

if __name__ == '__main__':
    unittest.main()


This test suite includes two test cases for each function, one for lowercase and one for uppercase inputs. Additionally, it tests numbers and special characters. Make sure to run this test suite to ensure that the functions work as expected.