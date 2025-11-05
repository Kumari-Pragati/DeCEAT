system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
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


assistant

import unittest

# Define the function to be tested
from HumanEval_11_code import string_xor

class TestStringXOR(unittest.TestCase):
    
    # Test cases for string_xor function
    def test_string_xor(self):
        self.assertEqual(string_xor("010", "110"), "100")
        self.assertEqual(string_xor("101", "011"), "110")
        self.assertEqual(string_xor("000", "000"), "000")
        self.assertEqual(string_xor("111", "000"), "111")
        self.assertEqual(string_xor("000", "111"), "111")

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases that cover various scenarios to ensure the `string_xor` function behaves correctly according to its specification.