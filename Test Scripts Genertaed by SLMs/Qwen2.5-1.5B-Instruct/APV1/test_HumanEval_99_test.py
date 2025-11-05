system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
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


assistant

import unittest

# Function to be tested
from HumanEval_99_code import closest_integer

class TestClosestInteger(unittest.TestCase):

    def test_closest_integer(self):
        self.assertEqual(closest_integer("10"), 10)
        self.assertEqual(closest_integer("15.3"), 15)
        self.assertEqual(closest_integer("14.5"), 15)
        self.assertEqual(closest_integer("-14.5"), -15)
        self.assertEqual(closest_integer("0"), 0)
        self.assertEqual(closest_integer("12.75"), 13)
        self.assertEqual(closest_integer("-12.75"), -13)
        self.assertEqual(closest_integer("12.25"), 12)
        self.assertEqual(closest_integer("-12.25"), -12)
        self.assertEqual(closest_integer("12.5"), 13)
        self.assertEqual(closest_integer("-12.5"), -13)
        self.assertEqual(closest_integer("12.6"), 13)
        self.assertEqual(closest_integer("-12.6"), -13)
        self.assertEqual(closest_integer("12.49999"), 13)
        self.assertEqual(closest_integer("-12.49999"), -13)
        self.assertEqual(closest_integer("12.50001"), 13)
        self.assertEqual(closest_integer("-12.50001"), -13)

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestClosestInteger` class within the `unittest` framework, which contains a single method `test_closest_integer`. This method tests various inputs against the `closest_integer` function using assertions. The `unittest.main()` call at the end of the script runs all the tests defined in this class.