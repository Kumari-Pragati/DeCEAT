Generate a unittest test script for the following Python function. 
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_99_code import closest_integer
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples:
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15
    >>> closest_integer("14.5")
    15
    >>> closest_integer("-14.5")
    -15
    '''

    from math import floor, ceil

    # Clean up string
    value = value.strip()
    num = float(value)

    # Handle .5 cases — round away from zero
    if abs(num * 10) % 10 == 5:
        return ceil(num) if num > 0 else floor(num)
    else:
        return round(num)

 import unittest
from HumanEval_99_code import closest_integer

class TestClosestInteger(unittest.TestCase):

    def test_positive_integer(self):
        self.assertEqual(closest_integer("10"), 10)

    def test_positive_float_less_than_one(self):
        self.assertEqual(closest_integer("15.3"), 15)

    def test_positive_float_equal_to_one(self):
        self.assertEqual(closest_integer("1.0"), 1)

    def test_positive_float_greater_than_one(self):
        self.assertEqual(closest_integer("15.7"), 16)

    def test_negative_float_less_than_zero(self):
        self.assertEqual(closest_integer("-14.3"), -14)

    def test_negative_float_equal_to_zero(self):
        self.assertEqual(closest_integer("-0.0"), 0)

    def test_negative_float_greater_than_zero(self):
        self.assertEqual(closest_integer("-15.5"), -16)

    def test_equidistant_case(self):
        self.assertEqual(closest_integer("14.5"), 15)
        self.assertEqual(closest_integer("-14.5"), -15)

    def test_empty_string(self):
        self.assertEqual(closest_integer(""), 0)

    def test_non_numeric_string(self):
        self.assertEqual(closest_integer("abc"), 0)

    def test_very_large_number(self):
        self.assertEqual(closest_integer("1e100"), 1e100)

    def test_very_small_number(self):
        self.assertEqual(closest_integer("1e-100"), 0)

if __name__ == '__main__':
    unittest.main()