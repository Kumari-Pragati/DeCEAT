You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function. 
Follow all rules carefully.

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

    def test_positive_fraction_less_than_half(self):
        self.assertEqual(closest_integer("15.3"), 15)

    def test_positive_fraction_equal_to_half(self):
        self.assertEqual(closest_integer("14.5"), 15)

    def test_negative_fraction_equal_to_half(self):
        self.assertEqual(closest_integer("-14.5"), -15)

    def test_negative_integer(self):
        self.assertEqual(closest_integer("-10"), -10)

    def test_zero(self):
        self.assertEqual(closest_integer("0"), 0)

    def test_fraction_greater_than_half(self):
        self.assertEqual(closest_integer("15.6"), 16)

    def test_very_large_positive_fraction(self):
        self.assertEqual(closest_integer("1000000000000000.1"), 1000000000000000)

    def test_very_large_negative_fraction(self):
        self.assertEqual(closest_integer("-1000000000000000.1"), -1000000000000000)

    def test_empty_string(self):
        self.assertEqual(closest_integer(""), 0)

    def test_non_numeric_string(self):
        with self.assertRaises(ValueError):
            closest_integer("abc")

if __name__ == '__main__':
    unittest.main()


Note: The original function `closest_integer` does not handle non-numeric strings and will raise a `ValueError` if such input is provided. The test case `test_non_numeric_string` assumes that the function should raise a `ValueError` when a non-numeric string is passed. If the function is expected to handle such cases differently, the test case should be adjusted accordingly.