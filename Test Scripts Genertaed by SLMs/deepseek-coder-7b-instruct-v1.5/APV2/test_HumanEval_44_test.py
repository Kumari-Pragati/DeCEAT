You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_44_code import change_base

class TestChangeBase(unittest.TestCase):

    def test_change_base_to_2(self):
        self.assertEqual(change_base(8, 2), '1000')
        self.assertEqual(change_base(7, 2), '111')

    def test_change_base_to_3(self):
        self.assertEqual(change_base(8, 3), '22')

    def test_change_base_to_10(self):
        self.assertEqual(change_base(8, 10), '8')
        self.assertEqual(change_base(7, 10), '7')

    def test_change_base_to_9(self):
        self.assertEqual(change_base(8, 9), '8')
        self.assertEqual(change_base(7, 9), '7')

    def test_change_base_to_8(self):
        self.assertEqual(change_base(8, 8), '8')
        self.assertEqual(change_base(7, 8), '7')

    def test_change_base_to_7(self):
        self.assertEqual(change_base(8, 7), '7')
        self.assertEqual(change_base(7, 7), '10')

    def test_change_base_to_6(self):
        self.assertEqual(change_base(8, 6), '4')
        self.assertEqual(change_base(7, 6), '5')

    def test_change_base_to_5(self):
        self.assertEqual(change_base(8, 5), '4')
        self.assertEqual(change_base(7, 5), '4')

    def test_change_base_to_4(self):
        self.assertEqual(change_base(8, 4), '2')
        self.assertEqual(change_base(7, 4), '3')

    def test_change_base_to_1(self):
        self.assertEqual(change_base(8, 1), '1')
        self.assertEqual(change_base(7, 1), '1')

    def test_change_base_to_0(self):
        with self.assertRaises(ValueError):
            change_base(8, 0)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for various base conversions, including base 10, which is the default base for integers in Python. It also includes tests for base 1 and 0, which should raise a ValueError.

Please note that the function `change_base` is expected to be in a file named `HumanEval_44_code.py` in the same directory as the test file.