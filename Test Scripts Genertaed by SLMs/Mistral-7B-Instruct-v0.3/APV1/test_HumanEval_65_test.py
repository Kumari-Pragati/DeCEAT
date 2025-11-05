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

 Here is a comprehensive unittest test suite for the given Python function `circular_shift`.


import unittest
from HumanEval_65_code import circular_shift

class TestCircularShift(unittest.TestCase):

    def test_positive_shift(self):
        """Test circular shift with positive shift"""
        self.assertEqual(circular_shift(12, 1), "21")
        self.assertEqual(circular_shift(1234, 2), "3412")
        self.assertEqual(circular_shift(123456, 3), "345612")
        self.assertEqual(circular_shift(1234567, 4), "5671234")
        self.assertEqual(circular_shift(12345678, 5), "67812345")
        self.assertEqual(circular_shift(123456789, 6), "789123456")
        self.assertEqual(circular_shift(1234567890, 7), "8901234567")

    def test_zero_shift(self):
        """Test circular shift with zero shift"""
        self.assertEqual(circular_shift(12, 0), "12")
        self.assertEqual(circular_shift(1234, 0), "1234")
        self.assertEqual(circular_shift(123456, 0), "123456")
        self.assertEqual(circular_shift(1234567, 0), "1234567")
        self.assertEqual(circular_shift(12345678, 0), "12345678")
        self.assertEqual(circular_shift(123456789, 0), "123456789")
        self.assertEqual(circular_shift(1234567890, 0), "1234567890")

    def test_negative_shift(self):
        """Test circular shift with negative shift"""
        self.assertEqual(circular_shift(12, -1), "12")
        self.assertEqual(circular_shift(1234, -2), "4123")
        self.assertEqual(circular_shift(123456, -3), "561234")
        self.assertEqual(circular_shift(1234567, -4), "7123456")
        self.assertEqual(circular_shift(12345678, -5), "85671234")
        self.assertEqual(circular_shift(123456789, -6), "901234567")
        self.assertEqual(circular_shift(1234567890, -7), "0123456789")

    def test_shift_greater_than_number_of_digits(self):
        """Test circular shift with shift greater than number of digits"""
        self.assertEqual(circular_shift(12, 2), "12")
        self.assertEqual(circular_shift(1234, 5), "4321")
        self.assertEqual(circular_shift(123456, 7), "612345")
        self.assertEqual(circular_shift(1234567, 8), "7123456")
        self.assertEqual(circular_shift(12345678, 9), "81234567")
        self.assertEqual(circular_shift(123456789, 10), "912345678")
        self.assertEqual(circular_shift(1234567890, 11), "0123456789")

if __name__ == '__main__':
    unittest.main()