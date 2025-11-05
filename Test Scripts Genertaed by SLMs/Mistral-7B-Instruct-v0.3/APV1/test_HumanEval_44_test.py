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
    return ret

 Here is a simple unittest test suite for the `change_base` function. I've included tests for various base numbers and edge cases.


import unittest
from HumanEval_44_code import change_base

class TestChangeBase(unittest.TestCase):

    def test_change_base_positive(self):
        self.assertEqual(change_base(8, 3), '22')
        self.assertEqual(change_base(8, 2), '1000')
        self.assertEqual(change_base(7, 2), '111')
        self.assertEqual(change_base(10, 3), '1111')
        self.assertEqual(change_base(15, 4), '3111')
        self.assertEqual(change_base(25, 5), '11001')

    def test_change_base_zero(self):
        self.assertEqual(change_base(0, 2), '0')

    def test_change_base_negative(self):
        self.assertEqual(change_base(-8, 3), '21')
        self.assertEqual(change_base(-8, 2), '1010')
        self.assertEqual(change_base(-7, 2), '110')

    def test_change_base_edge_cases(self):
        self.assertEqual(change_base(1, 2), '1')
        self.assertEqual(change_base(1, 3), '1')
        self.assertEqual(change_base(1, 4), '1')
        self.assertEqual(change_base(1, 5), '1')
        self.assertEqual(change_base(1, 6), '1')
        self.assertEqual(change_base(1, 7), '1')
        self.assertEqual(change_base(1, 8), '1')
        self.assertEqual(change_base(1, 9), '1')
        self.assertEqual(change_base(1, 10), '1')

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for positive numbers, zero, negative numbers, and edge cases where the input number is 1. The test suite checks the function's behavior for various base numbers (2, 3, 4, 5, 6, 7, 8, 9, and 10).