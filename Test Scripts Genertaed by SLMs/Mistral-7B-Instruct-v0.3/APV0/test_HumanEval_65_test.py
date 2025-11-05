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

 Here is a unittest test script for the `circular_shift` function:


import unittest
from HumanEval_65_code import circular_shift

class TestCircularShift(unittest.TestCase):
    def test_positive_shift(self):
        self.assertEqual(circular_shift(12, 1), "21")
        self.assertEqual(circular_shift(1234, 2), "3412")
        self.assertEqual(circular_shift(123456, 3), "345612")
        self.assertEqual(circular_shift(1234567, 4), "5671234")
        self.assertEqual(circular_shift(123456789, 5), "678912345")
        self.assertEqual(circular_shift(1234567890, 6), "7890123456")
        self.assertEqual(circular_shift(12345678901, 7), "890112345678")

    def test_zero(self):
        self.assertEqual(circular_shift(0, 1), "0")
        self.assertEqual(circular_shift(0, 2), "0")
        self.assertEqual(circular_shift(0, 3), "0")
        self.assertEqual(circular_shift(0, 4), "0")
        self.assertEqual(circular_shift(0, 5), "0")
        self.assertEqual(circular_shift(0, 6), "0")
        self.assertEqual(circular_shift(0, 7), "0")

    def test_negative_shift(self):
        self.assertEqual(circular_shift(-12, 1), "-21")
        self.assertEqual(circular_shift(-1234, 2), "-1234")
        self.assertEqual(circular_shift(-123456, 3), "-561234")
        self.assertEqual(circular_shift(-1234567, 4), "-6712345")
        self.assertEqual(circular_shift(-123456789, 5), "-912345678")
        self.assertEqual(circular_shift(-1234567890, 6), "-0123456789")
        self.assertEqual(circular_shift(-12345678901, 7), "-901234567890")

    def test_shift_greater_than_number_of_digits(self):
        self.assertEqual(circular_shift(12, 5), "12")
        self.assertEqual(circular_shift(1234, 5), "1234")
        self.assertEqual(circular_shift(123456, 7), "123456")
        self.assertEqual(circular_shift(1234567, 8), "1234567")
        self.assertEqual(circular_shift(123456789, 9), "123456789")
        self.assertEqual(circular_shift(1234567890, 10), "1234567890")
        self.assertEqual(circular_shift(12345678901, 11), "12345678901")

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to cover different scenarios, such as positive shifts, zero, negative shifts, and shifts greater than the number of digits. It also tests the edge case where the input is a negative number.