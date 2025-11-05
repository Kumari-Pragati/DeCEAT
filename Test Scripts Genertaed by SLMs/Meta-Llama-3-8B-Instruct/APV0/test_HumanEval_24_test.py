user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_24_code import largest_divisor
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def largest_divisor(n: int) -> int:
    """For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in reversed(range(n)):
        if n % i == 0:
            return iassistant

Here is the unittest test script for the `largest_divisor` function:

import unittest
from HumanEval_24_code import largest_divisor

class TestLargestDivisor(unittest.TestCase):
    def test_largest_divisor(self):
        # Test cases
        self.assertEqual(largest_divisor(15), 5)
        self.assertEqual(largest_divisor(12), 6)
        self.assertEqual(largest_divisor(24), 12)
        self.assertEqual(largest_divisor(25), 25)
        self.assertEqual(largest_divisor(30), 15)
        self.assertEqual(largest_divisor(36), 18)
        self.assertEqual(largest_divisor(48), 24)
        self.assertEqual(largest_divisor(50), 25)
        self.assertEqual(largest_divisor(60), 30)
        self.assertEqual(largest_divisor(72), 36)
        self.assertEqual(largest_divisor(80), 40)
        self.assertEqual(largest_divisor(90), 45)
        self.assertEqual(largest_divisor(100), 50)

        # Test edge cases
        self.assertEqual(largest_divisor(0), 0)
        self.assertEqual(largest_divisor(1), 1)
        self.assertEqual(largest_divisor(-1), 1)
        self.assertEqual(largest_divisor(-5), 5)

        # Test invalid inputs
        with self.assertRaises(TypeError):
            largest_divisor("hello")
        with self.assertRaises(TypeError):
            largest_divisor(None)

if __name__ == '__main__':
    unittest.main()

This script includes a variety of test cases to ensure the `largest_divisor` function is working correctly. It tests the function with positive and negative integers, as well as edge cases like 0 and 1. It also tests the function with invalid inputs, such as strings and None.