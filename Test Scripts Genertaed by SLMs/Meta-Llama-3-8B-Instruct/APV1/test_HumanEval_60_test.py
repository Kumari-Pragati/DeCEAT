user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_60_code import sum_to_n
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
    return sum(range(n + 1))assistant

Here is the comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_60_code import sum_to_n

class TestSumToN(unittest.TestCase):

    def test_sum_to_n_positive_numbers(self):
        self.assertEqual(sum_to_n(1), 1)
        self.assertEqual(sum_to_n(5), 15)
        self.assertEqual(sum_to_n(10), 55)
        self.assertEqual(sum_to_n(30), 465)
        self.assertEqual(sum_to_n(100), 5050)

    def test_sum_to_n_negative_numbers(self):
        with self.assertRaises(TypeError):
            sum_to_n(-1)

    def test_sum_to_n_non_integer_numbers(self):
        with self.assertRaises(TypeError):
            sum_to_n(3.5)

    def test_sum_to_n_zero(self):
        self.assertEqual(sum_to_n(0), 0)

    def test_sum_to_n_large_numbers(self):
        self.assertEqual(sum_to_n(1000), 500500)

if __name__ == '__main__':
    unittest.main()


This test suite includes the following test cases:

- `test_sum_to_n_positive_numbers`: Tests the function with positive integers.
- `test_sum_to_n_negative_numbers`: Tests the function with negative integers to ensure it raises a TypeError.
- `test_sum_to_n_non_integer_numbers`: Tests the function with non-integer numbers to ensure it raises a TypeError.
- `test_sum_to_n_zero`: Tests the function with zero to ensure it returns the correct result.
- `test_sum_to_n_large_numbers`: Tests the function with large numbers to ensure it returns the correct result.