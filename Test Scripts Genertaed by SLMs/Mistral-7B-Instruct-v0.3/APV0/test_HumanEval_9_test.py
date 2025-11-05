Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_9_code import rolling_max
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def rolling_max(numbers: List[int]) -> List[int]:
    """Return a list where each element is the maximum of all elements up to that index.
    >>> rolling_max([1, 2, 3, 2, 5])
    [1, 2, 3, 3, 5]
    >>> rolling_max([])
    []
    """
    result: List[int] = []
    running_max = None
    for n in numbers:
        if running_max is None:
            running_max = n
        else:
            running_max = max(running_max, n)
        result.append(running_max)
    return result

 Here is a unittest test script for the `rolling_max` function:


import unittest
from HumanEval_9_code import rolling_max

class TestRollingMax(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(rolling_max([]), [])

    def test_single_element(self):
        self.assertEqual(rolling_max([1]), [1])

    def test_multiple_elements(self):
        self.assertEqual(rolling_max([1, 2, 3, 2, 5]), [1, 2, 3, 3, 5])

    def test_negative_numbers(self):
        self.assertEqual(rolling_max([-1, -2, -3, -2, -5]), [-1, -1, -2, -2, -2])

    def test_duplicate_numbers(self):
        self.assertEqual(rolling_max([1, 1, 2, 1, 5]), [1, 1, 2, 2, 5])

    def test_large_numbers(self):
        self.assertEqual(rolling_max([1000000001, 1000000002, 1000000003, 1000000002, 1000000001]),
                         [1000000001, 1000000002, 1000000003, 1000000003, 1000000001])

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases for different scenarios, such as an empty list, a single element, multiple elements, negative numbers, duplicate numbers, and large numbers. It uses the `unittest.TestCase` class to define test methods and the `unittest.main()` function to run the tests.