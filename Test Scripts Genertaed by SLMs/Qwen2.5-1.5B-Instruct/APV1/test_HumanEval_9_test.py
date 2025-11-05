system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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


assistant

import unittest

# Function to be tested
from HumanEval_9_code import rolling_max

class TestRollingMax(unittest.TestCase):
    def test_rolling_max(self):
        # Test case 1: Positive integers
        self.assertEqual(rolling_max([1, 2, 3, 2, 5]), [1, 2, 3, 3, 5])

        # Test case 2: Empty list
        self.assertEqual(rolling_max([]), [])

        # Test case 3: Negative integers
        self.assertEqual(rolling_max([-10, -2, -3, -2, -5]), [-10, -2, -3, -3, -5])

        # Test case 4: Mixed positive and negative integers
        self.assertEqual(rolling_max([1, -2, 3, -2, 5]), [1, -2, 3, 3, 5])

        # Test case 5: Single-element list
        self.assertEqual(rolling_max([7]), [7])

    def test_edge_cases(self):
        # Test case 6: All elements are equal
        self.assertEqual(rolling_max([1, 1, 1, 1, 1]), [1, 1, 1, 1, 1])

        # Test case 7: Only one element
        self.assertEqual(rolling_max([42]), [42])

        # Test case 8: Zero as input (though not directly applicable due to type hinting)
        self.assertEqual(rolling_max([0]), [0])

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestRollingMax` class within the `unittest` framework, which contains two test methods: `test_rolling_max` and `test_edge_cases`. The `test_rolling_max` method tests various scenarios including positive integers, empty lists, negative integers, mixed types, single-element lists, and edge cases like all elements being equal or only having one element. The `test_edge_cases` method includes additional checks for zero as an input, though it's noted that this might not be directly applicable due to the type hinting. The `unittest.main()` call at the end runs these tests when the script is executed.