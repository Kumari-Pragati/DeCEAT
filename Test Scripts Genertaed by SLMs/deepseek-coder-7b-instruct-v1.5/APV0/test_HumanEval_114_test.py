You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_114_code import minSubArraySum

class TestMinSubArraySum(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(minSubArraySum([2, 3, 4, 1, 2, 4]), 1)

    def test_negative_numbers(self):
        self.assertEqual(minSubArraySum([-1, -2, -3]), -6)

    def test_mixed_numbers(self):
        self.assertEqual(minSubArraySum([2, -3, 4, -1, 2, -4]), 1)

    def test_single_number(self):
        self.assertEqual(minSubArraySum([5]), 5)

    def test_zeroes(self):
        self.assertEqual(minSubArraySum([0, 0, 0]), 0)

    def test_empty_list(self):
        self.assertEqual(minSubArraySum([]), 0)

if __name__ == '__main__':
    unittest.main()


This script creates a unittest class `TestMinSubArraySum` that contains several test methods. Each method tests a specific scenario. The `assertEqual` function is used to check if the output of `minSubArraySum` function matches the expected result.

Please note that the function `minSubArraySum` is not defined in the script. You should replace `from HumanEval_114_code import minSubArraySum` with the actual location of your function.

Also, the function `minSubArraySum` is designed to find the minimum sum of any non-empty sub-array of `nums`. The provided test cases cover various scenarios, including positive numbers, negative numbers, mixed numbers, single number, zeroes, and an empty list.