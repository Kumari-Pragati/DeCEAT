You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
Here is a unittest script for the given Python function:


import unittest
from HumanEval_11_code import string_xor

class TestStringXor(unittest.TestCase):
    def test_string_xor(self):
        self.assertEqual(string_xor('010', '110'), '100')
        self.assertEqual(string_xor('111', '000'), '111')
        self.assertEqual(string_xor('101010', '010101'), '111111')
        self.assertEqual(string_xor('111111', '111111'), '000000')
        self.assertEqual(string_xor('000000', '000000'), '000000')
        self.assertEqual(string_xor('111111', '000000'), '111111')
        self.assertEqual(string_xor('000000', '111111'), '111111')
        self.assertEqual(string_xor('1010101010', '0101010101'), '1111111111')

if __name__ == '__main__':
    unittest.main()


This script tests the `string_xor` function with a variety of inputs to ensure it's working correctly. Each test case compares the output of the function to the expected result. If any of these tests fail, the unittest framework will report the failure.