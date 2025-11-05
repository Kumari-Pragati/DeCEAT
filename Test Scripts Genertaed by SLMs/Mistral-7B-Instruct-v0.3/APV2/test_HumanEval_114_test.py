You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

 Here is a complete unittest test suite for the provided function `minSubArraySum`. I've included test cases that cover various scenarios, including empty lists, negative numbers, and positive numbers.


import unittest
from HumanEval_114_code import minSubArraySum

class TestMinSubArraySum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(minSubArraySum([]), 0)

    def test_single_element(self):
        self.assertEqual(minSubArraySum([1]), 1)
        self.assertEqual(minSubArraySum([-1]), -1)

    def test_negative_numbers(self):
        self.assertEqual(minSubArraySum([-1, -2, -3]), -6)
        self.assertEqual(minSubArraySum([-1, 0, -2, 3]), -1)

    def test_positive_numbers(self):
        self.assertEqual(minSubArraySum([2, 3, 4, 1, 2, 4]), 1)
        self.assertEqual(minSubArraySum([2, 1, 1, 2, 3, 4]), 2)

    def test_mixed_numbers(self):
        self.assertEqual(minSubArraySum([-1, 2, 3, -4]), 3)
        self.assertEqual(minSubArraySum([-1, 2, -3, 4]), 1)

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios, such as empty lists, single elements, negative numbers, positive numbers, and mixed numbers. The test suite uses the `unittest.TestCase` class to define test methods with the `test_` prefix, and the `assertEqual` method to compare the expected and actual results. The test suite is run using the `unittest.main()` function.