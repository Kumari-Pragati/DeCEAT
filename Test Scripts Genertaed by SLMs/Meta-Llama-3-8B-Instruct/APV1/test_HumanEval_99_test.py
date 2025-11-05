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

    # Handle.5 cases — round away from zero
    if abs(num * 10) % 10 == 5:
        return ceil(num) if num > 0 else floor(num)
    else:
        return round(num)assistant

Here is the comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_99_code import closest_integer

class TestClosestInteger(unittest.TestCase):

    def test_closest_integer(self):
        # Test cases for positive numbers
        self.assertEqual(closest_integer("10"), 10)
        self.assertEqual(closest_integer("15.3"), 15)
        self.assertEqual(closest_integer("14.5"), 15)
        self.assertEqual(closest_integer("14.9"), 15)
        self.assertEqual(closest_integer("15.1"), 15)

        # Test cases for negative numbers
        self.assertEqual(closest_integer("-14.5"), -15)
        self.assertEqual(closest_integer("-14.9"), -15)
        self.assertEqual(closest_integer("-15.1"), -15)
        self.assertEqual(closest_integer("-10"), -10)

        # Test cases for zero
        self.assertEqual(closest_integer("0"), 0)

        # Test cases for edge cases
        self.assertEqual(closest_integer("0.5"), 1)
        self.assertEqual(closest_integer("-0.5"), -1)
        self.assertEqual(closest_integer("1.0"), 1)
        self.assertEqual(closest_integer("-1.0"), -1)

        # Test cases for non-numeric inputs
        with self.assertRaises(ValueError):
            closest_integer("abc")
        with self.assertRaises(ValueError):
            closest_integer("123abc")

if __name__ == '__main__':
    unittest.main()


This test suite covers various test cases including positive and negative numbers, zero, edge cases, and non-numeric inputs. The `assertEqual` method is used to check if the output of the function matches the expected output. The `assertRaises` method is used to check if the function raises a `ValueError` when given non-numeric inputs.