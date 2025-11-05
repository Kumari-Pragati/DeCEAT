user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_44_code import change_base
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    ret = ""
    while x > 0:
        ret = str(x % base) + ret
        x //= base
    return retassistant

Here is the comprehensive unittest test suite for the given Python function:


import unittest
from HumanEval_44_code import change_base

class TestChangeBase(unittest.TestCase):

    def test_change_base_valid(self):
        self.assertEqual(change_base(8, 3), '22')
        self.assertEqual(change_base(8, 2), '1000')
        self.assertEqual(change_base(7, 2), '111')
        self.assertEqual(change_base(10, 2), '1010')
        self.assertEqual(change_base(15, 8), '17')
        self.assertEqual(change_base(20, 10), '20')

    def test_change_base_invalid_base(self):
        with self.assertRaises(ValueError):
            change_base(8, 11)
        with self.assertRaises(ValueError):
            change_base(8, 12)

    def test_change_base_invalid_input(self):
        with self.assertRaises(TypeError):
            change_base('8', 2)
        with self.assertRaises(TypeError):
            change_base(8.5, 2)

    def test_change_base_edge_cases(self):
        self.assertEqual(change_base(0, 2), '0')
        self.assertEqual(change_base(1, 2), '1')
        self.assertEqual(change_base(9, 2), '1001')

if __name__ == '__main__':
    unittest.main()


This test suite covers the following scenarios:

1. Valid inputs: Test the function with valid inputs, including edge cases.
2. Invalid base: Test the function with invalid base values (greater than 10).
3. Invalid input: Test the function with invalid input types (non-integer, float).
4. Edge cases: Test the function with edge cases, such as input 0 and input 1.

Note that the `assertRaises` method is used to test the function's behavior when invalid inputs are provided.