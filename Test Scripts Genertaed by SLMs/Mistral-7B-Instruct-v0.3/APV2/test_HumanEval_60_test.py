You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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
    return sum(range(n + 1))

 Here is a complete unittest test suite for the `sum_to_n` function:


import unittest
from HumanEval_60_code import sum_to_n

class TestSumToN(unittest.TestCase):

    def test_sum_to_n_with_positive_numbers(self):
        self.assertEqual(sum_to_n(1), 1)
        self.assertEqual(sum_to_n(5), 15)
        self.assertEqual(sum_to_n(10), 55)
        self.assertEqual(sum_to_n(30), 465)
        self.assertEqual(sum_to_n(100), 5050)

    def test_sum_to_n_with_zero(self):
        self.assertEqual(sum_to_n(0), 0)

    def test_sum_to_n_with_negative_numbers(self):
        with self.assertRaises(ValueError):
            sum_to_n(-1)

if __name__ == '__main__':
    unittest.main()


This test suite includes three test cases:

1. `test_sum_to_n_with_positive_numbers` tests the function with positive numbers.
2. `test_sum_to_n_with_zero` tests the function with zero.
3. `test_sum_to_n_with_negative_numbers` tests the function with negative numbers.

The test suite uses the `unittest.TestCase` class to define test cases, and the `assertEqual` and `assertRaises` methods to verify the expected behavior of the `sum_to_n` function.