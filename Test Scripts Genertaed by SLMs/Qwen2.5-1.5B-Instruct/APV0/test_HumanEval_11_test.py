system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
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


assistant

import unittest

# Importing the function to be tested
from HumanEval_11_code import string_xor

class TestStringXOR(unittest.TestCase):
    def test_string_xor(self):
        self.assertEqual(string_xor('010', '110'), '100')
        self.assertEqual(string_xor('111', '000'), '111')
        self.assertEqual(string_xor('000', '111'), '111')
        self.assertEqual(string_xor('101', '011'), '110')

if __name__ == '__main__':
    unittest.main()


This script defines a `TestStringXOR` class that inherits from `unittest.TestCase`. It contains a single method `test_string_xor`, which tests the `string_xor` function with various input pairs. The `assertEqual` methods compare the output of `string_xor` against expected results using the `==` operator. If any assertion fails, it will raise an error indicating what was wrong. Finally, the `unittest.main()` call at the end runs all the tests defined in the `TestStringXOR` class.