system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_114_code import minSubArraySum
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    max_sum = 0
    s = 0
    for num in nums:
        s += -num
        if s < 0:
            s = 0
        max_sum = max(s, max_sum)
    if max_sum == 0:
        max_sum = max(-i for i in nums)
    min_sum = -max_sum
    return min_sum


assistant

import unittest

# Importing the function to be tested
from HumanEval_114_code import minSubArraySum

class TestMinSubArraySum(unittest.TestCase):

    def test_minSubArraySum(self):
        # Test case 1
        self.assertEqual(minSubArraySum([2, 3, 4, 1, 2, 4]), 1)

        # Test case 2
        self.assertEqual(minSubArraySum([-1, -2, -3]), -6)

        # Test case 3
        self.assertEqual(minSubArraySum([1, 2, 3, -6, 1]), -6)

        # Test case 4
        self.assertEqual(minSubArraySum([1, 2, 3, 4, 5]), 1)

        # Test case 5
        self.assertEqual(minSubArraySum([-1, -2, -3, -4, -5]), -15)

        # Test case 6
        self.assertEqual(minSubArraySum([10, -10, 10]), 0)

        # Test case 7
        self.assertEqual(minSubArraySum([-1, 2, -1, 2, -1, 2]), 2)

        # Test case 8
        self.assertEqual(minSubArraySum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 1)

    def test_empty_array(self):
        self.assertEqual(minSubArraySum([]), None)  # This is expected behavior as per the problem statement

if __name__ == '__main__':
    unittest.main()


This script defines a `TestMinSubArraySum` class that inherits from `unittest.TestCase`. It contains several test cases to verify the correctness of the `minSubArraySum` function. The `test_minSubArraySum` method includes both positive and negative test cases to ensure the function behaves correctly under various scenarios. Additionally, it handles edge cases such as empty arrays, which are not explicitly mentioned in the problem description but are important to consider when designing a solution.