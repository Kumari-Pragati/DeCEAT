system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
Write a complete unittest test suite for the following Python function.
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


assistant

import unittest

# Provided function
from HumanEval_9_code import rolling_max

# Test class
class RollingMaxTest(unittest.TestCase):
    
    def test_rolling_max(self):
        # Test case 1
        self.assertEqual(rolling_max([1, 2, 3, 2, 5]), [1, 2, 3, 3, 5])
        
        # Test case 2
        self.assertEqual(rolling_max([]), [])
        
        # Test case 3
        self.assertEqual(rolling_max([-10, -3, -6, -2, -8]), [-10, -3, -6, -6, -8])

if __name__ == '__main__':
    unittest.main()


This test suite includes three test cases to verify the correctness of the `rolling_max` function.