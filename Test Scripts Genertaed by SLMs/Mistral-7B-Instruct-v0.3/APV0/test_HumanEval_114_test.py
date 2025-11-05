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

 Here is a unittest test script for the provided function `minSubArraySum`. The test cases cover various scenarios, including an empty list, a list with only negative numbers, a list with only positive numbers, a list with a mix of positive and negative numbers, and a list with a single zero.


import unittest
from HumanEval_114_code import minSubArraySum

class TestMinSubArraySum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(minSubArraySum([]), 0)

    def test_all_negative(self):
        self.assertEqual(minSubArraySum([-1, -2, -3]), -6)

    def test_all_positive(self):
        self.assertEqual(minSubArraySum([1, 2, 3, 4]), 1)

    def test_mix_positive_negative(self):
        self.assertEqual(minSubArraySum([2, -3, 4, -1, 2, 4]), 1)

    def test_single_zero(self):
        self.assertEqual(minSubArraySum([0]), 0)

if __name__ == '__main__':
    unittest.main()


This script includes a test case for an empty list, a list with only negative numbers, a list with only positive numbers, a list with a mix of positive and negative numbers, and a list with a single zero. You can run this script directly to test the `minSubArraySum` function.