You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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
    return ret

 Here is a complete unittest test suite for the `change_base` function:


import unittest
from HumanEval_44_code import change_base

class TestChangeBase(unittest.TestCase):

    def test_change_base_simple_cases(self):
        self.assertEqual(change_base(8, 3), '22')
        self.assertEqual(change_base(8, 2), '1000')
        self.assertEqual(change_base(7, 2), '111')
        self.assertEqual(change_base(10, 2), '1010')
        self.assertEqual(change_base(15, 3), '12')
        self.assertEqual(change_base(23, 5), '131')

    def test_change_base_zero(self):
        self.assertEqual(change_base(0, 2), '0')

    def test_change_base_negative(self):
        self.assertEqual(change_base(-1, 2), '17')

    def test_change_base_large_numbers(self):
        self.assertEqual(change_base(123456, 8), '177777')
        self.assertEqual(change_base(123456, 16), '373a')

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases for different inputs and edge cases. It covers positive numbers, zero, negative numbers, and large numbers. The test cases are designed to ensure that the `change_base` function works correctly for the given requirements.