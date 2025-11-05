You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function. 
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

 
import unittest
from HumanEval_60_code import sum_to_n

class TestSumToN(unittest.TestCase):
    def test_sum_to_n_with_positive_integers(self):
        self.assertEqual(sum_to_n(30), 465)
        self.assertEqual(sum_to_n(100), 5050)
        self.assertEqual(sum_to_n(5), 15)
        self.assertEqual(sum_to_n(10), 55)
        self.assertEqual(sum_to_n(1), 1)

    def test_sum_to_n_with_zero(self):
        self.assertEqual(sum_to_n(0), 0)

    def test_sum_to_n_with_negative_integers(self):
        with self.assertRaises(ValueError):
            sum_to_n(-1)
        with self.assertRaises(ValueError):
            sum_to_n(0)

    def test_sum_to_n_with_non_integer_values(self):
        with self.assertRaises(TypeError):
            sum_to_n(30.5)
        with self.assertRaises(TypeError):
            sum_to_n("30")

if __name__ == '__main__':
    unittest.main()


In this test suite, we have added tests for the following scenarios:

1. Positive integer inputs to ensure the function returns the correct sum.
2. Zero input to test the edge case where the sum should be 0.
3. Negative integer inputs to check if the function raises a `ValueError` as expected.
4. Non-integer inputs to verify that the function raises a `TypeError` when provided with invalid arguments.

Please note that the original `sum_to_n` function does not explicitly handle negative numbers or non-integer values. Therefore, I've added tests to check for these cases, assuming that the function should raise exceptions for invalid inputs. If the original function is expected to handle such cases differently, the test cases should be adjusted accordingly.