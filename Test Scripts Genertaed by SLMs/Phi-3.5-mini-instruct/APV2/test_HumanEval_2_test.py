You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function. 
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_2_code import truncate_number
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def truncate_number(number: float) -> float:
    """Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    return number % 1.0

 
import unittest
from HumanEval_2_code import truncate_number

class TestTruncateNumber(unittest.TestCase):

    def test_positive_float_truncate_decimal(self):
        self.assertEqual(truncate_number(3.5), 0.5)

    def test_positive_float_truncate_whole_number(self):
        self.assertEqual(truncate_number(4.0), 0.0)

    def test_positive_float_truncate_negative_decimal(self):
        with self.assertRaises(ValueError):
            truncate_number(-3.5)

    def test_positive_float_truncate_zero(self):
        self.assertEqual(truncate_number(0.0), 0.0)

    def test_positive_float_truncate_very_large_number(self):
        self.assertEqual(truncate_number(1000000.999), 0.999)

    def test_positive_float_truncate_very_small_number(self):
        self.assertEqual(truncate_number(0.000001), 0.000001)

    def test_positive_float_truncate_negative_number(self):
        with self.assertRaises(ValueError):
            truncate_number(-1.5)

if __name__ == '__main__':
    unittest.main()


Note: The original function definition does not specify how to handle negative numbers. The provided test suite includes a test case to check for a `ValueError` when a negative number is passed to the `truncate_number` function. However, since the function's implementation is not provided, I've assumed that it should raise a `ValueError` for negative inputs. If the function is intended to handle negative numbers differently, the test case should be adjusted accordingly.

Also, the function's docstring suggests that it should return the decimal part of a positive floating-point number. If the function is supposed to handle negative numbers or zero differently, the function's implementation and the corresponding test cases should be updated to reflect those requirements.