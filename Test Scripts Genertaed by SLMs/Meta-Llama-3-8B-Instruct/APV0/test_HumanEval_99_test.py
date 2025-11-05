user

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

    # Handle.5 cases — round away from zero
    if abs(num * 10) % 10 == 5:
        return ceil(num) if num > 0 else floor(num)
    else:
        return round(num)assistant

Here is a unittest test script for the `closest_integer` function:

import unittest
from HumanEval_99_code import closest_integer

class TestClosestInteger(unittest.TestCase):
    def test_integer_values(self):
        self.assertEqual(closest_integer("10"), 10)
        self.assertEqual(closest_integer("15"), 15)
        self.assertEqual(closest_integer("14"), 14)
        self.assertEqual(closest_integer("-14"), -14)

    def test_decimal_values(self):
        self.assertEqual(closest_integer("15.3"), 15)
        self.assertEqual(closest_integer("14.5"), 15)
        self.assertEqual(closest_integer("-14.5"), -15)
        self.assertEqual(closest_integer("0.5"), 1)
        self.assertEqual(closest_integer("-0.5"), -1)

    def test_edge_cases(self):
        self.assertEqual(closest_integer("0"), 0)
        self.assertEqual(closest_integer("-0"), -0)
        self.assertEqual(closest_integer("1.0"), 1)
        self.assertEqual(closest_integer("-1.0"), -1)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            closest_integer("not a number")
        with self.assertRaises(ValueError):
            closest_integer("inf")

if __name__ == '__main__':
    unittest.main()

This test script covers the following cases:

1. Integer values: Test that the function returns the correct integer value for inputs like "10", "15", etc.
2. Decimal values: Test that the function handles decimal values correctly, including cases where the input is exactly halfway between two integers (e.g. "14.5").
3. Edge cases: Test that the function handles edge cases like 0, -0, 1.0, and -1.0 correctly.
4. Invalid input: Test that the function raises a `ValueError` when given invalid input like "not a number" or "inf".

You can run this script directly to see the test results.