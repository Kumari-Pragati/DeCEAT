system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

# Importing the function we want to test
from HumanEval_2_code import truncate_number

class TestTruncateNumber(unittest.TestCase):
    def test_truncate_number(self):
        # Test cases to verify the correctness of the truncate_number function
        self.assertAlmostEqual(truncate_number(3.5), 0.5, places=5)
        self.assertAlmostEqual(truncate_number(7.999), 0.999, places=5)
        self.assertAlmostEqual(truncate_number(4.0), 0.0, places=5)
        self.assertAlmostEqual(truncate_number(1.111), 0.111, places=5)
        self.assertAlmostEqual(truncate_number(0.0), 0.0, places=5)

    def test_edge_cases(self):
        # Edge case tests to ensure edge conditions are handled correctly
        self.assertEqual(truncate_number(0.0), 0.0, "Edge case at zero should return zero")
        self.assertAlmostEqual(truncate_number(-3.5), -3.5, places=5, msg="Negative numbers should also work")

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestTruncateNumber` class that inherits from `unittest.TestCase`. It contains two methods: `test_truncate_number`, which includes several test cases to validate the functionality of the `truncate_number` function, and `test_edge_cases`, which handles edge cases such as negative numbers and zero. The `unittest.main()` call at the end runs all the defined tests when the script is executed directly.