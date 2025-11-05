You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 Here is a comprehensive unittest test suite for the given Python function `minSubArraySum`. The test cases cover various scenarios such as empty list, positive numbers, negative numbers, and a mix of positive and negative numbers.


import unittest
from HumanEval_114_code import minSubArraySum

class TestMinSubArraySum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(minSubArraySum([]), 0)

    def test_positive_numbers(self):
        self.assertEqual(minSubArraySum([2, 3, 4, 1, 2, 4]), 1)

    def test_negative_numbers(self):
        self.assertEqual(minSubArraySum([-1, -2, -3]), -6)

    def test_negative_and_positive_numbers(self):
        self.assertEqual(minSubArraySum([-1, 2, -3, 4, -5, 6]), 3)

    def test_single_negative_number(self):
        self.assertEqual(minSubArraySum([-1]), 1)

    def test_single_positive_number(self):
        self.assertEqual(minSubArraySum([1]), 1)

if __name__ == '__main__':
    unittest.main()


This test suite includes 6 test cases to cover various scenarios. The test cases are defined as methods within the `TestMinSubArraySum` class, and the `unittest.main()` function is called at the end to run the tests.