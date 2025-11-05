system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
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


assistant

import unittest

# Function to be tested
from HumanEval_9_code import rolling_max

class TestRollingMax(unittest.TestCase):
    def test_rolling_max(self):
        self.assertEqual(rolling_max([1, 2, 3, 2, 5]), [1, 2, 3, 3, 5])
        self.assertEqual(rolling_max([]), [])
        self.assertEqual(rolling_max([-10, -3, -6, -2, 0]), [-10, -3, -3, -3, 0])

if __name__ == '__main__':
    unittest.main()


This script imports `unittest` and defines a test case class `TestRollingMax`. It includes three test methods (`test_rolling_max`) to verify the correctness of the `rolling_max` function using assertions. The `assertEqual` method checks if the output of the function matches the expected results. Finally, it runs the tests when executed as a standalone script.