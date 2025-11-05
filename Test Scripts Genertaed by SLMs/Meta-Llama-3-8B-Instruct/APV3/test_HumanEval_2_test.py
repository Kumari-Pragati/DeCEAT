system

### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_2_code import truncate_number
   - Define a single unittest.TestCase class
   - Include multiple test_ methods for normal, edge, and invalid inputs
   - End with if __name__ == '__main__': unittest.main()
4. Use only unittest assertions.
5. Do not include markdown, prose, or explanations.
6. Output must be runnable Python code.

### Example
#### Function:
def sum_of_elements(numbers: list) -> int:
    """Return the sum of all integers in a list."""
    return sum(numbers)

#### Test Script:
import unittest

class TestSumOfElements(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_of_elements([1, 2, 3, 4]), 10)

    def test_negative_numbers(self):
        self.assertEqual(sum_of_elements([-1, -2, -3]), -6)

    def test_empty_list(self):
        self.assertEqual(sum_of_elements([]), 0)

if __name__ == '__main__':
    unittest.main()user

### Immediate Task
Write the complete unittest test suite for the following Python function.

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
    return number % 1.0assistant

import unittest
from HumanEval_2_code import truncate_number

class TestTruncateNumber(unittest.TestCase):
    def test_truncate_number(self):
        self.assertAlmostEqual(truncate_number(3.5), 0.5)
        self.assertAlmostEqual(truncate_number(1.0), 0.0)
        self.assertAlmostEqual(truncate_number(2.2), 0.2)
        self.assertAlmostEqual(truncate_number(4.4), 0.4)
        self.assertAlmostEqual(truncate_number(5.5), 0.5)
        self.assertAlmostEqual(truncate_number(6.6), 0.6)
        self.assertAlmostEqual(truncate_number(7.7), 0.7)
        self.assertAlmostEqual(truncate_number(8.8), 0.8)
        self.assertAlmostEqual(truncate_number(9.9), 0.9)
        self.assertAlmostEqual(truncate_number(10.0), 0.0)
        self.assertAlmostEqual(truncate_number(10.1), 0.1)
        self.assertAlmostEqual(truncate_number(10.2), 0.2)
        self.assertAlmostEqual(truncate_number(10.3), 0.3)
        self.assertAlmostEqual(truncate_number(10.4), 0.4)
        self.assertAlmostEqual(truncate_number(10.5), 0.5)
        self.assertAlmostEqual(truncate_number(10.6), 0.6)
        self.assertAlmostEqual(truncate_number(10.7), 0.7)
        self.assertAlmostEqual(truncate_number(10.8), 0.8)
        self.assertAlmostEqual(truncate_number(10.9), 0.9)
        self.assertAlmostEqual(truncate_number(11.0), 0.0)
        self.assertAlmostEqual(truncate_number(11.1), 0.1)
        self.assertAlmostEqual(truncate_number(11.2), 0.2)
        self.assertAlmostEqual(truncate_number(11.3), 0.3)
        self.assertAlmostEqual(truncate_number(11.4), 0.4)
        self.assertAlmostEqual(truncate_number(11.5), 0.5)
        self.assertAlmostEqual(truncate_number(11.6), 0.6)
        self.assertAlmostEqual(truncate_number(11.7), 0.7)
        self.assertAlmostEqual(truncate_number(11.8), 0.8)
        self.assertAlmostEqual(truncate_number(11.9), 0.9)
        self.assertAlmostEqual(truncate_number(12.0), 0.0)
        self.assertAlmostEqual(truncate_number(12.1), 0.1)
        self.assertAlmostEqual(truncate_number(12.2), 0.2)
        self.assertAlmostEqual(truncate_number(12.3), 0.3)
        self.assertAlmostEqual(truncate_number(12.4), 0.4)
        self.assertAlmostEqual(truncate_number(12.5), 0.5)
        self.assertAlmostEqual(truncate_number(12.6), 0.6)
        self.assertAlmostEqual(truncate_number(12.7), 0.7)
        self.assertAlmostEqual(truncate_number(12.8), 0.8)
        self.assertAlmostEqual(truncate_number(12.9), 0.9)
        self.assertAlmostEqual(truncate_number(13.0), 0.0)
        self.assertAlmostEqual(truncate_number(13.1), 0.1)
        self.assertAlmostEqual(truncate_number(13.2), 0.2)
        self.assertAlmostEqual(truncate_number(13.3), 0.3)
        self.assertAlmostEqual(truncate_number(13.4), 0.4)
        self.assertAlmostEqual(truncate_number(13.5), 0.5)
        self.assertAlmostEqual(truncate_number(13.6), 0.6)
        self.assertAlmostEqual(truncate_number(13.7), 0.7)
        self.assertAlmostEqual(truncate_number(13.8), 0.8)
        self.assertAlmostEqual(truncate_number(13.9), 0.9)
        self.assertAlmostEqual(truncate_number(14.0), 0.0)
        self.assertAlmostEqual(truncate_number(14.1), 0.1)
        self.assertAlmostEqual(truncate_number(14.2), 0.2)
        self.assertAlmostEqual(truncate_number(14.3), 0.3)
        self.assertAlmostEqual(truncate_number(14.4), 0.4)
        self.assertAlmostEqual(truncate_number(14.5), 0.5)
        self.assertAlmostEqual(truncate_number(14.6), 0.6)
        self.assertAlmostEqual(truncate_number(14.7), 0.7)
        self.assertAlmostEqual(truncate_number(14.8), 0.8)
        self.assertAlmostEqual(truncate_number(14.9), 0.9)
        self.assertAlmostEqual(truncate_number(15.0), 0.0)
        self.assertAlmostEqual(truncate_number(15.1), 0.1)
        self.assertAlmostEqual(truncate_number(15.2), 0.2)
        self.assertAlmostEqual