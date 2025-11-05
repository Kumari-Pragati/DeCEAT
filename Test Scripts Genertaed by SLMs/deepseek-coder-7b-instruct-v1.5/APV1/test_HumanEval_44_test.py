You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_44_code import change_base

class TestChangeBase(unittest.TestCase):
    def test_change_base_positive(self):
        self.assertEqual(change_base(8, 3), '22')
        self.assertEqual(change_base(8, 2), '1000')
        self.assertEqual(change_base(7, 2), '111')

    def test_change_base_zero(self):
        self.assertEqual(change_base(0, 3), '0')
        self.assertEqual(change_base(0, 2), '0')

    def test_change_base_negative(self):
        with self.assertRaises(ValueError):
            change_base(-8, 3)
        with self.assertRaises(ValueError):
            change_base(8, -2)

    def test_change_base_base10(self):
        self.assertEqual(change_base(8, 10), '8')
        self.assertEqual(change_base(7, 10), '7')

    def test_change_base_base16(self):
        self.assertEqual(change_base(16, 16), '10')
        self.assertEqual(change_base(255, 16), 'FF')

if __name__ == '__main__':
    unittest.main()


This suite includes tests for positive numbers, zero, negative numbers, base 10, and base 16. It checks that the function correctly converts numbers to the specified base and that it raises a ValueError when given a negative number or an invalid base.