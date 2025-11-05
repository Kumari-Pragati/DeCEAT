You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_145_code import order_by_points

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    def digits_sum(n):
        neg = 1
        if n < 0:
            n, neg = -1 * n, -1
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg
        return sum(n)

    return sorted(nums, key=digits_sum)


### Response:
Here is the unittest test suite for the given Python function:


import unittest
from HumanEval_145_code import order_by_points

class TestOrderByPoints(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(order_by_points([]), [])

    def test_positive_numbers(self):
        self.assertEqual(order_by_points([1, 11, 22, 33]), [1, 11, 22, 33])

    def test_negative_numbers(self):
        self.assertEqual(order_by_points([-1, -11, -22, -33]), [-33, -22, -11, -1])

    def test_mixed_numbers(self):
        self.assertEqual(order_by_points([1, 11, -1, -11]), [-1, -11, 1, 11])

    def test_large_numbers(self):
        self.assertEqual(order_by_points([123, 456, 789]), [123, 456, 789])

    def test_index_based_sorting(self):
        self.assertEqual(order_by_points([1, 11, -1, -11, -12]), [-1, -11, 1, -12, 11])

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for different scenarios:

- An empty list
- Lists with only positive numbers
- Lists with only negative numbers
- Lists with both positive and negative numbers
- Lists with large numbers
- Lists with numbers that have the same sum of digits, ensuring that they are sorted based on their index in the original list

Each test case verifies that the output of the `order_by_points` function matches the expected result.