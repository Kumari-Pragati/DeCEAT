You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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

 Here is a complete unittest test suite for the `largest_divisor` function:


import unittest
from HumanEval_24_code import largest_divisor

class TestLargestDivisor(unittest.TestCase):

    def test_largest_divisor(self):
        self.assertEqual(largest_divisor(1), 1)
        self.assertEqual(largest_divisor(2), 2)
        self.assertEqual(largest_divisor(3), 3)
        self.assertEqual(largest_divisor(4), 2)
        self.assertEqual(largest_divisor(5), 5)
        self.assertEqual(largest_divisor(6), 6)
        self.assertEqual(largest_divisor(7), 7)
        self.assertEqual(largest_divisor(8), 4)
        self.assertEqual(largest_divisor(9), 3)
        self.assertEqual(largest_divisor(10), 5)
        self.assertEqual(largest_divisor(15), 5)
        self.assertEqual(largest_divisor(16), 8)
        self.assertEqual(largest_divisor(17), 1)
        self.assertEqual(largest_divisor(18), 6)
        self.assertEqual(largest_divisor(19), 1)
        self.assertEqual(largest_divisor(20), 4)
        self.assertEqual(largest_divisor(21), 7)
        self.assertEqual(largest_divisor(22), 11)
        self.assertEqual(largest_divisor(23), 1)
        self.assertEqual(largest_divisor(24), 8)
        self.assertEqual(largest_divisor(25), 5)
        self.assertEqual(largest_divisor(26), 13)
        self.assertEqual(largest_divisor(27), 3)
        self.assertEqual(largest_divisor(28), 4)
        self.assertEqual(largest_divisor(29), 1)
        self.assertEqual(largest_divisor(30), 2)

if __name__ == '__main__':
    unittest.main()


This test suite includes a test function `test_largest_divisor` that checks the function's behavior for various input values. The test function uses the `assertEqual` method to verify that the function's output matches the expected output for each test case.