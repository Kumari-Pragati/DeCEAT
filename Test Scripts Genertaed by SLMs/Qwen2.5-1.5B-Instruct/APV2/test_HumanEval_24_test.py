system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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
            return i


assistant

import unittest

# Function to be tested
from HumanEval_24_code import largest_divisor

class TestLargestDivisor(unittest.TestCase):
    
    def test_largest_divisor(self):
        # Test cases to verify correctness of the function
        self.assertEqual(largest_divisor(15), 5)
        self.assertEqual(largest_divisor(28), 7)
        self.assertEqual(largest_divisor(100), 50)
        self.assertEqual(largest_divisor(13), 1)
        self.assertEqual(largest_divisor(1), 1)

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases to ensure the `largest_divisor` function works correctly across different inputs.