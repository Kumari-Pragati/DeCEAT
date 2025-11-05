You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function. 
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_11_code import string_xor
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    def xor(i: str, j: str) -> str:
        if i == j:
            return '0'
        else:
            return '1'

    return ''.join(xor(x, y) for x, y in zip(a, b))

 
import unittest
from HumanEval_11_code import string_xor

class TestStringXor(unittest.TestCase):

    def test_string_xor_same_length(self):
        self.assertEqual(string_xor('010', '110'), '100')

    def test_string_xor_different_lengths(self):
        self.assertEqual(string_xor('0101', '110'), '1011')

    def test_string_xor_empty_strings(self):
        self.assertEqual(string_xor('', '110'), '110')
        self.assertEqual(string_xor('010', ''), '010')

    def test_string_xor_single_character(self):
        self.assertEqual(string_xor('0', '1'), '1')
        self.assertEqual(string_xor('1', '0'), '1')

    def test_string_xor_all_zeros(self):
        self.assertEqual(string_xor('0000', '0000'), '0000')

    def test_string_xor_all_ones(self):
        self.assertEqual(string_xor('1111', '1111'), '0000')

    def test_string_xor_mixed_zeros_ones(self):
        self.assertEqual(string_xor('0101', '1100'), '1001')

    def test_string_xor_long_strings(self):
        self.assertEqual(string_xor('0101010101', '1101010101'), '1000100010')

    def test_string_xor_strings_with_leading_zeros(self):
        self.assertEqual(string_xor('00001010', '11001010'), '11000000')

    def test_string_xor_strings_with_trailing_zeros(self):
        self.assertEqual(string_xor('1010', '0100'), '1110')

if __name__ == '__main__':
    unittest.main()


This test suite covers various scenarios for the `string_xor` function, including strings of different lengths, empty strings, single-character strings, strings with all zeros or all ones, mixed strings, and strings with leading or trailing zeros. It ensures that the function behaves correctly for all these cases.