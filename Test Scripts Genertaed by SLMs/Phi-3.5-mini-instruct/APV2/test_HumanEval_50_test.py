You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function. 
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

 Here is the complete unittest test suite for the provided `encode_shift` and `decode_shift` functions:


import unittest
from HumanEval_50_code import encode_shift, decode_shift

class TestShiftFunctions(unittest.TestCase):

    def test_encode_shift(self):
        self.assertEqual(encode_shift('hello'), 'mjqqt')
        self.assertEqual(encode_shift('world'), 'btwqi')
        self.assertEqual(encode_shift('python'), 'udjgtq')
        self.assertEqual(encode_shift(''), '')
        self.assertEqual(encode_shift('a'), 'f')
        self.assertEqual(encode_shift('z'), 'e')
        self.assertEqual(encode_shift('abc'), 'fgh')
        self.assertEqual(encode_shift('xyz'), 'cde')

    def test_decode_shift(self):
        self.assertEqual(decode_shift('mjqqt'), 'hello')
        self.assertEqual(decode_shift('btwqi'), 'world')
        self.assertEqual(decode_shift('udjgtq'), 'python')
        self.assertEqual(decode_shift(''), '')
        self.assertEqual(decode_shift('f'), 'a')
        self.assertEqual(decode_shift('e'), 'z')
        self.assertEqual(decode_shift('fgh'), 'abc')
        self.assertEqual(decode_shift('cde'), 'xyz')

    def test_encode_shift_with_non_alpha(self):
        self.assertEqual(encode_shift('hello123'), 'mjqqt123')
        self.assertEqual(encode_shift('world!'), 'btwqi!')
        self.assertEqual(encode_shift('python3'), 'udjgtq3')
        self.assertEqual(encode_shift(' '), ' ')
        self.assertEqual(encode_shift('#'), '#')

    def test_decode_shift_with_non_alpha(self):
        self.assertEqual(decode_shift('mjqqt123'), 'hello123')
        self.assertEqual(decode_shift('btwqi!'), 'world!')
        self.assertEqual(decode_shift('udjgtq3'), 'python3')
        self.assertEqual(decode_shift(' '), ' ')
        self.assertEqual(decode_shift('#'), '#')

if __name__ == '__main__':
    unittest.main()


This test suite covers various cases, including empty strings, single characters, multiple characters, and strings with non-alphabetic characters. It tests both the `encode_shift` and `decode_shift` functions to ensure they correctly encode and decode strings by shifting characters by 5 in the alphabet.