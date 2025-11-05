You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_65_code import circular_shift
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    s = str(x)
    if shift > len(s):
        return s[::-1]
    else:
        return s[len(s) - shift:] + s[:len(s) - shift]


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_65_code import circular_shift

class TestCircularShift(unittest.TestCase):

    def test_single_digit(self):
        self.assertEqual(circular_shift(1, 1), "1")

    def test_multiple_digits(self):
        self.assertEqual(circular_shift(123, 1), "312")
        self.assertEqual(circular_shift(123, 2), "231")
        self.assertEqual(circular_shift(123, 3), "123")
        self.assertEqual(circular_shift(123, 4), "321")

    def test_large_shift(self):
        self.assertEqual(circular_shift(123, 4), "321")

    def test_zero_shift(self):
        self.assertEqual(circular_shift(123, 0), "123")

    def test_negative_shift(self):
        self.assertEqual(circular_shift(123, -1), "213")

if __name__ == '__main__':
    unittest.main()


This script tests the function with different scenarios:

- Single digit numbers
- Multiple digit numbers with shifts less than, equal to, and greater than the number of digits
- Large shifts (greater than the number of digits)
- Zero shift
- Negative shift

The test cases cover all the possible scenarios that the function could be tested with.