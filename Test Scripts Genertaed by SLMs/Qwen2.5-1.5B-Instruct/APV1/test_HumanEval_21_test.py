system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_21_code import rescale_to_unit
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    min_number = min(numbers)
    max_number = max(numbers)
    return [(x - min_number) / (max_number - min_number) for x in numbers]


assistant

import unittest

# Importing the function we want to test
from HumanEval_21_code import rescale_to_unit

class TestRescaleToUnit(unittest.TestCase):
    def test_rescale_to_unit(self):
        # Test case 1: Normal input
        result = rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        self.assertEqual(result, [0.0, 0.25, 0.5, 0.75, 1.0])

        # Test case 2: Single element input
        result = rescale_to_unit([10.0])
        self.assertEqual(result, [0.0])

        # Test case 3: Empty list input
        result = rescale_to_unit([])
        self.assertEqual(result, [])

        # Test case 4: All elements are the same
        result = rescale_to_unit([1.0] * 6)
        self.assertEqual(result, [0.0, 0.25, 0.5, 0.75, 1.0, 1.0])

        # Test case 5: Randomly generated inputs
        random_numbers = [float(i) for i in range(10)]
        result = rescale_to_unit(random_numbers)
        expected_result = [(x - min(random_numbers)) / (max(random_numbers) - min(random_numbers)) for x in random_numbers]
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestRescaleToUnit` class within the `unittest` module, which contains several test cases for the `rescale_to_unit` function. Each test case uses assertions to verify if the output matches the expected results. The `assertEqual` method checks if the actual result matches the expected result. If any assertion fails, it raises an error indicating what went wrong.