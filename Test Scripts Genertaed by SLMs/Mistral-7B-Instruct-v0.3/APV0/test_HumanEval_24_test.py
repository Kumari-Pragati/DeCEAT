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
            return i

 Here is a simple unittest test script for the `largest_divisor` function. I've included some test cases to cover different scenarios, such as even and odd numbers, prime numbers, and numbers close to the square root of a perfect square.


import unittest
from HumanEval_24_code import largest_divisor

class TestLargestDivisor(unittest.TestCase):
    def test_largest_divisor(self):
        self.assertEqual(largest_divisor(15), 5)
        self.assertEqual(largest_divisor(20), 4)
        self.assertEqual(largest_divisor(21), 7)
        self.assertEqual(largest_divisor(28), 4)
        self.assertEqual(largest_divisor(49), 7)
        self.assertEqual(largest_divisor(625), 25)
        self.assertEqual(largest_divisor(1000), 10)
        self.assertEqual(largest_divisor(17), 17)  # Prime number
        self.assertEqual(largest_divisor(2), 2)
        self.assertEqual(largest_divisor(0), 0)
        self.assertEqual(largest_divisor(-15), 15)

if __name__ == '__main__':
    unittest.main()


This script defines a test case class `TestLargestDivisor` with a method `test_largest_divisor`. Inside this method, we test the `largest_divisor` function with various input values. The `unittest.main()` function is called at the end to run the tests.