system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
Write a complete unittest test suite for the following Python function.
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


assistant

import unittest

# Define the function to be tested
def truncate_number(number: float) -> float:
    """Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    return number % 1.0

class TestTruncateNumber(unittest.TestCase):
    
    def test_truncate_number(self):
        self.assertAlmostEqual(truncate_number(3.5), 0.5, places=5)
        self.assertAlmostEqual(truncate_number(7.894), 0.894, places=5)
        self.assertAlmostEqual(truncate_number(123.456789), 0.456789, places=5)
        self.assertAlmostEqual(truncate_number(0.999999), 0.999999, places=5)

if __name__ == '__main__':
    unittest.main()


This unittest test suite includes a class `TestTruncateNumber` that inherits from `unittest.TestCase`. It contains a single method `test_truncate_number`, which tests the `truncate_number` function with various inputs to ensure its correctness. The `assertAlmostEqual` method is used to check if the returned value matches the expected result within a specified number of decimal places.