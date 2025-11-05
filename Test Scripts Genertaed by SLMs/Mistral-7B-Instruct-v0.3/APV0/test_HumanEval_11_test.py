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

 Here is a unittest test script for the `string_xor` function:


import unittest
from HumanEval_11_code import string_xor

class TestStringXor(unittest.TestCase):
    def test_string_xor(self):
        self.assertEqual(string_xor('010', '110'), '100')
        self.assertEqual(string_xor('101', '010'), '111')
        self.assertEqual(string_xor('10101010', '11111111'), '00000000')
        self.assertEqual(string_xor('', '1'), '1')
        self.assertEqual(string_xor('1', ''), '1')
        self.assertEqual(string_xor('1', '1'), '0')

if __name__ == '__main__':
    unittest.main()


This test script includes a test case for the `string_xor` function with various inputs. It checks that the function correctly performs binary XOR on the given strings and returns the expected results. The test cases cover different scenarios such as empty strings, strings of different lengths, and strings with only one character.