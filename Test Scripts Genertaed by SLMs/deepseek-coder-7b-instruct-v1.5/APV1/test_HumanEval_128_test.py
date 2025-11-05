You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_128_code import prod_signs

class TestProdSigns(unittest.TestCase):
    def test_empty_arr(self):
        self.assertIsNone(prod_signs([]))

    def test_all_positive_numbers(self):
        self.assertEqual(prod_signs([1, 2, 2, 4]), 15)

    def test_all_negative_numbers(self):
        self.assertEqual(prod_signs([-1, -2, -2, -4]), -15)

    def test_mixed_numbers(self):
        self.assertEqual(prod_signs([1, -2, 2, -4]), -9)

    def test_with_zero(self):
        self.assertEqual(prod_signs([0, 1]), 0)

    def test_with_single_zero(self):
        self.assertEqual(prod_signs([0]), 0)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for different scenarios:

- When the array is empty
- When all numbers are positive
- When all numbers are negative
- When there are both positive and negative numbers
- When there is a zero in the array
- When the array contains only a single zero

Each test checks that the function returns the correct output for the given input.