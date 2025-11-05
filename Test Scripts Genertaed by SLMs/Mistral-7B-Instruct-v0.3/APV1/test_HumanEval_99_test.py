You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 Here is a comprehensive unittest test suite for the given Python function `closest_integer`. The test cases cover a variety of input scenarios, including positive and negative numbers, floating-point numbers, and edge cases like numbers ending in `.5`.


import unittest
from HumanEval_99_code import closest_integer

class TestClosestInteger(unittest.TestCase):

    def test_positive_integer(self):
        self.assertEqual(closest_integer("10"), 10)
        self.assertEqual(closest_integer("100"), 100)
        self.assertEqual(closest_integer("1000"), 1000)

    def test_negative_integer(self):
        self.assertEqual(closest_integer("-10"), -10)
        self.assertEqual(closest_integer("-100"), -100)
        self.assertEqual(closest_integer("-1000"), -1000)

    def test_floating_point_numbers(self):
        self.assertEqual(closest_integer("15.3"), 15)
        self.assertEqual(closest_integer("14.5"), 14)
        self.assertEqual(closest_integer("15.8"), 16)
        self.assertEqual(closest_integer("14.2"), 14)

    def test_edge_cases(self):
        self.assertEqual(closest_integer("15.5"), 16)
        self.assertEqual(closest_integer("-15.5"), -16)
        self.assertEqual(closest_integer("0.5"), 1)
        self.assertEqual(closest_integer("-0.5"), -1)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for positive integers, negative integers, floating-point numbers, and edge cases like numbers ending in `.5`. The test cases are designed to cover a variety of input scenarios and ensure the function behaves as expected.