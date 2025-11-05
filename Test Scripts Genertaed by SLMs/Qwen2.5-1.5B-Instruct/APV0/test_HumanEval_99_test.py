system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
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

    # Handle .5 cases — round away from zero
    if abs(num * 10) % 10 == 5:
        return ceil(num) if num > 0 else floor(num)
    else:
        return round(num)


assistant

import unittest

# Importing the closest_integer function from the given code snippet
from HumanEval_99_code import closest_integer

class TestClosestInteger(unittest.TestCase):

    def test_closest_integer(self):
        self.assertEqual(closest_integer("10"), 10)
        self.assertEqual(closest_integer("15.3"), 15)
        self.assertEqual(closest_integer("14.5"), 15)
        self.assertEqual(closest_integer("-14.5"), -15)
        self.assertEqual(closest_integer("0"), 0)
        self.assertEqual(closest_integer("-0.5"), -1)
        self.assertEqual(closest_integer("1.5"), 2)
        self.assertEqual(closest_integer("-1.5"), -2)
        self.assertEqual(closest_integer("1e-2"), 0)
        self.assertEqual(closest_integer("1e+2"), 100)
        self.assertEqual(closest_integer("123.456"), 123)
        self.assertEqual(closest_integer("-123.456"), -123)

if __name__ == '__main__':
    unittest.main()


This script defines a `TestClosestInteger` class within the `unittest` framework to test the `closest_integer` function thoroughly. It includes various test cases covering different scenarios as specified in the docstring of the function. The `unittest.main()` call at the end makes the tests executable when run directly.