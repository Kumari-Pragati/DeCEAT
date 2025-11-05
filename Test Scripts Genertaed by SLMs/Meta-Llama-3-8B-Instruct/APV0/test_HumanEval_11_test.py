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

    return ''.join(xor(x, y) for x, y in zip(a, b))assistant

Here is the unittest test script for the `string_xor` function:

import unittest
from HumanEval_11_code import string_xor

class TestStringXor(unittest.TestCase):
    def test_empty_strings(self):
        self.assertEqual(string_xor("", ""), "")

    def test_single_character_strings(self):
        self.assertEqual(string_xor("1", "1"), "0")
        self.assertEqual(string_xor("1", "0"), "1")
        self.assertEqual(string_xor("0", "1"), "1")
        self.assertEqual(string_xor("0", "0"), "0")

    def test_binary_strings(self):
        self.assertEqual(string_xor("010", "110"), "100")
        self.assertEqual(string_xor("101", "010"), "111")
        self.assertEqual(string_xor("111", "111"), "000")
        self.assertEqual(string_xor("000", "000"), "000")

    def test_non_binary_strings(self):
        with self.assertRaises(ValueError):
            string_xor("hello", "world")

    def test_inconsistent_lengths(self):
        with self.assertRaises(ValueError):
            string_xor("hello", "hello world")

if __name__ == '__main__':
    unittest.main()

This script tests the `string_xor` function with various inputs, including:

1. Empty strings
2. Single-character strings
3. Binary strings (i.e., strings consisting only of 1s and 0s)
4. Non-binary strings (i.e., strings containing characters other than 1s and 0s)
5. Strings with inconsistent lengths (i.e., strings of different lengths)

The script uses the `assertEqual` method to verify that the output of the `string_xor` function matches the expected output for each test case. For non-binary strings and strings with inconsistent lengths, the script uses the `assertRaises` method to verify that the function raises a `ValueError` exception as expected.