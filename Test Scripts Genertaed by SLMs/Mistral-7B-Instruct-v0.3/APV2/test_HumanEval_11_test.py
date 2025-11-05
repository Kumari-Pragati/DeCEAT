You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
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

 Here is a complete unittest test suite for the `string_xor` function:


import unittest
from HumanEval_11_code import string_xor

class TestStringXor(unittest.TestCase):

    def test_string_xor_basic(self):
        self.assertEqual(string_xor('010', '110'), '100')
        self.assertEqual(string_xor('101', '010'), '111')
        self.assertEqual(string_xor('100', '010'), '110')
        self.assertEqual(string_xor('000', '000'), '000')
        self.assertEqual(string_xor('111', '111'), '000')

    def test_string_xor_empty(self):
        self.assertEqual(string_xor('', ''), '')
        self.assertEqual(string_xor('', '1'), '1')
        self.assertEqual(string_xor('1', ''), '1')

    def test_string_xor_single_char(self):
        self.assertEqual(string_xor('0', '0'), '0')
        self.assertEqual(string_xor('0', '1'), '1')
        self.assertEqual(string_xor('1', '0'), '1')
        self.assertEqual(string_xor('1', '1'), '0')

    def test_string_xor_long_strings(self):
        self.assertEqual(string_xor('01010101010101010101010101010101', '11010101010101010101010101010101'), '10010101010101010101010101010101')
        self.assertEqual(string_xor('10101010101010101010101010101010101010101', '0101010101010101010101010101010101010101'), '1101010101010101010101010101010101010101')

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases for different scenarios, such as basic XOR operations, empty strings, single characters, and long strings. The test cases are designed to cover a wide range of possible inputs and edge cases.