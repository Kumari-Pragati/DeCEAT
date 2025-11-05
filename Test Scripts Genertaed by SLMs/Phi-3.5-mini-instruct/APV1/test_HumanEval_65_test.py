You are an expert Python programmer. 
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 import unittest
from HumanEval_65_code import circular_shift

class TestCircularShift(unittest.TestCase):

    def test_circular_shift_right_one(self):
        self.assertEqual(circular_shift(12, 1), "21")

    def test_circular_shift_right_two(self):
        self.assertEqual(circular_shift(12, 2), "12")

    def test_circular_shift_right_greater_than_digits(self):
        self.assertEqual(circular_shift(123, 4), "321")

    def test_circular_shift_left_one(self):
        self.assertEqual(circular_shift(123, -1), "321")

    def test_circular_shift_left_two(self):
        self.assertEqual(circular_shift(123, -2), "123")

    def test_circular_shift_zero(self):
        self.assertEqual(circular_shift(123, 0), "123")

    def test_circular_shift_negative_shift(self):
        self.assertEqual(circular_shift(123, -1), "321")

    def test_circular_shift_negative_shift_greater_than_digits(self):
        self.assertEqual(circular_shift(123, -4), "321")

    def test_circular_shift_empty_string(self):
        self.assertEqual(circular_shift("", 1), "")

    def test_circular_shift_single_digit(self):
        self.assertEqual(circular_shift(9, 1), "9")

    def test_circular_shift_negative_number(self):
        self.assertEqual(circular_shift(-123, 1), "-213")

    def test_circular_shift_zero_shift(self):
        self.assertEqual(circular_shift(0, 0), "0")

    def test_circular_shift_all_digits(self):
        self.assertEqual(circular_shift(9876543210, 1), "0123456789")

if __name__ == '__main__':
    unittest.main()