system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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


assistant

import unittest

# Function to be tested
from HumanEval_8_code import sum_product

class TestSumProduct(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))
    
    def test_empty_list(self):
        self.assertEqual(sum_product([]), (0, 1))

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestSumProduct` class that inherits from `unittest.TestCase`. It contains two test methods: `test_sum` and `test_empty_list`, which use the `assertEqual` method to check if the output of the `sum_product` function matches the expected results. The `unittest.main()` call at the end runs all the tests defined within this class.