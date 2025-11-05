user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_97_code import multiply
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.

    Examples:
    multiply(148, 412) ➞ 16
    multiply(19, 28) ➞ 72
    multiply(2020, 1851) ➞ 0
    multiply(14, -15) ➞ 20
    """

    return abs(a % 10) * abs(b % 10)assistant

Here is the unittest test script for the `multiply` function:

import unittest
from HumanEval_97_code import multiply

class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        # Test cases
        self.assertEqual(multiply(148, 412), 16)
        self.assertEqual(multiply(19, 28), 72)
        self.assertEqual(multiply(2020, 1851), 0)
        self.assertEqual(multiply(14, -15), 20)
        self.assertEqual(multiply(-14, 15), 20)
        self.assertEqual(multiply(-14, -15), 20)
        self.assertEqual(multiply(0, 0), 0)
        self.assertEqual(multiply(0, 1), 0)
        self.assertEqual(multiply(1, 0), 0)
        self.assertEqual(multiply(1, 1), 1)
        self.assertEqual(multiply(-1, -1), 1)
        self.assertEqual(multiply(-1, 1), 1)
        self.assertEqual(multiply(1, -1), 1)

    def test_invalid_input(self):
        # Test cases with invalid input (e.g. non-integer values)
        with self.assertRaises(TypeError):
            multiply("hello", 42)
        with self.assertRaises(TypeError):
            multiply(42, "world")

if __name__ == '__main__':
    unittest.main()

This script defines a `TestMultiply` class that contains two test methods: `test_multiply` and `test_invalid_input`.

The `test_multiply` method tests the `multiply` function with various input values, including positive and negative integers, and checks that the output is correct.

The `test_invalid_input` method tests the `multiply` function with invalid input values, such as non-integer values, and checks that a `TypeError` is raised.

You can run this script directly to execute the tests.