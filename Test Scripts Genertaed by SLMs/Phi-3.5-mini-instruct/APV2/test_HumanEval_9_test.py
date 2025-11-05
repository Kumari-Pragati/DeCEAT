You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function. 
Follow all rules carefully.

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

 import unittest
from HumanEval_9_code import rolling_max

class TestRollingMax(unittest.TestCase):

    def test_rolling_max_with_positive_numbers(self):
        self.assertEqual(rolling_max([1, 2, 3, 2, 5]), [1, 2, 3, 3, 5])

    def test_rolling_max_with_empty_list(self):
        self.assertEqual(rolling_max([]), [])

    def test_rolling_max_with_single_element(self):
        self.assertEqual(rolling_max([5]), [5])

    def test_rolling_max_with_negative_numbers(self):
        self.assertEqual(rolling_max([-1, -2, -3, -2, -5]), [-1, -1, -1, -1, -5])

    def test_rolling_max_with_mixed_numbers(self):
        self.assertEqual(rolling_max([1, -2, 3, -2, 5]), [1, 1, 3, 3, 5])

    def test_rolling_max_with_repeated_numbers(self):
        self.assertEqual(rolling_max([1, 1, 1, 1, 1]), [1, 1, 1, 1, 1])

    def test_rolling_max_with_all_same_numbers(self):
        self.assertEqual(rolling_max([7, 7, 7, 7, 7]), [7, 7, 7, 7, 7])

    def test_rolling_max_with_large_numbers(self):
        self.assertEqual(rolling_max([1000000, 2000000, 1500000, 2500000]), [1000000, 2000000, 2000000, 2500000])

if __name__ == '__main__':
    unittest.main()