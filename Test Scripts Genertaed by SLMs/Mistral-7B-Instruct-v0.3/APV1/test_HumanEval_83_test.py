You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_83_code import starts_one_ends

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    if n == 1:
        return 1
    return 18 * (10 ** (n - 2))

 Here is a comprehensive unittest test suite for the given Python function `starts_one_ends`. The test suite includes various test cases to cover different scenarios and edge cases.


import unittest
from HumanEval_83_code import starts_one_ends

class TestStartsOneEnds(unittest.TestCase):

    def test_one_digit(self):
        self.assertEqual(starts_one_ends(1), 1)

    def test_two_digits(self):
        self.assertEqual(starts_one_ends(2), 2)

    def test_three_digits(self):
        self.assertEqual(starts_one_ends(3), 18)

    def test_four_digits(self):
        self.assertEqual(starts_one_ends(4), 180)

    def test_five_digits(self):
        self.assertEqual(starts_one_ends(5), 1800)

    def test_zero_digits(self):
        with self.assertRaises(ValueError):
            starts_one_ends(0)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            starts_one_ends(-1)

    def test_large_number(self):
        with self.assertRaises(ValueError):
            starts_one_ends(1000)

if __name__ == '__main__':
    unittest.main()


This test suite covers the following scenarios:

1. One-digit numbers that start or end with 1.
2. Two-digit numbers that start or end with 1.
3. Three-digit numbers that start or end with 1.
4. Four-digit numbers that start or end with 1.
5. Five-digit numbers that start or end with 1.
6. Zero-digit numbers (not valid input).
7. Negative numbers (not valid input).
8. Large numbers (not valid input).