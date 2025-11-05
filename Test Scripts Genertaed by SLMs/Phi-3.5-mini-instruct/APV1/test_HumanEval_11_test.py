You are an expert Python programmer. 
Your task is to write a comprehensive unittest test suite for the given Python function.

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

class TestStringXOR(unittest.TestCase):

    def test_string_xor_equal_length(self):
        self.assertEqual(string_xor('010', '110'), '100')

    def test_string_xor_unequal_length(self):
        with self.assertRaises(ValueError):
            string_xor('0101', '110')

    def test_string_xor_empty_strings(self):
        self.assertEqual(string_xor('', ''), '')

    def test_string_xor_all_zeros(self):
        self.assertEqual(string_xor('000', '000'), '000')

    def test_string_xor_all_ones(self):
        self.assertEqual(string_xor('111', '111'), '000')

    def test_string_xor_mixed_zeros_ones(self):
        self.assertEqual(string_xor('0101', '1100'), '1011')

    def test_string_xor_single_character(self):
        self.assertEqual(string_xor('0', '1'), '1')
        self.assertEqual(string_xor('1', '0'), '1')

    def test_string_xor_long_strings(self):
        self.assertEqual(string_xor('0101010101', '1100110011'), '1001100110')

    def test_string_xor_same_string(self):
        self.assertEqual(string_xor('0101010101', '0101010101'), '0000000000')

    def test_string_xor_non_binary_strings(self):
        with self.assertRaises(ValueError):
            string_xor('abc', '110')

if __name__ == '__main__':
    unittest.main()