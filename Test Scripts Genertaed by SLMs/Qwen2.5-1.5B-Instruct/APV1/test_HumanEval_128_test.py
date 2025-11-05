system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_128_code import prod_signs
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    """
    if not arr:
        return None
    prod = 0 if 0 in arr else (-1) ** len(list(filter(lambda x: x < 0, arr)))
    return prod * sum([abs(i) for i in arr])


assistant

import unittest

# Function to be tested
from HumanEval_128_code import prod_signs

class TestProdSigns(unittest.TestCase):
    def test_empty_array(self):
        self.assertIsNone(prod_signs([]))

    def test_positive_numbers(self):
        self.assertEqual(prod_signs([1, 2, 2, -4]), -9)

    def test_negative_numbers(self):
        self.assertEqual(prod_signs([-1, -2, -2, 4]), 9)

    def test_zero_in_array(self):
        self.assertEqual(prod_signs([0, 1]), 0)

    def test_mixed_numbers(self):
        self.assertEqual(prod_signs([1, -2, 3, -4]), 24)

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `unittest` test case class named `TestProdSigns`. It includes several test methods to verify different scenarios as described in the docstring of the `prod_signs` function. The `unittest.main()` call at the end runs these tests when this script is executed directly.