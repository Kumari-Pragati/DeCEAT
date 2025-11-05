system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_0_code import has_close_elements
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = abs(elem - elem2)
                if distance < threshold:
                    return True
    return False


assistant

import unittest

# Provided function
from HumanEval_0_code import has_close_elements

class TestHasCloseElements(unittest.TestCase):

    def test_case_1(self):
        self.assertFalse(has_close_elements([1.0, 2.0, 3.0], 0.5))

    def test_case_2(self):
        self.assertTrue(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))

    def test_case_3(self):
        self.assertFalse(has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0], 0.6))

    def test_case_4(self):
        self.assertTrue(has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0], 0.1))

if __name__ == '__main__':
    unittest.main()


This test suite includes four test cases that cover various scenarios as specified in the `has_close_elements` function documentation. Each test case uses the `assertFalse` or `assertTrue` method based on whether the expected outcome matches the actual result returned by the function.