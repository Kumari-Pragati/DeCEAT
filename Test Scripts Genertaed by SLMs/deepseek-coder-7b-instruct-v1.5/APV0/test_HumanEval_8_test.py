You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_8_code import sum_product
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """Return a pair (sum, product) for the given list of integers.
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    >>> sum_product([])
    (0, 1)
    """
    sum_value = 0
    prod_value = 1
    for n in numbers:
        sum_value += n
        prod_value *= n
    return sum_value, prod_value


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_8_code import sum_product

class TestSumProduct(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sum_product([]), (0, 1))

    def test_single_element(self):
        self.assertEqual(sum_product([5]), (5, 5))

    def test_multiple_elements(self):
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))

    def test_negative_elements(self):
        self.assertEqual(sum_product([-1, -2, -3, -4]), (-10, -24))

    def test_mixed_elements(self):
        self.assertEqual(sum_product([1, -2, 3, -4]), (-2, -12))

if __name__ == '__main__':
    unittest.main()


This script creates a TestSumProduct class that inherits from unittest.TestCase. It includes several test methods to test the sum_product function with different types of input. Each method asserts that the output of sum_product matches the expected output for a given input.

To run this script, you need to have the HumanEval_8_code module available in your Python environment, and the sum_product function should be defined in that module.