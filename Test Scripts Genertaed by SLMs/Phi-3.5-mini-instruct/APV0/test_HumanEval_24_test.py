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

 import unittest
from HumanEval_24_code import largest_divisor

class TestLargestDivisor(unittest.TestCase):

    def test_largest_divisor_positive_integer(self):
        self.assertEqual(largest_divisor(15), 5)

    def test_largest_divisor_one(self):
        self.assertEqual(largest_divisor(1), None)

    def test_largest_divisor_negative_integer(self):
        self.assertEqual(largest_divisor(-15), None)

    def test_largest_divisor_zero(self):
        self.assertEqual(largest_divisor(0), None)

    def test_largest_divisor_even_number(self):
        self.assertEqual(largest_divisor(12), 6)

    def test_largest_divisor_prime_number(self):
        self.assertEqual(largest_divisor(7), None)

    def test_largest_divisor_multiple_of_n(self):
        self.assertEqual(largest_divisor(20), 10)

    def test_largest_divisor_smallest_positive_integer(self):
        self.assertEqual(largest_divisor(1), None)

if __name__ == '__main__':
    unittest.main()