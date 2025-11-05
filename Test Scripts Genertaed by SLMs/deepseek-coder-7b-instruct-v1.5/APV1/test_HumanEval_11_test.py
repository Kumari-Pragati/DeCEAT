You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_11_code import string_xor

class TestStringXor(unittest.TestCase):

    def test_same_length_strings(self):
        self.assertEqual(string_xor('010', '110'), '100')
        self.assertEqual(string_xor('101', '010'), '111')
        self.assertEqual(string_xor('111', '111'), '000')

    def test_different_length_strings(self):
        self.assertEqual(string_xor('010', '1101'), '1001')
        self.assertEqual(string_xor('101', '01'), '111')
        self.assertEqual(string_xor('111', '11111'), '00010')

    def test_empty_strings(self):
        self.assertEqual(string_xor('', ''), '')
        self.assertEqual(string_xor('', '110'), '110')
        self.assertEqual(string_xor('010', ''), '010')

    def test_strings_with_zeroes_only(self):
        self.assertEqual(string_xor('000', '000'), '000')
        self.assertEqual(string_xor('000', '001'), '001')
        self.assertEqual(string_xor('001', '000'), '001')

    def test_strings_with_ones_only(self):
        self.assertEqual(string_xor('111', '111'), '000')
        self.assertEqual(string_xor('111', '110'), '001')
        self.assertEqual(string_xor('110', '111'), '001')

if __name__ == '__main__':
    unittest.main()


This suite includes tests for different scenarios such as strings of different lengths, empty strings, strings consisting only of 0s or 1s, and strings with equal and unequal values.