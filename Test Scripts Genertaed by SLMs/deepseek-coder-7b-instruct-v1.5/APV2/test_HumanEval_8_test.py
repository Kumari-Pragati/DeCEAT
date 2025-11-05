You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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
Here is a unittest test suite for the provided Python function:


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
        self.assertEqual(sum_product([-1, 2, -3, 4]), (5, -12))

if __name__ == '__main__':
    unittest.main()


This suite includes tests for empty lists, lists with a single element, lists with multiple elements, lists with negative elements, and lists with mixed positive and negative elements. Each test verifies that the function returns the correct sum and product for the given input.